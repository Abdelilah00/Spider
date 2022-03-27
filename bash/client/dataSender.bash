#!/bin/bash
jq -Rsn '
    [inputs
     | . / "\n"
     | (.[] | select(length > 0) | . / " ") as $input
     | {"storage": $input[0],"memory": $input[1], "cpu": $input[2], "user": $input[3]}]
' <logs.txt > logs.json

curl -X POST -d  @logs.json -H 'Content-Type: application/json' http://localhost:8080/collector
