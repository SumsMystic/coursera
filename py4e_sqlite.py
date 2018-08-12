'''
Created on July 15, 2018

@author: Sumeet Agrawal
'''

import sqlite3

# Create DB connection objects
conn = sqlite3.connect('D:\PythonLearning\db\coursera_assignments.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'D:\PythonLearning\test_files\mbox.txt'
fh = open(fname, 'r')
commit_cntr = 0

for line in fh:
    
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]

    domain = email.split('@')[1]
    org = domain.split('.')[0]
    
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (domain,))
    row = cur.fetchone()
    if row is None:
        cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (domain,))
        commit_cntr += 1
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (domain,))
        commit_cntr += 1
    
    if commit_cntr == 10:
        conn.commit()
        commit_cntr = 0
    
conn.commit()

# https://www.sqlite.org/lang_select.html
cur.execute('SELECT org, count FROM Counts ORDER BY count DESC')
max_email_count = cur.fetchone()[1]


print(max_email_count)
cur.close()

