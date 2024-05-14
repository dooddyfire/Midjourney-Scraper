
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
import time
import requests 
from seleniumbase import Driver
import pandas as pd 

url = input("Enter midjourney showcase url : ")

filename = input("Enter your filename : ")
total = int(input("Enter your total image : (0 is scrape all page)")) 

driver = Driver(uc=True)

driver.get(url)

input("Please Login and Press Enter : ")
#time.sleep(3)

lis = [ i.get_attribute('href') for i in driver.find_elements(By.CSS_SELECTOR,'a.bg-cover')]


link_lis = []
img_lis = []
desc_lis = []

c = 1 



for item in lis[:total]:


    print(item)

    link_lis.append(item)

    driver.get(item)
    time.sleep(3)

    # img = driver.find_element(By.CSS_SELECTOR, "img.w-full").get_attribute('src')
    # img_lis.append(img)
    # print(img)

    try:
        desc = driver.find_element(By.CSS_SELECTOR,'#lightboxPrompt').find_element(By.CSS_SELECTOR,'p').text 
        desc_lis.append(desc)
        print(desc)
    except: 
        print("ไม่มี")
        desc_lis.append("ไม่มี")

    
    c = c + 1


df = pd.DataFrame()
df['Link'] = link_lis 
df['Description'] = desc_lis 

df.to_excel(f"{filename}.xlsx")
print("All Done Enjoy!!!!")

