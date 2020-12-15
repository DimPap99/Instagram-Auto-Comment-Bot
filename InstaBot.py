from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random, os, time, sys, logging, datetime
from ConfigHandler import ConfigHandler
from Logger import Logger
from selenium.webdriver.support.wait import WebDriverWait

class InstaBot(object):


    names_list = ['@nick_giannakopoylos ', '@kwstas.daras ', '@g_chatzo ',
     '@skot_d_stef ', '@aristos_chalvadakis ', '@amarildo.doci ', '@anthimosfam ', '@swtria.anyf ', 
     '@thanasis_zois ', '@xristos_kn ', '@zaxariouu_mi ', '@labros_cass ' ]


    def __init__(self, user, password, photo_url):
        self.driver = webdriver.Chrome(executable_path='./chromedriver.exe')
        self.password = password
        self.user = user
        self.photo_url = photo_url
    

    def connect(self):
        
        self.driver.get("https://instagram.com")
        time.sleep(5)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Accept')]")\
            .click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(self.user)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(self.password)
        self.driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()
        time.sleep(5)
        # WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Not Now')]"))).click()
        # WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Not Now')]"))).click()

        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
            .click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
            .click()
        time.sleep(2)
        self.driver.get(self.photo_url)
        time.sleep(2)
        
        return True
    @classmethod
    def generate_comment(cls)->list:
        temp_list = cls.names_list.copy()
        names = []
        for i in range(0, 3):
            index = random.randint(0, len(temp_list) - 1)
            names.append(temp_list[index])
            temp_list.remove(temp_list[index])

        return ''.join(names)
    
    def make_comment(self):
        commentArea = self.driver.find_element_by_class_name('Ypffh')
        commentArea.click()
        time.sleep(5)
        commentArea = self.driver.find_element_by_class_name('Ypffh')
        commentArea.click()
        commentArea.send_keys(InstaBot.generate_comment())
        self.driver.find_element_by_xpath("//button[contains(text(), 'Post')]")\
            .click()
        time.sleep(2)
    
    def start(self):
        if self.connect() is True:
            start = time.time()
            counter = 0
            while time.time() - start <= (5 * 3600):
                self.make_comment()
                counter += 1
                time.sleep(38)
