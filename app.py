import tornado.ioloop
import tornado.web
import os

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

class NameHandler(tornado.web.RequestHandler):
    def get(self, name):
        self.write("Hello, %s" % (name))

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/hello/(.*)", NameHandler),
    ])

def main(port):
    app = make_app()
    app.listen(port)
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    port = int(os.environ.get('PORT', '8888'))
    main(port)
