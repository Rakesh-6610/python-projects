from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pickle
import time
import os
from dotenv import load_dotenv


load_dotenv()

username = os.getenv("EMAIL")
password = os.getenv("FACEBOOK_PASSWORD")
recipient = "Rakesh Karmaker"
message = "Hello there, this message is from python"


driver = webdriver.Chrome()
driver.get('https://www.messenger.com/')



# Load cookies from the file
with open('cookies.pkl', 'rb') as file:
    cookies = pickle.load(file)
    for cookie in cookies:
        driver.add_cookie(cookie)

# Refresh the page to log in with cookies
driver.refresh()
time.sleep(2)




pin_box = driver.find_element( By.ID , "mw-numeric-code-input-prevent-composer-focus-steal")
pin_box.send_keys(os.getenv("FACEBOOK_PIN"))
while "Enter your PIN to restore your chat history" in driver.page_source:
    time.sleep(5)


# search_box = driver.find_element( By.XPATH, '//input[@placeholder="Search Messenger"]')

search_box = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Search Messenger"]'))
)

search_box.send_keys(recipient.split()[0])
search_box.send_keys(Keys.RETURN)
search_box.send_keys(Keys.RETURN)

# time.sleep(5)

# select_user = driver.find_element(By.XPATH, f'//ul//li[@role="option"]//span[contains(text(), "Rakesh Karmaker")]')

select_user = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, f'//ul//li[@role="option"]//span[contains(text(), "Rakesh Karmaker")]'))
)
select_user.click()
time.sleep(2)

# Send the message
message_box = driver.find_element( By.XPATH, '//div[@aria-label="Message"]')
message_box.send_keys(message)
message_box.send_keys(Keys.RETURN)

# Close the browser
time.sleep(5)
driver.quit()   