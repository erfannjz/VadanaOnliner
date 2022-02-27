import pyautogui as pygui
from selenium import webdriver
from selenium.webdriver.common.by import By
from os import devnull
from json5 import load

if __name__ != '__main__':

    with open('config/config.json', encoding='utf-8') as config:
        config = load(config)
        username = config['username']
        password = config['password']
        vadamap_url = config['vadamap_url']
        link_text = config['link_text']
        class_time = config['class_time']

    class Vadana:
        class_time = class_time
        
        def __init__(self):
            try:   
                self.driver = webdriver.Firefox(service_log_path=devnull)
            except:
                self.driver = webdriver.Chrome(service_log_path=devnull)
            self.driver.get(vadamap_url)

        def onliner(self):
            try:
                self.driver.find_element(By.CLASS_NAME, 'close').click()
            finally:
                self.driver.find_element(By.ID, 'username').send_keys(username)
                self.driver.find_element(By.ID, 'password').send_keys(password)
                self.driver.find_element(By.ID, 'loginbtn').click()
                self.driver.find_element(By.PARTIAL_LINK_TEXT, 'کلاس های آنلاین').click()
                self.driver.find_element(By.PARTIAL_LINK_TEXT, link_text).click()
                self.driver.find_element(By.CLASS_NAME, 'aconbtnjoin').click()
                button = pygui.locateCenterOnScreen('images/button.png')
                pygui.moveTo(button)
                pygui.click()
            

        def offliner(self):
            self.driver.quit()
