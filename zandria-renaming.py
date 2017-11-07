#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# A hash map of posts to rename, in the format URL : New name
rename = {
    "https://poly.google.com/view/0-gJcbrGLJy": "Cactus",
}

# Your Google account credentials
mail_address = ''
password = ''

driver = webdriver.Chrome()

# Go to Google and login
url = 'https://www.google.com/accounts/Login?hl=en&continue=http://www.google.com/'
driver.get(url)

webdriver.ActionChains(driver).move_to_element(driver.find_element_by_id("identifierId")).click().send_keys(
    mail_address).move_to_element(driver.find_element_by_id("identifierNext")).click().perform()

time.sleep(2)

webdriver.ActionChains(driver).move_to_element(driver.find_element_by_name("password")).click(
).send_keys(password).move_to_element(driver.find_element_by_id("passwordNext")).click().perform()

time.sleep(2)

# Go to Poly and start renaming!
for key, value in sorted(rename.iteritems()):
    print(value)
    driver.get(key)

    time.sleep(2)

    # Press edit
    edit = driver.find_element_by_xpath("//div[@jsname='rhPddf']")
    webdriver.ActionChains(driver).move_to_element(edit).click().perform()
    time.sleep(2)

    # Change title
    title = driver.find_element_by_class_name('NEfL5c')
    title.clear()
    title.send_keys(value)

    # Press submit
    submit = driver.find_element_by_xpath("//div[@jsname='YcrmD']")
    webdriver.ActionChains(driver).move_to_element(submit).click().perform()

    # Wait a bit and then continue loop
    time.sleep(2)
