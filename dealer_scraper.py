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
import zipfile
import json
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.proxy import Proxy,ProxyType
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import base64
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
import numpy as np 
import pandas as pd
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import requests
import random

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
    
def get_proxy_driver():
            options = webdriver.ChromeOptions()
            options.add_argument("--user-data-dir=chrome-data/")
            driver = webdriver.Opera(executable_path='operadriver.exe',options=options)
          #♠  driver.set_page_load_timeout(60)
            


            return driver    
 




print('Data Processing............')




columnlist=["num","Dealership_Name","Legal_Name","Registration_Number","HST_Number","Address","City","Province","Postal_Code","Dealership_Type","Phone","Fax"]	  

DataFrame=pd.DataFrame()
#DataFrame = pd.read_excel("./Tax Delinquent 2016.xlsx", sheetname=0)

#        writer.writerow(header)

url='https://wheelsonline.ca/directory.asp?I=Ontario-Car-Dealers-Directory-Directions-ON-Canada&countryID=1&ProvinceID=1&by=name&alpha='

url='https://wheelsonline.ca/directory.asp?I=Ontario-Vehicle-Dealers-Directory-ON-Canada&ProvinceID=1&countryID=1&by=area#dir_top'
alpha=['0-9' ,'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
len_alpha=len(alpha) 
links_area=[]
driver=get_proxy_driver()
i=0
driver.get(url)
elements=driver.find_elements_by_css_selector("div.large-12.small-12.left > a")


for element in elements:
  
    dealer_name=element.get_attribute('href')
    links_area.append(dealer_name)
    
len_area=len(links_area) 
driver=get_proxy_driver()
i=0
links=[]

while i<len_area:
    try:
            try:
                    driver.quit()
            except:
                    pass
            driver=get_proxy_driver()
            
            driver.get(links_area[i])
    
            print('Data Processing............:',i)
                
            if "wheelsonline.ca" in driver.current_url:
                elements=driver.find_elements_by_tag_name('a')
                for element in elements:
                    try:
                        if 'contact_dealer.asp?' in  element.get_attribute('href'):
                            links.append(element.get_attribute('href'))
                    except:
                            pass

                i=i+1

            else:
                try:
                    driver.quit()
                except:
                    pass
                driver=get_proxy_driver()


            #DataFrame=get_info_parcels(driver,DataFrame)
    except Exception as e:
                try:
                    driver.quit()
                except:
                    pass
                driver=get_proxy_driver()
                print(i,' ',e)
                i=i

len(links)     
   
driver=get_proxy_driver()
len_links=len(links)
i=1062
err=0
newlist=[]
for i in range(1062,len_links):
    if i not in listlink:
        newlist.append(i)

    
len_links=len(newlist)  
i=0 
while i< len_links:

    try:
            try:
                    driver.quit()
            except:
                    pass
                
                
            driver=get_proxy_driver()        

        
            link=links[newlist[i]]
            link_=link.replace('-ON&action','&action').replace('contact_dealer.asp','sign_up.asp')+'&dtID=2&pid=ON&src=dlrClm'
            driver.get(link_)
            if "wheelsonline.ca" in driver.current_url:
            # ele=driver.find_element_by_css_selector('body > div.show_on_screen_only > div.row.main_page_container > div > h1').text
            # if ele=="Claim and Manage Your Dealership":
                        elements=driver.find_element_by_css_selector('fieldset.form_platform').find_elements_by_css_selector('div.row div label')
                        print('Data Processing............:',i)

                        for element in elements:
                            text=element.text
                            if 'Dealership Name' in text:
                                Dealership_Name=element.find_element_by_tag_name('input').get_attribute('value')
                            elif 'Legal Name' in text:
                                Legal_Name=element.find_element_by_tag_name('input').get_attribute('value')
                            elif 'Registration Number' in text:
                                Registration_Number=element.find_element_by_tag_name('input').get_attribute('value')
                            elif  'HST Number' in text:
                                HST_Number=element.find_element_by_tag_name('input').get_attribute('value')
                            elif  'Address' in text:
                                Address=element.find_element_by_tag_name('input').get_attribute('value')
                            elif  'City' in text:
                                City=element.find_element_by_tag_name('input').get_attribute('value')
                            elif  'Province' in text:
                                Province=element.find_element_by_tag_name('input').get_attribute('value')
                            elif  'Postal Code' in text:
                                Postal_Code=element.find_element_by_tag_name('input').get_attribute('value')
                            elif  'Dealership Type' in text:
                                Dealership_Type=element.find_element_by_tag_name('input').get_attribute('value')            
                            elif  'Phone' in text:
                                Phone=element.find_element_by_tag_name('input').get_attribute('value')
                            elif  'Fax' in text:
                                Fax=element.find_element_by_tag_name('input').get_attribute('value')
                        row = [newlist[i],Dealership_Name,Legal_Name,Registration_Number,HST_Number,Address,City,Province,Postal_Code,Dealership_Type,Phone,Fax]	
                        DataFrame = DataFrame.append(pd.DataFrame(pd.DataFrame(np.array(row).reshape(1,12), columns=columnlist)),ignore_index=True)
                        i=i+1
            else:
                i=i+1
                try:
                    driver.quit()
                except:
                    pass
                #driver=get_proxy_driver()
                           
    except Exception as e:
                try:
                    driver.quit()
                except:
                    pass
                #driver=get_proxy_driver()
                print(i,' ',e)
writer = pd.ExcelWriter('Dealership list 630.xlsx')
DataFrame.to_excel(writer,'Sheet1')
writer.save()

