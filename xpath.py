from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
wait = WebDriverWait(driver, 10)

FindinGXpath = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@placeholder="Hide/Show Example"]')))
FindinGXpath.send_keys("Hello World!!")

time.sleep(3)
driver.quit()