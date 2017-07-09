import matplotlib.pyplot as plt
import numpy as np

def execute(cnx, start_year, end_year):
	cursor = cnx.cursor()
	query = 'select count(title) from movies_seen where year >=' + start_year + ' and year <= ' + end_year
	cursor.execute(query)
	for a in cursor:
		result = a[0]
	cursor.close()
	return result

def gather(cnx):
	year_query = ['1950', '1960', '1970', '1980', '1990', '2000', '2010', '2020']
	m_data = []
	i = 0
	j = 1
	while j < len(year_query):
		query_count = execute(cnx, year_query[i], year_query[j])
		j += 1
		i += 1
		m_data.append(query_count)
	plot_results(m_data)

def plot_results(m_counts):
	fig, ax1 = plt.subplots(figsize=(12,9))
	fig.subplots_adjust(left = 0.1, right = 0.92)

	pos = np.arange(len(m_counts))

	rects = ax1.bar(pos, m_counts, align = 'center', color = 'blue')
	x_ticks = ['1950-1959', '1960-1969', '1970-1979', '1980-1989', '1990-1999', '2000-2009', '2010-2019']
	ax1.set_xticks(pos)
	ax1.set_xticklabels(x_ticks)
	ax1.set_xlabel('Decade')
	ax1.set_ylabel('Number of movies')
	ax1.set_title('Release Date of Movies Seen in Past Year')

	i = 0
	for rect in rects:
		ax1.text(rect.get_x() + rect.get_width()/2.0, rect.get_height() + 0.1, m_counts[i], va = 'bottom', color = 'black')
		i += 1
	plt.yticks(np.arange(0, 31, 5.0))
	plt.show()
