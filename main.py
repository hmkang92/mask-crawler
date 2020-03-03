#author : Kang Hyeong Min
#date : 03/03/2020

import os
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from bs4 import BeautifulSoup
import pyperclip

path = os.path.join((os.path.dirname(os.path.realpath(__file__)) ), "chromedriver_win32", "chromedriver.exe")  # webdriver's path

naver_login_url = 'https://nid.naver.com/nidlogin.login'
mask_url = 'https://smartstore.naver.com/soommask/products/4828127993'

dummy_test = 'https://smartstore.naver.com/jjungdaeshop/products/4487102544'

self_id = "" # your naver id
self_pw = "" # your naver password

options = webdriver.ChromeOptions()
#options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")

def copy_input(instance_of_path, input):
    pyperclip.copy(input)
    instance_of_path.click()
    ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
    time.sleep(1)

def naver_login(get_id, get_pw):
    driver.get(naver_login_url)
    #print(driver.window_handles)
        
    id_form = driver.find_element_by_id("id")
    #id_form.clear()
    copy_input(id_form, get_id)
    #id_form.send_keys(get_id)

    pw_form = driver.find_element_by_id("pw")
    #pw_form.clear()
    #pw_form.send_keys(get_pw)
    copy_input(pw_form, get_pw)

    login_button_xpath = """//*[@id="frmNIDLogin"]/fieldset/input"""
    driver.find_element_by_xpath(login_button_xpath).click()
    driver.implicitly_wait(60) # seconds

    """
    html = driver.page_source
    soup = BeautifulSoup(html)
    naver_user_name = soup.find('strong', {'id':'user_name'})
    """

def buying_mask():
    driver.get(mask_url)
    #driver.get(dummy_test)

    buy_button = driver.find_element_by_xpath("//span[@class='buy']")

    try:
        buy_button = driver.find_element_by_xpath("//span[@class='buy']")
        print(buy_button)
        html = driver.page_source
        soup = BeautifulSoup(html)
        
        bool_buy_button = soup.find_all('span', {'class':'buy'})
        for i_b in bool_buy_button:

            if "stopDefault" in str(i_b): # sold out
                driver.quit()
            else:
                buy_button.click()
                input("find it")
                
    except Exception as error:
        print(error)
        driver.quit()

    driver.quit()

while(1):
    driver = webdriver.Chrome(path, chrome_options=options)
    naver_login(self_id, self_pw)
    time.sleep(2)
    buying_mask()
    driver.quit()

#driver.switch_to.window(driver.window_handles[-1])
#driver.switch_to.window(driver.window_handles[0])

#driver.get_screenshot_as_file('capture.png')

