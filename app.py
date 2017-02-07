import tornado.ioloop
import tornado.web
import os
import MySQLdb

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

class UserHandler(tornado.web.RequestHandler):
    def __init__(self, connector):
        self.connector = connector

    def get(self, uid):
        cursor = self.connector.cursor()
        cursor.execute("select * from user")
        self.write("<br>".join([row[1] for row in cursor.fetchall() if len(row) > 1]))
        cursor.close()

def make_app():
    options = {
        'mysql_host': os.environ.get('MYSQL_PORT_3306_TCP_ADDR', 'localhost'),
        'mysql_port': int(os.environ.get('MYSQL_PORT_3306_TCP_PORT', 8888)),
        'mysql_user': os.environ.get('MYSQL_ENV_MYSQL_USER', 'test'),
        'mysql_pass': os.environ.get('MYSQL_ENV_MYSQL_PASSWORD', 'secret'),
        'mysql_database': os.environ.get('MYSQL_ENV_MYSQL_DATABASE', 'user'),
    }
    connector = MySQLdb.connect(
            host=options['mysql_host'],
            port=options['mysql_port'],
            user=options['mysql_user'],
            passwd=options['mysql_pass'],
            db=options['mysql_database'])

    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/user/(.*)", UserHandler, dict(connector=connector)),
    ])

def main(port):
    app = make_app()
    app.listen(port)
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    port = int(os.environ.get('PORT', '8888'))
    main(port)
