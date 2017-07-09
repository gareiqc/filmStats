import mysql.connector
import sys
import dec_bar as dcb

def authenticate(creds):
	keys = []
	try:
		with open(creds, 'r') as f:
			keys = [line.strip() for line in f]
	except:
		print "There was a problem with the input file."
		sys.exit(0)
	return mysql.connector.connect(user=keys[0],password=keys[1],database=keys[2])

if __name__ == "__main__":
	cnx = authenticate(sys.argv[1])
	dcb.gather(cnx)
	cnx.close()
