import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

user = input('Please enter your Email: ')
password = input('Please enter your Password: ')

browser = webdriver.Chrome()
browser.get('https://www.buzzsprout.com/')

def log_in():

    time.sleep(5)

    find_log_in = browser.find_element_by_xpath('/html/body/header/nav/div/a[1]').click()
    time.sleep(2)

    find_user = browser.find_element_by_id('user_email').send_keys(user)

    find_pass = browser.find_element_by_id('user_password').send_keys(password)

    find_submit = browser.find_element_by_xpath('/html/body/div/div/fieldset[1]/form/input[5]').click()

    print("Login successful.")

def podcast_title():

    find_title = browser.find_element_by_css_selector('.episode--not_live a').click()
    time.sleep(2)

    find_edit_chapters = browser.find_element_by_xpath('//*[@id="main"]/div[2]/div[2]/div/div/strong/a').click()
    time.sleep(2)

    print("Opened the latest epsiode.")

def open_file():
    src = sys.argv[1]

    with open (src, 'r') as file:

        for line in file:
            line = line.strip()
            space = line.find(' ')
            desc = line[space:]
            timestamp = line[:space]

            print (f"Adding line: {line}")

            if len(timestamp) == 4:
                timestamp = '00:0' + timestamp
            elif len(timestamp) == 5:
                timestamp = '00:' + timestamp
            elif len(timestamp) == 7:
                timestamp = '0' + timestamp

            add_new_chapter = browser.find_element_by_xpath('//*[@id="add_new_chapter"]').click()

            add_title = browser.find_element_by_css_selector('#new_chapter_form #chapter_title')
            time.sleep(2)

            add_title.send_keys(desc)
            time.sleep(1)

            add_timestamp = browser.find_element_by_css_selector('#new_chapter_form #chapter_start_time_string')
            time.sleep(1)

            add_timestamp.click()
            add_timestamp.clear()
            add_timestamp.click()
            add_timestamp.send_keys(timestamp)

            create_chapter = browser.find_element_by_css_selector('#new_chapter_form .btn_create').click()
            time.sleep(2)

    save_update = browser.find_element_by_xpath('//*[@id="publish_chapters"]').click()

log_in()
podcast_title()
open_file()
print ('Upload successful!')
print ('Your chapter markers have been uploaded.')
