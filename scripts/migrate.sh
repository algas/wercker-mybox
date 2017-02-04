echo $MYSQL_PORT_3306_TCP_ADDR
echo $MYSQL_PORT_3306_TCP_PORT
mysql -h "$MYSQL_PORT_3306_TCP_ADDR" -P "$MYSQL_PORT_3306_TCP_PORT" -u "foo" -p"bar" "user" < ./scripts/create_table.sql
