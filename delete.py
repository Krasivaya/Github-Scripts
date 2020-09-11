import sys
from selenium import webdriver

browser = webdriver.Chrome(executable_path='/chromedriver')
browser.get('https://github.com/login')

def delete():
    folder = sys.argv[1]
    user = browser.find_element_by_xpath('//*[@id="login_field"]')
    user.send_keys('Github_Username')
    pwd = browser.find_element_by_xpath('//*[@id="password"]')
    pwd.send_keys('Github_Password')
    click = browser.find_element_by_xpath('//*[@id="login"]/form/div[4]/input[9]')
    click.click()
    browser.get('https://github.com/Github_Username/'+ folder +'/settings')
    del_btn = browser.find_element_by_xpath('//*[@id="options_bucket"]/div[10]/ul/li[4]/details/summary')
    del_btn.click()
    repo = browser.find_element_by_xpath('//*[@id="options_bucket"]/div[10]/ul/li[4]/details/details-dialog/div[3]/form/p/input')
    repo.send_keys('Github_Username/'+folder)
    repo = browser.find_element_by_xpath('//*[@id="options_bucket"]/div[10]/ul/li[4]/details/details-dialog/div[3]/form/button')
    repo.click()
    browser.close()
    
delete()