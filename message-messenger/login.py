from selenium import webdriver
import pickle
import time
import os

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open Facebook Messenger
driver.get('https://www.messenger.com/')

# Log in manually and complete 2FA
print("Please log in and complete 2FA manually.")
time.sleep(60)  # Wait for 60 seconds to complete login

# Save cookies to a file
with open('cookies.pkl', 'wb') as file:
    pickle.dump(driver.get_cookies(), file)

driver.quit()

os.system("start message-messenger.py")