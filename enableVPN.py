# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 22:47:21 2020

@author: ambs
"""
from selenium import webdriver
from selenium.webdriver.opera.options import Options
from time import sleep
options = webdriver.ChromeOptions()
options.add_argument("--user-data-dir=chrome-data/")
driver = webdriver.Opera(executable_path='operadriver.exe',options=options)

driver.get('https://whatismyipaddress.com')


