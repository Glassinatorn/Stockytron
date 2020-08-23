#!/bin/bash

# creating and importing tables with data
for FILE in /home/*.csv; do
    NAME=$(printf "$FILE" |
        cut -d '/' -f 3 |
        cut -d '.' -f 1 |
        tr '[:upper:]' '[:lower:]')

    psql -c "CREATE TABLE $NAME \
        (date date PRIMARY KEY, \
        open FLOAT, \
        high FLOAT, \
        low FLOAT, \
        close FLOAT, \
        adj FLOAT, \
        volume FLOAT);" \
        -U django -d intraday

    psql -c "\copy \
        $NAME
        FROM $FILE csv" -U django -d intraday
done
