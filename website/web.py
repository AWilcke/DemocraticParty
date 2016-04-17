# all the imports
import sqlite3
from database import *
from contextlib import closing
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash

# create our little application :)
app = Flask(__name__)

app.config.update(dict(
    DATABASE= './base.db',
    DEBUG=True,
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_object(__name__)

def connect_db():
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

@app.cli.command('initdb')
def initdb_command():
    """Creates the database tables."""
    init_db()
    print('Initialized the database.')


def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


@app.before_request
def before_request():
    g.db = connect_db()
    global queues
    init_db()
    insert_party('baba', 'bexe')
    par = get_party('baba', 'bexe')
    print 'par is:'
    print par
    print queues
    q = [b for (a, b) in queues if (a == par)][0]
    q.enqueue('Hello', 'user1', 'n')
    q.enqueue('7 Years', 'user1', 'm')
    q.enqueue('Stressed Out', 'user1', 'n')
    q.enqueue('I Was Wrong', 'user1', 'b')
    q.vote('7 Years', 'user1', 1)
    q.vote('7 Years', 'user2', 1)
    q.vote('Hello', 'user1', 1)
    q.vote('Stressed Out', 'user2', -1)
    q.enqueue('Sorry', 'user1', 'e')
    q.vote('7 Years', 'user3', 1)
    q.vote('Hello', 'user3', 1)
    q.vote('Sorry', 'user4', 1)
    q.sort()
    update_songs('baba', 'bexe', q)

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()
        
@app.route('/')
def show_entries():
    curr = g.db.cursor().execute('select party, partyid from parties')
    entries = [dict(party=row[1], partyid=row[0]) for row in cur.fetchall()]
    return render_template('show_entries.html', entries=entries)

############################################
#
# new party -> call insert_party(party, password)
#
# song requested -> 
#   call get_party(party, password)
#   find appropriate queue from global queues array in database
#   add song to queue -> queue.enqueue(song, userid, url)
#   call update_songs(party, password, queue)
#
# vote -> 
#   call get_party(party, password)
#   find appropriate queue from global queues array in database
#   vote on song in queue -> queue.vote(song, userid, num)
#   call update_songs(party, password, queue)
#   
############################################

if __name__ == '__main__':
    app.run()
    