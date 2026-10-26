from selenium import webdriver
from selenium.webdriver.common.by import By
import time 


driver = webdriver.Chrome()

url = "http://github.com"
driver.get(url)

searchInput = driver.find_element(By.NAME,"q")
time.sleep(100)
searchInput.send_keys("python")
time.sleep(100)

driver.close()