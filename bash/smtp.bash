#!/bin/bash

SERVER="smtp.gmail.com"
FROM="testsmtp631@gmail.com"
TO="testsmtp631@gmail.com"
SUBJ="subject"
MESSAGE="test message"
CHARSET="utf-8"

sendemail -f $FROM -t $TO -u $SUBJ -s $SERVER -m $MESSAGE -v -o message-charset=$CHARSET

# https://linuxhint.com/bash_script_send_email/