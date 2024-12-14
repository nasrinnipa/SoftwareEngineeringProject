import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

def test():
    # Open the URL
    driver.get("http://127.0.0.1:8000/")
    
    # Wait for 3 seconds after loading the page
    time.sleep(3)
    
    # Wait until the Sign In link is visible and click it
    sign_in_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Sign In"))
    )
    sign_in_link.click()

    # Wait for the login form to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )

    # Enter the username and password
    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")

    
    username_field.clear()
    password_field.clear()

    username_field.send_keys("buyer")
    time.sleep(1)
    password_field.send_keys("buyer")

    # Click the login button
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()

    driver.get("http://127.0.0.1:8000/market")
    time.sleep(4)

    driver.get("http://127.0.0.1:8000/market/product-details/13")
    time.sleep(2)
    driver.get("http://127.0.0.1:8000/logout")
    time.sleep(5)


     # Wait for the login form to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )

    # Enter the username and password
    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")

    # wrong pass word 
    
    username_field.clear()
    password_field.clear()

    username_field.send_keys("seller")
    time.sleep(1)
    password_field.send_keys("buyer")

    # Click the login button
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()

    time.sleep(4)

     # Wait for the login form to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )

    # Enter the username and password
    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")

    username_field.clear()
    password_field.clear()

    username_field.send_keys("seller")
    time.sleep(1)
    password_field.send_keys("seller")

    time.sleep(2)
    
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()


    driver.get("http://127.0.0.1:8000/product/")
    time.sleep(4)

    driver.get("http://127.0.0.1:8000/product/13/")
    time.sleep(2)
    driver.get("http://127.0.0.1:8000/product/")
    time.sleep(5)

    driver.get("http://127.0.0.1:8000/logout/")
    time.sleep(3)

    driver.quit()

test()
