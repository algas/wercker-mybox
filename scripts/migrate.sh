mysql -h "$MYSQL_PORT_3306_TCP_ADDR" -P "$MYSQL_PORT_3306_TCP_PORT" -u "$MYSQL_ENV_MYSQL_USER" -p"$MYSQL_ENV_MYSQL_PASSWORD" -e "create table user(id int not null auto_increment, name varchar(255), primary key (id)); insert into user (name) values ('foo');" $MYSQL_ENV_MYSQL_DATABASE < scripts/create_table.sql
