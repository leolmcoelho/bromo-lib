from Bromo.bromo import Bromo
from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
#driver = webdriver.Chrome()
driver.get('https://www.google.com/')
br = Bromo(driver)
br.click('//*[contains(concat( " ", @class, " " ), concat( " ", "gb_f", " " ))]')