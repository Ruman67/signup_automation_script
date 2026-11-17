from selenium import webdriver
driver = webdriver.Chrome()

driver.get("https://authorized-partner.vercel.app/")
input("Press Enter to close the browser")
driver.quit()