mysql -e 'create database user' -h mariadb -u $MYSQL_USER -p$MYSQL_PASS
mysql -u $MYSQL_USER -p$MYSQL_PASS < ./scripts/create_table.sql
