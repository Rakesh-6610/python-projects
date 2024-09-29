from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pickle
import time
import os
from dotenv import load_dotenv
import pyperclip


load_dotenv()


def main():

    #Get recipient and messages
    messages_list = get_recipient_and_messages()

    #Check if the user has a secure storage PIN
    has_pin = True if (input("Do you have a secure storage PIN? (y/n): ").lower() == "y") else False 

    #Open chrome
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


    #use this if user has secure storage PIN
    if has_pin:
        cancel_pin(driver)
    
    #send message to each recipient
    for recipient, messages in messages_list.items():
        #select user
        has_selected = select_user(driver, recipient)
        if not has_selected:
            raise SystemError("Inserted username couldn't be found")

        # Send the message
        for message in messages:
            pyperclip.copy(message)
            message_box = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//div[@aria-label="Message"]'))
            )
            message_box.click()
            message_box.send_keys(Keys.CONTROL + 'v')
            message_box.send_keys(Keys.RETURN)

    # Close the browser
    time.sleep(5)
    driver.quit()   


def select_user(driver, name):
        loop_count = 0
        while True:
            search_box = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Search Messenger"]'))
            )

            search_box.send_keys((" ").join(name.split()[:-1]))
            search_box.send_keys(Keys.RETURN)
            search_box.send_keys(Keys.RETURN)

            time.sleep(1)
            selected_user = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, f'//ul//li[@role="option"]//span[contains(text(), "{name}")]'))
            )
            time.sleep(1)
            selected_user.click()
            time.sleep(3)

            try:
                user_heading = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, f'//h2[@dir="auto"]//span[@dir="auto"]//span[contains(text(), "{name}")]'))
                )
                return True
            except:
                select_user(driver, name)
            finally:
                if loop_count > 10:
                    return False
                loop_count += 1




def cancel_pin(driver):
    cancel_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//div[@aria-label="Close"]'))
    )
    cancel_box.click()
    dont_restore = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//div[@aria-label="Don\'t restore messages"]'))
    )
    dont_restore.click()

def get_recipient_and_messages():
    print("Please enter the recipient name and messages sent to him. If not press 'enter'")
    people_message = {}
    while True:
        recipient = input("Enter recipient (Full Name): ").title().strip()
        if recipient == "":
            break
        messages = []
        while True:
            message = input("Enter message: ").strip()
            if message == "":
                break
            messages.append(message)
        people_message[recipient] = messages
    return people_message



if __name__ == '__main__':
    if "message-messenger" not in os.getcwd():
        raise ValueError("This script must be run in the 'message-messenger' folder")
    else:
        if not os.path.exists('cookies.pkl'):
            os.system("start login.py")
        else:
            main()


