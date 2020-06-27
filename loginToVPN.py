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

driver = webdriver.Opera(executable_path=r'/path/to/operadriver')
driver.get('https://whatismyipaddress.com')
sleep(10)
driver.quit() 



from selenium import webdriver
from time import sleep

# The profile where I enabled the VPN previously using the GUI.
options = webdriver.ChromeOptions()
options.add_argument("--user-data-dir=chrome-data/")

driver = webdriver.Opera(executable_path='operadriver.exe',options=options)
driver.get('https://whatismyipaddress.com')
sleep(10)
driver.quit()


from selenium.webdriver.chrome.options import Options

from selenium import webdriver

options = Options()
options.add_argument("--user-data-dir=chrome-data/")

pluginfile = 'HMA-VPN-Proxy-Unblocker.zip'
options.add_extension(pluginfile)
driver = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=options)
driver.get('https://my.hidemyass.com/?utm_medium=prg_link&utm_source=extension_chrome&utm_campaign=hma_mvp#login')

