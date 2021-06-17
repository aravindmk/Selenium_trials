from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time,os

browser = webdriver.Firefox()
browser.get('https://www.youtube.com/results?search_query=sreeragamo')

print("You are accessing :",browser.title)

#time.sleep(10)
#title = browser.find_elements_by_id("video-title")
#print(len(title))

filters = browser.find_element_by_css_selector("Filters")
filters.send_keys(Keys.RETURN)