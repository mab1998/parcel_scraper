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


import time

import requests
import random
import base64
import numpy as np 


Parcels_input=np.loadtxt('./input_parcel.csv',delimiter="\n",dtype=str)



i=3240
i=3761
i=9653
i=10887
i=11659
len_parcel=len(Parcels_input) 


while i<len_parcel:
    try:
            parcel=Parcels_input[i]

            r = open("cookies", "r")
            cs=r.read()
            cookies = json.loads(cs)
            
            
            
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

        print(i,' ',e)
        i=i


        



