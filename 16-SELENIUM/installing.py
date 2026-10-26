from selenium import webdriver

driver = webdriver.Chrome()

url = "https://sadikturan.com"
driver.get(url)

input("Tarayıcıyı kapatmak için ENTER'a bas...")
driver.quit()
