import sqlite3

con = sqlite3.connect('test_db.sqlite')
cur = con.cursor()

query_1 = '''
CREATE TABLE IF NOT EXISTS laws(
    id INTEGER PRIMARY KEY,
    title TEXT,
    text TEXT,
    year INTEGER
);
'''
query_2 = '''
CREATE TABLE IF NOT EXISTS authors(
    id INTEGER,
    author TEXT,
    country TEXT
    )
'''
query_3 = '''
CREATE TABLE IF NOT EXISTS sections(
    id INTEGER,
    section TEXT
    )
'''
cur.execute(query_1)
cur.execute(query_2)
cur.execute(query_3)
con.close()
