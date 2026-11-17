from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

driver.get("https://authorized-partner.vercel.app/")
login = driver.find_element(By.CSS_SELECTOR,"a[href='/login']")
login.click()
input("Press Enter to close the browser")
driver.quit()