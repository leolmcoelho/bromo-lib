from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver



class MyLib():
    def __init__(self, driver):
        ''' if driver == 'chrome':
            self.driver = webdriver.Chrome(ChromeDriverManager().install())'''
        self.driver = driver
    
    def click(self, tag, method = 'xpath', time=10):
        if method == 'xpath':
            element = WebDriverWait(self.driver, time).until(
                EC.element_to_be_clickable((By.XPATH, tag)))
            element = self.driver.find_element_by_xpath(tag)
            
        if method == 'id':
            element = WebDriverWait(self.driver, time).until(
                EC.element_to_be_clickable((By.ID, tag)))
            element = self.driver.find_element_by_id(tag)

        if method == 'class':
            element = WebDriverWait(self.driver, time).until(
                EC.element_to_be_clickable((By.CLASS_NAME, tag)))
            element = self.driver.find_element_by_class_name(tag)
                    
      
        return element.click()
    
    def write(self, tag, message, method='xpath', time=10):
        if method == 'xpath':
            WebDriverWait(self.driver, time).until(
                EC.element_to_be_clickable((By.XPATH, tag)))
            element = self.driver.find_element_by_xpath(tag)
            
        if method == 'id':
            WebDriverWait(self.driver, time).until(
                EC.presence_of_element_located((By.ID, tag)))
            element = self.driver.find_element_by_id(tag)
            
        if method == 'class':
            WebDriverWait(self.driver, time).until(
                EC.presence_of_element_located((By.CLASS_NAME, tag)))
            element = self.driver.find_element_by_class_name(tag)
            
        element.clear()
        return element.send_keys(str(message))
    
    def located(self, tag, time=10,  method='xpath'):
        if method == 'xpath':
            WebDriverWait(self.driver, time).until(
                EC.presence_of_element_located((By.XPATH, tag)))

        if method == 'id':
            WebDriverWait(self.driver, time).until(
                EC.presence_of_element_located((By.ID, tag)))

        if method == 'class':
            WebDriverWait(self.driver, time).until(
                EC.presence_of_element_located((By.CLASS_NAME, tag)))

    def key(self, tag, key = 'enter',  time='10',method='xpath'):
        if method == 'xpath':                           
            WebDriverWait(self.driver, time).until(
                EC.presence_of_element_located((By.XPATH, tag)))
            element = self.driver.find_element_by_xpath(tag)
            
        if method == 'id':
            WebDriverWait(self.driver, time).until(
                EC.presence_of_element_located((By.ID, tag)))
            element = self.driver.find_element_by_id(tag)
            
        if method == 'class':
            WebDriverWait(self.driver, time).until(
                EC.presence_of_element_located((By.CLASS_NAME, tag)))
            element = self.driver.find_element_by_class_name(tag)
                   
        if key == 'enter':
            return element.send_keys(Keys.ENTER)

        if key == 'esc':
            return element.send_keys(Keys.ESCAPE)



     