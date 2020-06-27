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
import base64


def find_by_xpath(locator):
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, locator))
        )

        return element
def find_by_id(locator):
        element = WebDriverWait(driver, 30).until(
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
   
 

def get_info_parcels(driver,parcel,DataFrame,i):
        
                 
        # find_by_id("txtData").click()
        # find_by_id("txtData").clear()
        # find_by_id("txtData").send_keys(parcel)
        # find_by_id("btnSearch").click()
        find_by_id("btnLgcyTaxes").click()

                              
        Parcel=find_by_xpath('/html/body/div[1]/div[3]/div[2]/div/div/div[4]/div[1]/div[1]/div/div[6]/div[2]').text
        print('Processing Parcel={}    ....{}/{} :'.format(Parcel,i,len_parcel,))
        Tax_Name=find_by_xpath('/html/body/div[1]/div[3]/div[2]/div/div/div[4]/div[1]/div[1]/div/div[1]/div[2]').text
        Tax_Mailing_Address=find_by_xpath('/html/body/div[1]/div[3]/div[2]/div/div/div[4]/div[1]/div[1]/div/div[3]/div[2]').text
        Tax_Address=Tax_Mailing_Address
        
        Tax_Address=Tax_Mailing_Address.split(',')
        try:
                Tax_City=Tax_Mailing_Address.split(',')[-2].split(' ')[-1]

                #Tax_City=find_by_xpath('/html/body/div[1]/div[3]/div[2]/div/div/div[4]/div[1]/div[1]/div/div[7]/div[2]').text
                Tax_State=Tax_Mailing_Address.split(',')[-1].split(' ')[1]
                Tax_Zip_Code=Tax_Mailing_Address.split(',')[-1].split(' ')[2]
        except:
                Tax_City=Tax_Mailing_Address

                #Tax_City=find_by_xpath('/html/body/div[1]/div[3]/div[2]/div/div/div[4]/div[1]/div[1]/div/div[7]/div[2]').text
                Tax_State=Tax_Mailing_Address
                Tax_Zip_Code=''              
        Tax_Address=Tax_Mailing_Address.split(',')[:-1]
        Tax_Address=' '.join(Tax_Address)
      
        Property_Address=find_by_xpath('/html/body/div[1]/div[3]/div[2]/div/div/div[4]/div[1]/div[1]/div/div[2]/div[2]').text

        PropertyAddress=Property_Address.split(',')
        try :
                PropertyCity=Property_Address.split(',')[0].split(' ')[-1]
                PropertyState=Property_Address.split(',')[1].split(' ')[0]
                PropertyPostalCode=Property_Address.split(',')[1].split(' ')[1]
        except:
                 PropertyCity=Property_Address
                 PropertyState=Property_Address
                 PropertyPostalCode=''
        
        PropertyAddress=Property_Address.split(',')[:-1]
        PropertyAddress=' '.join(PropertyAddress)
        
        Occupancy_Class=find_by_xpath('/html/body/div[1]/div[3]/div[2]/div/div/div[4]/div[1]/div[1]/div/div[5]/div[2]').text
        
        

        
        'row rowpadding'
        soup = BeautifulSoup(driver.page_source,"lxml")
        soup_table=soup.find("table", {"class": "ChargeAndPaymentDetailTable"})
        tr=soup_table.findAll('tr')
        data=tr[len(tr)-1].findAll("td")
        Charges_Tax_Bill=data[2].text
        Payment=data[3].text
        Balunce_Due=data[4].text
        
        
        Bedrooms=''
        Living_Area_Total=''
        Age=''   
        driver.find_element_by_id("btnBuildingInfo").click()
        soup = BeautifulSoup(driver.page_source,"lxml")
        soup_table=soup.findAll("div", {"class": "row rowpadding"})
        for ss in soup_table:
            sss=ss.find_all("div", {"class": "generalInfoLabel"})
            vvv=ss.find_all("div", {"class": "generalInfoValue"})

            i=0
            for ssss in sss:
                carc=ssss.text
#                print(ssss.text)
                if (carc=='Age' or carc=='Date Build'):
#                    print(vvv[i].text)
                    Age=vvv[i].text
                    
                if (carc=='Bedrooms'):
#                    print(vvv[i].text)
                    Bedrooms=vvv[i].text
                    
                if (carc=="Living Area Total"):
#                    print(vvv[i].text)
                    Living_Area_Total=vvv[i].text
                    
                    
                i=i+1
        for ss in soup_table:
            sss=ss.find_all("div", {"class": "generalInfoLabelGreen"})
            vvv=ss.find_all("div", {"class": "generalInfoValueGreen"})

            i=0
            for ssss in sss:
                carc=ssss.text
#                print(ssss.text)
                if (carc=='Age' or carc=='Date Build'):
#                    print(vvv[i].text)
                    Age=vvv[i].text
                    
                if (carc=="Number of Units" or carc=='Rooms'):
#                    print(vvv[i].text)
                    Bedrooms=vvv[i].text
                    
                if (carc=="Living Area Total"):
#                    print(vvv[i].text)
                    Living_Area_Total=vvv[i].text
                    
                    
                i=i+1
#            break
              
        row = [Parcel,Tax_Name	,Tax_Address,	Tax_City,Tax_State,Tax_Zip_Code,PropertyAddress,PropertyCity,PropertyState,	PropertyPostalCode	,Occupancy_Class, Bedrooms, Living_Area_Total,Age,Charges_Tax_Bill,Payment,Balunce_Due]	
#        print(row)
        DataFrame = DataFrame.append(pd.DataFrame(pd.DataFrame(np.array(row).reshape(1,17), columns=columnlist)),ignore_index=True)
#        row = pd.Series({'Parcel #':Parcel,	'Tax Name(Primary Owner)':Tax_Name	,'Tax Address':Tax_Address,	'Tax City':Tax_City,
#         'Tax State':Tax_State,'Tax Zip Code':Tax_Zip_Code,'PropertyAddress':PropertyAddress, 'PropertyCity':PropertyCity,
#        'PropertyState':PropertyState,	'PropertyPostalCode':PropertyPostalCode	,'Occupancy Class':Occupancy_Class, 
#        'Bedrooms':Bedrooms, 'Living Area Total':Living_Area_Total,'Age':Age,	'Charges (Tax Bill)':Charges_Tax_Bill,
#        'Payment':Payment,'Balunce Due':Balunce_Due}	,name=3)
#        print('The new data frame is: \n{}'.format(row))
#
##        pd.concat([DataFrame,row], axis=0, join='outer', join_axes=None, ignore_index=False,
##                  keys=None, levels=None, names=None, verify_integrity=False,
##                  copy=True)    
#        DataFrame = DataFrame.append(row,ignore_index=True)
        writer = pd.ExcelWriter('Tax Delinquent 2016.xlsx')
        DataFrame.to_excel(writer,'Sheet1')
        writer.save()

        return    DataFrame

def get_url(parcel):
    btn = base64.b64encode(parcel.encode()).decode()
    url=""
    txtData=base64.b64encode("782-17-109".encode()).decode()
    ddlCity=base64.b64encode("99".encode()).decode()
    rdoSearch=base64.b64encode("Parcel".encode()).decode()
    
    url="https://myplace.cuyahogacounty.us/"+txtData+"?"+"city="+ddlCity+"&searchBy="+rdoSearch
    url=url+"&" + "dataRequested="+btn
    
    return url

def post_url_tax():
    url="https://myplace.cuyahogacounty.us/MainPage/LegacyTaxes"
    


print('Data Processing............')




columnlist=['Parcel # ','Tax Name(Primary Owner)', 'Tax Address', 'Tax City',
 'Tax State', 'Tax Zip Code', 'PropertyAddress', 'PropertyCity', 'PropertyState', 
 'PropertyPostalCode', 'Occupancy Class', 'Bedrooms', 'Living Area Total', 'Age', 
 'Charges (Tax Bill)', 'Payment', 'Balunce Due']

Parcels_input=np.loadtxt('./input_parcel.csv',delimiter="\n",dtype=str)
DataFrame=pd.DataFrame()
#DataFrame = pd.read_excel("./Tax Delinquent 2016.xlsx", sheetname=0)

i=3240
i=3761
#        writer.writerow(header)

len_parcel=len(Parcels_input) 
driver=get_proxy_driver()

import requests
import json

parcel=Parcels_input[i]
url=get_url(parcel)
driver.get(url)

while i<len_parcel:
    try:

            # try:
            #     driver.quit()
            # except:
            #     pass
   
            # driver=get_proxy_driver()

            
            # driver.get("http://myplace.cuyahogacounty.us/")
            parcel=Parcels_input[i]
            # url=get_url(parcel)
            # driver.get(url)
            # driver.current_url
            
            
            # find_by_id("Parcel").click()
            # stat=True            
    #		driver=get_proxy_driver(useproxy, proxy)
    #		driver.get("http://myplace.cuyahogacounty.us/")	
            cookies=driver.get_cookies()
            f = open("cookies", "w")
            f.write(json.dumps(cookies))
            f.close()
            
            # r = open("cookies", "r")
            # cs=r.read()
            # d = json.loads(cs)
            # cs= cs.replace("[","").replace("]","")
            
            
            
            s = requests.Session()
            for cookie in cookies:
                s.cookies.set(cookie['name'], cookie['value'])
                
            url = "https://myplace.cuyahogacounty.us/MainPage/LegacyTaxes"

            payload = 'hdnTaxesParcelId='+str(parcel.replace("-",""))+'&hdnTaxesListId=&hdnTaxesButtonClicked=Tax+Bill&hdnTaxesSearchChoice=Parcel&hdnTaxesSearchText='+str(parcel)+'&hdnTaxesSearchCity=99&hdnTaxYear=2019'
            headers = {
              'Content-Type': 'application/x-www-form-urlencoded'
            }
            
            response = s.request("POST", url, headers=headers, data = payload)
            
            print("========================"+str(i))
            
            path="./txt/demo"+str(i)+".html"
            f = open(path, "w")
            f.write(str(response.text.encode('utf8')))
            f.close()
            
            
            parcel=Parcels_input[i]
            # DataFrame=get_info_parcels(driver,parcel,DataFrame,i)
            i=i+1
    except Exception as e:
        try:
                driver.quit()
        except:
                pass
   
        driver=get_proxy_driver()
        print(i,' ',e)
        i=i

        

#            try :

#        break
#            except:
        



