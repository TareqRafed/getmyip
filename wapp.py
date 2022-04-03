from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


def get_last_rec():
    lastUsers = []
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    driver.get("http://web.whatsapp.com")
    delay = 3 # seconds
    try:
        myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'landing-title')))
        if myElem:
            print("Please sign in using your phone")
        else:
            print("signed in")
    except TimeoutException:
        print("Loading took too much time!")
    #driver.quit() 

