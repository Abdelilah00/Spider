import sqlite3
import io
from sqlite3 import Error
import os.path
from datetime import datetime
import glob
import os

#init vars
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "../database/sqlite3.db")
limit = 1 + 5
conn = sqlite3.connect(db_path)

# create a buckup
db = 'backupdatabase_dump' + str(datetime.now()) + '.sql'
with io.open('../database/' + db, 'w') as p:
    # iterdump() function
    for line in conn.iterdump():
        p.write('%s\n' % line)

print(' Backup performed successfully!')
print(' Data Saved as ' + db)
conn.close()

# Get list of all files in a given directory sorted by name
excluded_files = sorted(filter(os.path.isfile, glob.glob(os.path.join(BASE_DIR, "../database/*"))))
excluded_files = excluded_files[-limit:]

# delete old backups
for clean_up in glob.glob(os.path.join(BASE_DIR, "../database/*")):
    if clean_up not in excluded_files:
        os.remove(clean_up)
