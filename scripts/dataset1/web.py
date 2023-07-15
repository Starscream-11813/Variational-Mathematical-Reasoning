
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://www.quillbot.com")
driver.save_screenshot("ss1.png")

xpath_input_clear = '/html/body/div[1]/div[2]/div[3]/div[1]/div/div/div[1]/div/div/div/div/div/div[1]/div[2]/div[2]/div/div[1]/div/div/div[1]/div/div'
xpath_input_field = '//*[@id="inputText"]'
xpath_submit_button = '/html/body/div[1]/div[2]/div[3]/div[1]/div/div/div[1]/div/div/div/div/div/div[1]/div[2]/div[2]/div/div[1]/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div/button'

# driver.find_element('xpath', xpath_input_clear).click()
# input_field = driver.find_element('xpath', xpath_input_field)
# input_field.clear()
# input_field.send_keys("abcdefg")
# sleep(0.2)
# driver.find_element('xpath', xpath_submit_button).click()

