#!/bin/bash
#usage : ./backup.bash X

currDate=$(date +"%Y-%m-%d %T")
cd ../database
sqlite3 "${currDate}".sqlar -Ac sqlite3.db
find *.sqlar | sort  -r | awk -v var=$1 'NR>var' | xargs -d '\n' rm