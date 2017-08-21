import tornado.ioloop
import tornado.web
from Handlers.BaseHandler import BaseHandler


class HelloWorldHandler(BaseHandler):
    def get(self):
        self.set_status(200)
        self.write("Hello World!")
