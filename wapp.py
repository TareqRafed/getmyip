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
    try:
        myElem = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'landing-title')))
        if myElem:
            print("Please sign in using your phone")
            isLoggedIn = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.ID, 'pane-side')))
            if isLoggedIn:
                contacts = driver.find_elements_by_class_name("zoWT4")
                last_rec = []
                for con in contacts:
                    span = con.find_element(by=By.TAG_NAME, value="span").text
                    last_rec.append(span)
                return last_rec

        else:
            print("ERROR")
    except TimeoutException:
        print("Loading took too much time!")
    #driver.quit() 

