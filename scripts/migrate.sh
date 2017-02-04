mysql -h "$MYSQL_PORT_3306_TCP_ADDR" -P "$MYSQL_PORT_3306_TCP_PORT" -u "$MYSQL_USER" -p"$MYSQL_PASSWORD" -e "create table user(id int);" $MYSQL_DATABASE
