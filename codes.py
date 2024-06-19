from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize WebDriver
driver = webdriver.Chrome()

# Open WhatsApp Web
driver.get('https://web.whatsapp.com')

# Allow time to scan the QR code
print("You have 15 seconds to scan the QR code...")
time.sleep(15)

# Open the group chat
chat_name = "chat name"  # name of the person or group
search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
search_box.click()
search_box.send_keys(chat_name)
search_box.send_keys(Keys.ENTER)

# Specify messages to send
messages = ["text" for i in range(1, 101)]  # generates messages from 1 to 100

# Sending messages
for message in messages:
    message_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
    message_box.send_keys(message)
    message_box.send_keys(Keys.ENTER)

print("100 messages sent successfully!")

time.sleep(5)
driver.quit()
