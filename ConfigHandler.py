from configparser import ConfigParser
#A class that is used for the hadnling of the configuration file
class ConfigHandler:

    def __init__(self, file_path):
        self.file_path = file_path
        self.config = ConfigParser()
        

#returns a dictionary like object from which we can read the values of the 
#configuration file

    def get_parser(self):
        self.config.read(self.file_path)
        return self.config
    
    #create a self.file_path configuration file
    def create_config(self) -> None:

    #This section provides default values for the keys of every other section
        self.config['credentials'] = {
            'username': 'None',
            'password': 'None'
            
        }
        self.config['urls'] = {
            'comments_urls': 'None'
        }
        self.config['application'] = {
            'delay_between_comments' : 'None',
            'run_for_hours': 'None' # if we have "inf" as argument the script will run forever
            
        }
        try:
            with open(self.file_path, 'w+') as f:
                self.config.write(f)
        except IOError as error:
            
            print("Error: %s" % str(error))


# conf = ConfigHandler('/home/pi/WaterUnderground_IoT/config.ini')
# conf.create_config()

# parser = conf.get_parser()
# print(parser.get('Application','well_depth'))
