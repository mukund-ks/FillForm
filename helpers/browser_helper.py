import os
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
# from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

sys.path.append(".")

element_class = "form-control"
submit_element_xpath = '//*[@id="registerBtn"]'
url = "https://training.ethnus.com/meeting/register?uId=304838000001516349"

# driver = webdriver.Chrome(executable_path='./chromedriver') # for chrome

# options = Options()
# options.binary_location = rf"{os.getenv('BROWSER_PATH')}"

# firefox_binary = FirefoxBinary(rf"{os.getenv('BROWSER_PATH')}")

service = Service(rf"{os.getenv('EXECUTABLE_PATH')}")

driver = webdriver.Firefox(service=service)


def get_keys(df) -> webdriver.Firefox:
    print('get keys')
    first_name = df["first_name"][0]
    last_name = df["last_name"][0]
    email = df["email"][0]

    fill = [first_name, last_name, email]
    field = driver.find_elements(By.CLASS_NAME, element_class)

    for a, q in zip(fill, field):
        q.send_keys(a)

    return driver


def submit_form() -> webdriver.Firefox:
    driver.find_element(By.XPATH, submit_element_xpath).click()
    return driver
