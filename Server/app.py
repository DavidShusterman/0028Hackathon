import os
import tornado.ioloop
import tornado.web
import motor.motor_tornado

root = os.path.dirname(__file__)


def create_server_application(mongo_db_client,index_file):
    return tornado.web.Application([
        (r"/helloworld", ))



def main():
    pass



if __name__ == "__main__":
    main()
