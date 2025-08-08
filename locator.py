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

'''using id'''
# element1 = wait.until(EC.element_to_be_clickable((By.ID, "autocomplete")))
# element1.click()

'''using name'''
# element1 = wait.until(EC.element_to_be_clickable((By.NAME, "dropdown-class-example")))
# element1.click()

# element2 = wait.until(EC.element_to_be_clickable((By.XPATH, "//option[@value='option2']")))
# element2.click()

'''using class ---> CLASS Locator only work for single class, By.CLASS_NAME only supports one single class (no spaces)'''
# OpenTab = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn-style")))

'''using css locator ----> Css locator can be used for multi line class, with using . operator afer every word'''
# OpenTab = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-style.class1.class2")))
# OpenTab.click()

'''using link'''
# UsingLinkOpeningTab = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Free Access to InterviewQues/ResumeAssistance/Material")))
# UsingLinkOpeningTab.click()

'''using partial link'''
# UsingPartialLinkOpeningTab = wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "InterviewQues/ResumeAssistance")))
# UsingPartialLinkOpeningTab.click()

'''using tag'''
# UsingTag = wait.until(EC.element_to_be_clickable((By.TAG_NAME, "button")))
# UsingTag.click()


time.sleep(3)
driver.quit()

