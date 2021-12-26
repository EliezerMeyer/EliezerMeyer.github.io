from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

path = "C:\Windows\chromedriver.exe"

driver = webdriver.Chrome(path)

driver.get("https://www.wipo.int/global_innovation_index/en/2021/")
link = driver.find_element(By.LINK_TEXT, "Download the Global Innovation Index 2021")
link.click()
