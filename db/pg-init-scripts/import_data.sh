#!/bin/sh

set -e
set -u

function insert_data() {
    local database=$1
    psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL
	    INSERT INTO DATABASE $database;
EOSQL
}

if [ -n "$POSTGRES_MULTIPLE_DATABASES" ]; then
    echo "Multiple database creation requested: $POSTGRES_MULTIPLE_DATABASES"
    for db in $(echo $POSTGRES_MULTIPLE_DATABASES | tr ',' ' '); do
        create_user_and_database $db
    done
    echo "Multiple databases created"
fi
