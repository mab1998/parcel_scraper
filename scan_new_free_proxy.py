# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 12:01:05 2018

@author: ambs
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 15:55:22 2018

@author: ambs
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 22:22:23 2018
@author: ambs
"""
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup
import requests

def test_proxy(proxy):
	proxies = {
              "http": "{}".format(proxy),
              "https": "{}".format(proxy),
            }
	try:
		response =requests.get("http://hcad.org/", proxies=proxies, timeout=1.0)

#		sock.connect(('www.google.com', 80))
		if response.status_code==200:

                       print('GOOD | ' + str(response.status_code)+' |'+proxy)
                       stat=True
		else:        
                  print('BAD | ' + str(response.status_code)+' |'+proxy)
                  stat=False
           
	except:
		print('BAD  | '+proxy)
		stat=False
	return stat

def create_proxy(country=None):

#            options = Options()
##           options.add_argument('--headless')
##           options.add_argument('--disable-gpu')  # Last I checked this was necessary.
#            driver = webdriver.Chrome(executable_path='./Driver/chromedriver.exe', chrome_options=options)
#            driver.get('http://freeproxylists.net')
            i = 0
            urls = [
              'https://www.us-proxy.org/',
              'https://free-proxy-list.net/uk-proxy.html',
              'https://free-proxy-list.net/',
              'https://www.socks-proxy.net/',
              'https://www.sslproxies.org/',
              'https://free-proxy-list.net/anonymous-proxy.html',
            ]
            #scraping links from urls
            f = open('proxies.txt', 'a')
            for x in range(len(urls)):
                try:
                    res = requests.get(urls[x] , headers={'User-Agent':'Mozilla/5.0'}) #fetching urls and setting user-agent
                except Exception as e:
                    print(e)
                    continue
                
                soup = BeautifulSoup(res.text,"lxml")
                for items in soup.select("tbody tr")[:-8]:  #mark -8 removes the broken lines from scrape
                    proxy_list = ':'.join([item.text for item in items.select("td")[:2]])  # grabing and joining the first 2 rows
#                    print(proxy_list)
                    if test_proxy(proxy_list):
                         #writing to a file , not the final output due to empty lines
                        f.write(proxy_list+'\n')

                
def create_proxy_txt(country=None):

        options = Options()
#        options.add_argument('--headless')
#        options.add_argument('--disable-gpu')  # Last I checked this was necessary.
        driver = webdriver.Chrome(executable_path='./Driver/chromedriver.exe', chrome_options=options)
        driver.get('http://freeproxylists.net')

        driver.find_element_by_link_text("English").click()
        with open('proxies.txt','w') as outfile:
            time.sleep(5)
            filter_p = driver.find_element_by_id('form1')
            
            countryOp = Select(filter_p.find_element_by_name('c'))
            countryOp.select_by_visible_text('United States')
            
            '''
            protocolOp = filter_p.find_elements_by_xpath("//input[@name='a[]']")
            for protocol_op in protocolOp:
                if protocol_op.get_attribute('value') != '2':
                    protocol_op.click()
            '''
            
            uptimeOp = Select(filter_p.find_element_by_name('u'))
            uptimeOp.select_by_value('90')
            
            filter_p.find_element_by_xpath("//input[@type = 'submit']").click()
            time.sleep(2)
            
            while 1:
                body = WebDriverWait(driver,10).until(lambda driver : driver.find_element_by_class_name('DataGrid'))
                for tag in body.find_elements_by_tag_name('tr')[1:]:
                    rows = tag.find_elements_by_tag_name('td')
                    if rows[0].text:
                        response = int(rows[8].find_element_by_tag_name('span').get_attribute('style').split(';')[0].split(':')[1].split('%')[0])
                        transfer = int(rows[9].find_element_by_tag_name('span').get_attribute('style').split(';')[0].split(':')[1].split('%')[0])
                        ip = rows[0].text
                        port = rows[1].text
                        proxy=ip+':'+port
                        if (response+transfer)>100:
                            if test_proxy(proxy):
                                outfile.writelines(proxy+ '\n')
                try:
                    next_page = WebDriverWait(driver,10).until(lambda driver : driver.find_element_by_partial_link_text('Next'))
                    next_page.click()
                except Exception as e:
                    print('1146=',e)
                    break
        driver.quit()    
            

def find_by_xpath(locator):
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, locator))
        )

        return element
def find_by_id(locator):
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, locator))
        )

        return element   
    
    
def find_by_css(locator):
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR , locator))
        )

        return element
def find_by_class(locator):
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME , locator))
        )

        return element   
    

#create_proxy_txt()
create_proxy()


