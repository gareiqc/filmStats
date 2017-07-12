# filmStats
A project spawned from my own curiosity of the statistics that could be produced by performing queries on a database of movies that I have seen

## How it works
This program uses mySQL connector to connect to a local database

For now, the program generates:

-A bar graph of the number of movies that I have seen in each decade starting from 1950 (dec_bar.py)

-A pie chart of the percent of movies that I have seen of each genre (genre_pie.py)

## Execution
This program can be executed by the following command:

`python movies.py keys.txt`

Note: the input file `keys.txt` is user-specific since it contains all keys -- public and private -- needed for the script to run properly.

## Format of `keys.txt`

	<mySQL username>
	<mySQL password>
	<mySQL database name>

