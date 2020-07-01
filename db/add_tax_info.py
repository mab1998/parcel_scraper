from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from create import Data
import numpy as np 
from bs4 import BeautifulSoup
import os
import lxml.html as lh
import json
import re
# Parcels_input=np.loadtxt('./input_parcel.csv',delimiter="\n",dtype=str)


engine = create_engine('sqlite:///parcel.db', echo=True)

Session = sessionmaker(bind = engine)
session = Session()

files = os.listdir('./txt')
i=1

err=[]
for file in files:
    print("==============",i)
    i=i+1
    doc=lh.parse("./txt/"+str(file))
    try:
        parcel_id=doc.xpath("/html/body/div[1]/div[3]/div[2]/div/div/div[4]/div[1]/div[1]/div/div[6]/div[2]")[0].text
    except Exception as e:
        print("++++++++++++++++++++++++++++++++++",file,"+++",e)
        err.append(file)
        continue
    result = session.query(Data).filter(Data.Parcel_id==parcel_id).first()


    result.Tax_Name=doc.xpath('/html/body/div[1]/div[3]/div[2]/div/div/div[4]/div[1]/div[1]/div/div[1]/div[2]')[0].text
    result.Tax_Mailing_Address=doc.xpath('/html/body/div[1]/div[3]/div[2]/div/div/div[4]/div[1]/div[1]/div/div[3]/div[2]')[0].text
    result.Tax_Address=result.Tax_Mailing_Address
    result.Tax_Address=result.Tax_Mailing_Address.split(',')

    try:
            result.Tax_City=result.Tax_Mailing_Address.split(',')[-2].split(' ')[-1]
            result.Tax_State=result.Tax_Mailing_Address.split(',')[-1].split(' ')[1]
            result.Tax_Zip_Code=result.Tax_Mailing_Address.split(',')[-1].split(' ')[2]
    except:
            result.Tax_City=result.Tax_Mailing_Address
            result.Tax_State=result.Tax_Mailing_Address
            result.Tax_Zip_Code=''              
    result.Tax_Address=result.Tax_Mailing_Address.split(',')[:-1]
    result.Tax_Address=' '.join(result.Tax_Address)

    result.Property_Address=doc.xpath('/html/body/div[1]/div[3]/div[2]/div/div/div[4]/div[1]/div[1]/div/div[2]/div[2]')[0].text


    result.PropertyAddress=result.Property_Address.split(',')
    try :
            result.PropertyCity=result.Property_Address.split(',')[0].split(' ')[-1]
            result.PropertyState=result.Property_Address.split(',')[1].split(' ')[0]
            
            # result.PropertyPostalCode=result.Property_Address.split(',')[1].split(' ')[1]
            result.PropertyPostalCode=re.findall("\d+", result.Property_Address.split(',')[1])[0]
    except:
              result.PropertyCity=result.Property_Address
              result.PropertyState=result.Property_Address
              result.PropertyPostalCode=''

    result.PropertyAddress=result.Property_Address.split(',')[:-1]
    result.PropertyAddress=' '.join(result.PropertyAddress)
    result.Occupancy_Class=doc.xpath('/html/body/div[1]/div[3]/div[2]/div/div/div[4]/div[1]/div[1]/div/div[5]/div[2]')[0].text

    demo = open("./txt/"+str(file), "r")
    html=demo.read()
    demo.close()


    soup = BeautifulSoup(html,"lxml")
    soup_table=soup.find("table", {"class": "ChargeAndPaymentDetailTable"})
    tr=soup_table.findAll('tr')
    data=tr[len(tr)-1].findAll("td")
    result.Charges_Tax_Bill=data[2].text
    result.Payment=data[3].text
    result.Balunce_Due=data[4].text
            
    session.commit()

print(".......................................",len(err))
f = open("err", "w")
f.write(json.dumps(err))
f.close()


# err=[]

# files = os.listdir('./txt_build')
# j=1
# for file in files:


#     print("jj==============",j)
#     j=j+1
#     doc=lh.parse("./txt_build/"+str(file))
#     try:
#         parcel_id=doc.xpath('//*[@id="hdnSearchText"]/@value')[0]
#     except Exception as e:
#         print("++++++++++++++++++++++++++++++++++",file,"+++",e)
#         err.append(file)
#         continue
    
#     # print("oooooooooooooooooooooooooooooooooooooo",parcel_id)
#     result = session.query(Data).filter(Data.Parcel_id==parcel_id).first()
#     # print("oooooooooooooooooooooooooooooooooooooo",result.id)

#     result.Bedrooms=''
#     result.Living_Area_Total=''
#     result.Age=''   


#     build = open("./txt_build/"+str(file), "r")
#     html=build.read()
#     build.close()

    
#     soup = BeautifulSoup(html,"lxml")
#     soup_table=soup.findAll("div", {"class": "row rowpadding"})
#     for ss in soup_table:
#         sss=ss.find_all("div", {"class": "generalInfoLabel"})
#         vvv=ss.find_all("div", {"class": "generalInfoValue"})
    
#         i=0
#         for ssss in sss:
#             carc=ssss.text
#     #                print(ssss.text)
#             if (carc=='Age' or carc=='Date Build'):
#     #                    print(vvv[i].text)
#                 result.Age=vvv[i].text
                
#             if (carc=='Bedrooms'):
#     #                    print(vvv[i].text)
#                 result.Bedrooms=vvv[i].text
                
#             if (carc=="Living Area Total"):
#     #                    print(vvv[i].text)
#                 result.Living_Area_Total=vvv[i].text
                
                
#             i=i+1
#     for ss in soup_table:
#         sss=ss.find_all("div", {"class": "generalInfoLabelGreen"})
#         vvv=ss.find_all("div", {"class": "generalInfoValueGreen"})
    
#         i=0
#         for ssss in sss:
#             carc=ssss.text
#     #                print(ssss.text)
#             if (carc=='Age' or carc=='Date Build'):
#     #                    print(vvv[i].text)
#                 result.Age=vvv[i].text
                
#             if (carc=="Number of Units" or carc=='Rooms'):
#     #                    print(vvv[i].text)
#                 result.Bedrooms=vvv[i].text
                
#             if (carc=="Living Area Total"):
#     #                    print(vvv[i].text)
#                 result.Living_Area_Total=vvv[i].text
                
                
#             i=i+1
#     print("++",result.id,"++",result)
#     # input("123 : ")
            
#     session.commit()
    
# print(".......................................",len(err))
# f = open("err_build", "w")
# f.write(json.dumps(err))
# f.close()


