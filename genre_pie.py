import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

def get_genre(cnx, genre):
	cursor = cnx.cursor()
	cursor.execute('select count(title) from movies_seen where genre like %s', (genre,))
	for a in cursor:
		genre_count = a[0]
	cursor.close()
	return genre_count

def gather(cnx):
	genre_query = ['%Comedy%', '%Fantasy%', '%Romance%', '%Drama%', '%Science Fiction%', '%Horror%', '%Crime%', '%Action%', '%Mystery%'] 
	m_data = []
	for i in range(0, len(genre_query)):
		query_count = get_genre(cnx, genre_query[i])
		m_data.append(query_count)
	plot_results(m_data)

def plot_results(m_counts):
	labels = 'Comedy', 'Fantasy', 'Romance', 'Drama', 'Science Fiction', 'Horror', 'Crime', 'Action', 'Mystery'
	sizes = m_counts
	plt.rcParams['font.size'] = '10.0'
	#Colors (in order) -- green, red, white, blue, yellow, gray, orange, cyan, magenta
	colors = ['#15A509', '#A54209', '#FFFFFF', '#1D48DC', '#CDDA11', '#DC731D', '#ACA5A8', '#48DBBA', '#A7155E']
	p_chart = plt.pie(sizes, startangle=290, autopct ='%1.1f%%', colors = colors)
	title = plt.title('Genre of Movies Seen in Past Year')
	title.set_ha("center")
	plt.gca().axis('equal')
	plt.legend(p_chart[0], labels, bbox_to_anchor=(0.97, 0.5), loc="center right", bbox_transform=plt.gcf().transFigure)
	plt.subplots_adjust(left=0.0, bottom=0.05, right=0.7)
	for i in range(0, len(m_counts)):
		p_chart[0][i].set_linewidth(0.1)
	#plt.show()
	plt.savefig('genre_pie.png')
