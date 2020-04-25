from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep

class BotWebScraping :
    def __init__(self):
        self.driver = webdriver.Chrome('chromedriver')
        self.driver.get(#I omit the website's url to commit on git)
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(text(), 'Tutte le offerte')]").click()
        sleep(2)
        self.driver.find_element_by_xpath("//span[contains(text(), 'Mostra più contenuti')]").click()       
        sleep(2)
        self.driver.execute_script("window.scrollTo(0, 1500)") 
        sleep(1)
        self.driver.find_element_by_xpath("/html/body/div[1]/div[4]/section[3]/div[1]/main/div[1]/div/div[1]/ul/li[77]/a/label").click() 
        sleep(2)  

        wait = WebDriverWait(self.driver, 100)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href*='Smartphone']")))

        for div in self.driver.find_elements_by_css_selector("a[href*='Smartphone']"):
            print(div.text)




BotWebScraping()        