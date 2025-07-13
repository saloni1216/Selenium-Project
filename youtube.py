from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

query = input("Enter what you want to search on YouTube: ")

driver = webdriver.Chrome()
driver.get("https://www.youtube.com")
driver.maximize_window()
time.sleep(2)

search_box = driver.find_element(By.NAME, "search_query")
search_box.send_keys(query)
search_box.send_keys(Keys.RETURN)
time.sleep(3)

first_video = driver.find_elements(By.ID, "video-title")[0]
first_video.click()
time.sleep(25)

driver.quit()
