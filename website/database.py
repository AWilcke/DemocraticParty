## database
import sqlite3
from queue import *

count = 0
queues = {}

def connect_db():
    return sqlite3.connect('mydb')

# initiliaze database
def init_db():
    global count
    db = connect_db()
    # erase queue of songs if one exists 
    db.cursor().execute('''DROP TABLE IF EXISTS songs''' + str(count))
    db.cursor().execute('''
        CREATE TABLE songs''' + str(count) +  ''' (songid INTEGER PRIMARY KEY autoincrement, 
        song TEXT not null, votes INTEGER, users TEXT not null)''')
    db.cursor().execute('''
        CREATE TABLE parties(partyid INTEGER PRIMARY KEY autoincrement, 
        party TEXT not null, password TEXT not null, songid INTEGER, 
        FOREIGN KEY(songid) references songs(songid))''')
    db.commit()
    db.close()
    count += 1

# delete database
def drop_db():
    db = connect_db()
    db.cursor().execute('''DROP TABLE IF EXISTS songs''' + str(count))
    db.cursor().execute('''DROP TABLE IF EXISTS parties''')
    db.commit()
    db.close()

# add party row into database
# create queue & table for songs 
def insert_party(party, password):
    global count
    db = connect_db()
    # create queue and add to end of list 
    q = Queue()
    queues[q] = count
    # create table for songs 
    songs_db = update_songs(party, password, q)
    db.cursor().execute('''INSERT INTO parties VALUES(?,?,?,?)''', (count, party, password, songs_db))
    db.commit()
    db.close()
    count += 1
    print party

#def get_party(party, password):
#    db = connect_db()
#    db.cursor().execute('''SELECT partyid, party, password, songid, songs''' + str(count) + ''' FROM parties WHERE party=? AND password=?''', (party, password))
#    db.close()
#    return db.cursor.fetchone()

def update_songs(party, password, queue):
    global count
    db = connect_db()
    index = queues.get(queue)
    # create new table & swap with existing table
    db.cursor().execute('''DROP TABLE IF EXISTS songs''' + str(index))
    db.cursor().execute('''
        CREATE TABLE songs''' + str(index) + '''(songid INTEGER PRIMARY KEY autoincrement, song TEXT not null,
                votes INTEGER, users TEXT not null)''')
    if (not queue.isEmpty()):
        for tup in queue:
            string = ''
            for word in tup[2]:
                string = string + ' ' + word
            db.cursor().execute('''INSERT INTO songs VALUES(,?,?,?)''', (tup[0], tup[1], string))
    db.commit()
    db.close()

def remove_party(party, password):
    db = connect_db()
    db.cursor().execute('''DELETE FROM parties WHERE party=? AND password=?''', (party, password))
    db.commit() 
    db.close()


# testing
'''drop_db()
init_db()
insert_party('seaside', 'e302')
insert_party('thanksbingedrinking', 'hamco')'''

# db.close()
