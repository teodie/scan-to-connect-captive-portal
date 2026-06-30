import os
import time
import secrets
import string
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def generate_password():
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(12))
    return password

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--disable-dev-shm-usage")

service = Service('/usr/bin/chromedriver')
driver = webdriver.Chrome(service=service, options=chrome_options)

password = generate_password()
print(password)

wait = WebDriverWait(driver, 15)

try:
    driver.get("http://192.168.0.1/login.html")
    driver.implicitly_wait(1)

    tenda_web_password_box = wait.until(EC.presence_of_element_located((By.ID,"login-password")))
    tenda_web_submit_button = driver.find_element(by=By.ID, value="save")

    tenda_web_password_box.send_keys("dashboard_pass_here")
    tenda_web_submit_button.click()

    dashboard_wireless_tab = wait.until(EC.presence_of_element_located((By.ID, "wireless")))
    dashboard_wireless_tab.click()
    
    password_box = wait.until(EC.presence_of_element_located((By.ID, "wifiPwd")))
    password_box.clear()
    password_box.send_keys(password)

    driver.implicitly_wait(2)

    save_button = driver.find_element(by=By.ID, value="submit")
    save_button.click()

    driver.implicitly_wait(3)

    alert = wait.until(EC.alert_is_present())

    print(f"Captured alert: {alert.text}")
    alert.accept()    
    
    time.sleep(5)

except Exception as e:
    print(f"Errot: something went wrong: {e}")
    
finally:    
    driver.quit()
