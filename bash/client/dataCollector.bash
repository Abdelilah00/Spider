#!/bin/bash
# collect the data
#for user in `w | awk '{if(NR>2)print $1}' | sort -u`
stats= "storage memory cpu user"
#for user in $(ps aux | grep -v COMMAND | awk '{print $1}' | sort -u); do
for user in $(users); do
  #todo: fix this line
  gb= $(df -h /home/$user | awk '{if(NR>1) print $2}')
  if $gb; then
    gb=0
  fi
  stats="$stats\n$gb $(ps aux | egrep ^$user | awk 'BEGIN{memory=0;cpu=0}; {memory += $4;cpu += $3} ;END{print memory" "cpu,$1}')"
done

# sort data numerically (largest first)
echo -e $stats | grep -v ^$ | sort -rn | head >./logs.txt
