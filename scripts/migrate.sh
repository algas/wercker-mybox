env
mysql -h "$MYSQL_PORT_3306_TCP_ADDR" -P "$MYSQL_PORT_3306_TCP_PORT" -u root -p$MYSQL_ENV_MYSQL_ROOT_PASSWORD -e "create database user;"
