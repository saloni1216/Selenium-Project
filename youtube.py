              
# Import Selenium WebDriver
from selenium import webdriver 
# Used to locate elements
from selenium.webdriver.common.by import By 
 # For pressing Enter key
from selenium.webdriver.common.keys import Keys 
# To pause between steps
import time                                  

# Ask the user what they want to search on YouTube
query = input("Enter what you want to search on YouTube: ")

# Launch Chrome browser
driver = webdriver.Chrome()

# Open YouTube website
driver.get("https://www.youtube.com")

# Maximize the browser window
driver.maximize_window()

# Wait for YouTube homepage to load
time.sleep(2)

# Find the search input box by its name and type the user's query
search_box = driver.find_element(By.NAME, "search_query")
search_box.send_keys(query)          # Type the search keyword
search_box.send_keys(Keys.RETURN)    # Press Enter to search

# Wait for the search results to load
time.sleep(3)

# Click the first video in the search results
first_video = driver.find_elements(By.ID, "video-title")[0]
first_video.click()

# Let the video play for 30 seconds
time.sleep(25)

# Close the browser
driver.quit()
