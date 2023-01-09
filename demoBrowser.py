from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.chrome.service import Service

service_obj = Service("C:/Users/neha rana/PycharmProjects/Drivers/chromedriver.exe")
driver = webdriver.Chrome(service= service_obj)
driver.get("https://www.facebook.com/")
#driver.implicitly_wait(10)
driver.close()
