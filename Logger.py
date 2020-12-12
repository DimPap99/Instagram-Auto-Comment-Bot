import logging
import os
from pathlib import Path
import datetime
import platform, time

def sys_info():
    arch=platform.architecture()
    cpu ='CPU type: {} / CPU count: {} / CPU class: {}' .format(platform.machine(), os.cpu_count(), platform.processor())
    os_plt = 'OS platform: {}-{}-{} / OS version: {}' .format(arch[0], str(os.name).upper(), arch[1], platform.platform())
    py_vers = 'Python version: {} ({}) / Python build: {}' .format(platform.python_version(), platform.python_implementation(), platform.python_compiler())
    return (cpu, os_plt, py_vers)
    # print(platform.node())
    # print(platform.release())
    # print(platform.system())
    # print(platform.uname())

 

def version_info(str_appname, str_appversion, str_appcopyright):
    vers_info = str_appname + ', version: ' + str_appversion + '\n'+ str_appcopyright
    return vers_info
    

 

#print_version_info('PyTest example','0.1 (beta)','Copyright (c) <author> 2020, Licence: CC-BY-SA/4.0i')

class Logger:
    
    
# initializes a logger based on the attributes of the class
    def init_logger(self, level):
        
        #write sys info only once in the beggining
        if os.path.exists(self.path) is False:
            vers_inf = self.version_info('InstaBot', '0.0.1', 'Copyright (c) 2020 Papadimitriou Dimitris, MIT License')
            inf = self.sys_info()
            sys_inf = inf[0] + '\n' + inf[1] + '\n' + inf[2]
            try:
                with open(self.path, 'w') as f:
                    f.write(vers_inf)
                    f.write(sys_inf)
            except IOError:
                print(IOError + ' at logger init.')
        logger = logging.getLogger(self.path)
        logger.setLevel(level)
        formatter = logging.Formatter(fmt='%(asctime)s %(levelname)-8s %(message)s',datefmt='%m-%d-%y %H:%M:%S')
        fh = logging.FileHandler(self.path)
        fh.setFormatter(formatter)
        self.file_handler = fh
        logger.addHandler(fh)
        
        return logger

    def sys_info(self):
        arch=platform.architecture()
        cpu ='\nCPU type: {} / CPU count: {} / CPU class: {}' .format(platform.machine(), os.cpu_count(), platform.processor())
        os_plt = 'OS platform: {}-{}-{} / OS version: {}' .format(arch[0], str(os.name).upper(), arch[1], platform.platform())
        py_vers = 'Python version: {} ({}) / Python build: {}' .format(platform.python_version(), platform.python_implementation(), platform.python_compiler())
        return (cpu, os_plt, py_vers)

    def version_info(self,str_appname, str_appversion, str_appcopyright):
        vers_info = str_appname + ', version: ' + str_appversion + '\n'+ str_appcopyright
        return vers_info

    def __init__(self, file_name, verbose:bool, level, date:str):
        
        self.file_name =  date + '_'+ file_name +'.log'# the file name along with the date of creation
        self.path = os.path.join(os.path.dirname(__file__), self.file_name) # the full path of the log file
        self.verbose = verbose # dictates whether everything will be logged or important information
        self.level = level # logging level
        self.logger = self.init_logger(level)
        
        #logging.basicConfig(filename=self.path, level=self.level, format='%(asctime)s:%(levelname)s:%(message)s')
    # get the parent dir of the directory from which we executed the script
    def get_parent_dir(self):
        current_dir = Path(os.path.dirname(__file__))
        
        return current_dir.parent
    #pressure_stability_checks the current date and the date of the log file
    # if they differ the log file is saved at the Logs directory 
    # and we create a new log file for the new date
    def check_log_renewal(self):
        try:
            dt_now = datetime.datetime.now()
            now = [dt_now.second, dt_now.minute, dt_now.hour, dt_now.hour, dt_now.day, dt_now.month, dt_now.year]
            
            log_date = list(map(int, self.file_name.split('_')[0].split('-')))

            
            # check D/M/Y of the rtc and the file
            if (now[4] == log_date[0] and now[5] == log_date[1] and now[6] == log_date[2]) is False:
                self.log_info("Changing Logs.")
                logging.shutdown()
                self.move_to_LOG_dir() #move the old log initialize a new one
                os.remove(self.path) # remove the old log
                
                self.file_name = str(now[4])+'-'+str(now[5])+'-'+str(now[6]) + '_' + self.file_name.split('_')[1]  +'.log' 
                print(self.file_name)
                self.path = os.path.join(os.path.dirname(__file__), self.file_name)
                self.logger = self.init_logger(self.level)
                self.log_info('Added new logger')
            else:
                print(True)
        except Exception as e:
            self.log_error("Error: %s" %str(e))
        

    #moves the log file to the Log dir if it exists if it doesnt it creates it and then moves the file
    
    def move_to_LOG_dir(self):
        current_dir = Path(os.path.dirname(__file__))
        logs_dir = os.path.join(self.get_parent_dir(),"Logs")
        #print(logs_dir)
        try:
            if os.path.isdir(logs_dir):
                if os.path.isfile(os.path.join(logs_dir, self.file_name)) is False:
                    os.rename(self.path, os.path.join(logs_dir, self.file_name) )
            else:
                os.makedirs(logs_dir)
                os.rename(os.path.join(current_dir, self.file_name), os.path.join(logs_dir, self.file_name) )
        except Exception as error:
            print(error)
# logging levels
    def log_info(self, message):
        self.logger.info(message)

    def log_debug(self, message):
        if self.verbose is True:
            self.logger.debug(message)

    def log_error(self, message):
        self.logger.error(message)

    def log_warning(self, message):
        self.logger.warning(message)


    

