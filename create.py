import sys
import os
from selenium import webdriver

path = '/home/coder/project/'
browser = webdriver.Chrome(executable_path = '/chromedriver')
browser.get('https://github.com/login')

def create():
    newFolder = str(sys.argv[1])
    try:
        os.makedirs(path + newFolder)
    except:
        print('The folder exists!')
    user = browser.find_element_by_xpath('//*[@id="login_field"]')
    user.send_keys('Github_Username')
    pwd = browser.find_element_by_xpath('//*[@id="password"]')
    pwd.send_keys('Github_Password')
    click = browser.find_element_by_xpath('//*[@id="login"]/form/div[4]/input[9]')
    click.click()
    browser.get('https://github.com/new')
    repo = browser.find_element_by_xpath('//*[@id="repository_name"]')
    repo.send_keys(newFolder)
    send = browser.find_element_by_xpath('//*[@id="new_repository"]/div[4]/button')
    send.submit()
    browser.close()
    
create()