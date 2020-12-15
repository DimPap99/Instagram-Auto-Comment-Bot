from InstaBot import InstaBot
from Logger import Logger
from ConfigHandler import ConfigHandler
import sys, os , datetime, time, logging
import pickle
def save(data):
    with open('./data.p', 'wb') as fp:
        pickle.dump(data, fp, protocol=pickle.HIGHEST_PROTOCOL)
def load_data(path) ->dict:
    if os.path.isfile(path):
        with open(path, 'rb') as f:
            comments = pickle.load(f)
            
    else:
        comments = {}
        comments['number'] = 0
    return comments

def main(logger):
    script_dir = os.path.dirname(__file__)
    conf = ConfigHandler(os.path.join(script_dir,'config.ini'))
    try: 
        
        if os.path.isfile(os.path.join(script_dir,'config.ini')) is True:
            parser = conf.get_parser()
        else:
            conf.create_config()
            parser = conf.get_parser()
    except Exception as e:
        
        logger.log_error("Error: %s" % str(e))
        raise RuntimeError

    
    try:
        print(parser.get('urls', 'comments_urls'))
        
        bot = InstaBot(parser.get('credentials', 'username'), parser.get('credentials', 'password'), parser.get('urls', 'comments_urls'))
        bot.start()   
        
    except KeyboardInterrupt:
        print(comments)
        raise RuntimeError


if __name__ == "__main__":
    try:
        comments = load_data('./data.p')
        dt_now = datetime.datetime.now()
        date = [dt_now.second, dt_now.minute, dt_now.hour, dt_now.hour, dt_now.day, dt_now.month, dt_now.year]
        logger = Logger('instabot',True,logging.DEBUG, str(date[4])+'-'+str(date[5])+'-'+str(date[6]))
    except Exception as error:
        print(error)
        sys.exit(-1)
    try:
        main(logger)
    except Exception as e:
        logger.log_error("Error: %s" % str(e))
    finally:
        save(comments)
    