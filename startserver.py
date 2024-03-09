from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import random
from selenium.webdriver import Chrome
def serverstarterbot():
    # opt = EdgeOptions().add_argument(r"--headless")
    opt = ChromeOptions()
    opt.add_argument('--incognito') # Extention to solve captchas
    opt.add_experimental_option('excludeSwitches', ['enable-automation']) #Remove "chrome is controlled by automated testsoftware"
    opt.add_argument('window-size=1146,671') # Change window size
    opt.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36') # Add useragent
    driver = webdriver.Chrome(options=opt)
    driver.get('https://aternos.org/go/')
    username = driver.find_element(By.XPATH, "//input[@placeholder='Username']")
    password = driver.find_element(By.XPATH, "//input[@placeholder='••••••••']")
    user = 'StarterBot'
    passw = 'BotAccount'
    for char in user:
        username.send_keys(char)
        time.sleep(random.uniform(0, 1))
    for char in passw:
        password.send_keys(char)
        time.sleep(random.uniform(0, 1)) 
    button = driver.find_element(By.XPATH, "//button[@title='Login']")
    button.click()
    enterservercommandbutton = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/main[1]/div[1]/div[2]/section[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]")))
    action = webdriver.ActionChains(driver)
    action.move_to_element(enterservercommandbutton)
    time.sleep(random.uniform(0, 2))
    action.click()
if __name__ == '__main__':
    serverstarterbot()