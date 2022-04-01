from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager



def get_last_rec():
    lastUsers = []
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    driver.get("http://web.whatsapp.com")
    source = driver.page_source
    
    #driver.quit() 

