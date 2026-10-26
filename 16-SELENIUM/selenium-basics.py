from selenium import webdriver
import time
driver = webdriver.Chrome()

url = "http://github.com"
driver.get(url)

time.sleep(2)
driver.maximize_window()  #maximize_window açılan ekranı tam ekran yapar. 
driver.save_screenshot("github.com-homepage.png") #save_screenshot açılan ekranı ekran görüntüsü alıp kayıt eder.

url = "http://github.com/sadikturan"
driver.get(url)
if "sadikturan" in driver.title:
    driver.save_screenshot("github-sadikturan.png")

print(driver.title)

time.sleep(2) #sayfayı 2 saniye bekletir 

driver.back() #gittiği sayfadan 1 sayfa geri gelir eğer driver.forward yazarsa 1 sayfa ileri gider.

time.sleep(2)

driver.close()