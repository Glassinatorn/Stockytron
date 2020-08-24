#!/bin/sh

set -e
set -u

function create_user_and_database() {
    local DATABASE=$1
    echo "  Creating user and database '$DATABASE'"
    psql -v EXIT_ON_ERROR=1 --username "$POSTGRES_USER" <<-EOSQL
	    CREATE USER $DATABASE;
	    CREATE DATABASE $DATABASE;
	    GRANT ALL PRIVILEGES ON DATABASE $DATABASE TO $DATABASE;
EOSQL
}

if [ -n "$POSTGRES_DATABASES" ]; then
    echo "Multiple database creation requested: $POSTGRES_DATABASES"
    for DB in $(echo $POSTGRES_DATABASES | tr ',' ' '); do
        create_user_and_database $DB

        # creating and importing tables with data
        if [ $DB != $DB_DJANGO ]; then
            for FILE in /home/$DB/*.csv; do
                NAME=$(printf "$FILE" |
                    cut -d '/' -f 4 |
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
                    -U $POSTGRES_USER -d $DB

                psql -c "\copy \
                    $NAME
                    FROM $FILE csv" -U $POSTGRES_USER -d $DB
            done
        fi
    done

    echo "Multiple databases created"
fi
