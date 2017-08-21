import os
import tornado.ioloop
import tornado.web
import motor.motor_tornado

root = os.path.dirname(__file__)


def create_server_application(mongo_db_client,index_file):
    return tornado.web.Application([
        (r"/helloworld", ))


def write_authenticated_user_to_server(username,password,dbhandler):
    dbhandler.Authenticated.insert_one({"username":username,"password":password})


def main():
    cfg_path = get_configuration_file()
    config_reader = ConfigReader(cfg_path)
    mongo_connection_string = os.environ.get('MONGO_CONN_STRING','localhost')
    mongo_db_name = config_reader.get_value("mongoDBName")
    mongo_db_connection = motor.motor_tornado.MotorClient(mongo_connection_string)
    mongo_db_client = mongo_db_connection[mongo_db_name]
    publisher = get_publisher(cfg_path)
    index_file = get_index_file()
    app = create_server_application(mongo_db_client,publisher,index_file)
    server_port = config_reader.get_value("serverPort")
    server_host= config_reader.get_value("serverHost")
    app.listen(server_port,address=server_host)
    tornado.ioloop.IOLoop.current().start()



if __name__ == "__main__":
    main()
