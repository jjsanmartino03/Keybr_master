from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


def get_letters(my_driver):
    final = ""
    to_fill = my_driver.find_elements_by_class_name("TextInput-item")
    for i in to_fill:
        final += i.text
    return final.replace("␣", " ")


driver = webdriver.Chrome()
driver.get("https://www.keybr.com/")

try:
    tour_close = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "Tour-close"))
    )
    tour_close.click()
except:
    pass

activate = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.CLASS_NAME, "TextInput"))
)
activate.click()

to_write = driver.find_element_by_xpath("//input")

for i in range(10):
    for i in get_letters(driver):
        to_write.send_keys(i)
    sleep(3)

driver.close()

