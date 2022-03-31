import sqlite3
import io
from sqlite3 import Error
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "database/sqlite3.db")
conn = sqlite3.connect(db_path)

# Open() function
with io.open('./backupdatabase_dump.sql', 'w') as p:
    # iterdump() function
    for line in conn.iterdump():
        p.write('%s\n' % line)

print(' Backup performed successfully!')
print(' Data Saved as backupdatabase_dump.sql')

conn.close()
