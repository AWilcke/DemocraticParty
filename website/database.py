## database
import sqlite3

# initiliaze database
def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

# delete database
def drop_db():
	with closing(connect_db()) as db:
	    db.cursor.execute('''DROP TABLE parties''')
	    db.commit()


def insert_party(party, password):
	with closing(connect_db()) as db:
		db.cursor.execute('''INSERT INTO parties(id, party, password, songid, songs) VALUES(,?,?,?,?)''', (party, password, 1, songs))
		db.commit()

def get_party(party, password):
	with closing(connect_db()) as db:
		db.cursor.execute('''SELECT id, party, password, songid, songs FROM parties WHERE party=? AND password=?''', (party, password))
		return db.cursor.fetchone()

def update_songs(party, queue):
	with closing(connect_db()) as db:
		# create new table & swap with existing table
		cursor = db.cursor()
		cursor.execute('''
		    CREATE TABLE songs(songid INTEGER PRIMARY KEY autoincrement, song TEXT not null,
		                       votes INTEGER, users TEXT not null)
		''')
		for tup in queue:
			cursor.execute('''INSERT INTO songs(songid, song, votes, users) VALUES(,?,?,?)''', (tup[0], tup[1], tup[2]))
		db.commit()

def remove_party(party, password):
	with closing(connect_db()) as db:
		db.cursor.execute('''DELETE FROM parties WHERE party=? AND password=?''', (party, password))
		db.commit(); 
