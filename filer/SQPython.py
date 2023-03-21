import sqlite3

def create_connection(db_file):
	conn = None
	try:
		conn = sqlite3.connect(db_file)
	except OSError as e:
		print(e)
	return conn

def select_all_tasks(conn):
	cur = conn.cursor()
	cur.execute("SELECT * FROM albums WHERE ArtistId = 3")

	rows = cur.fetchall()

	for row in rows:
		print(row)

conn = create_connection("music.db")
select_all_tasks(conn)
