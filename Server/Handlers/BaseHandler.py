import tornado.ioloop
import tornado.web

class BaseHandler(tornado.web.RequestHandler):
    """
    Base handler for all handlers.
    """
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "http://localhost:3000")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')