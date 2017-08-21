import os
import tornado.ioloop
import tornado.web
import motor.motor_tornado
from Handlers.HelloWorldHandler import HelloWorldHandler

root = os.path.dirname(__file__)


def create_server_application(mongo_db_client):
    return tornado.web.Application([
        (r"/helloworld",HelloWorldHandler)])


def main():
    mongo_connection_string = 'localhost'
    mongo_db_name = 'hackathonDB'
    mongo_db_connection = motor.motor_tornado.MotorClient(mongo_connection_string)
    mongo_db_client = mongo_db_connection[mongo_db_name]

    app = create_server_application(mongo_db_client)
    app.listen(port=8000,address="0.0.0.0")
    tornado.ioloop.IOLoop.current().start()



if __name__ == "__main__":
    main()
