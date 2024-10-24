# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 01:34:16 2023

@author: Rish
"""

import os
import pytesseract
from PIL import Image
from datetime import datetime
import pandas as pd

# Open the image file
path = r"C:\Users\Rish\Documents\Client projects Python\CDM\Order_ID_Extractor\SOURCE\0ac3acad-3882-45c8-ae77-6c788c731846 - KESHAV SHARMA.jpeg"
start = 'ORDER #'
end = 'ORDER TOTAL'

# create an empty dataframe with desired columns
df = pd.DataFrame()
df = pd.DataFrame(columns=["ORDER_ID",'FILENAME', 'SCREENSHOT_TYPE',"RESULT"])
#EMPTY LIST
data = []


source_path = r"C:\Users\Rish\Documents\Client projects Python\CDM\Order_ID_Extractor\SOURCE"
dir = os.listdir(source_path)

s_time = datetime.now()

desktop_ok = ["WRITE A PRODUCT REVIEW","LEAVE SELLER FEEDBACK", "LEAVE DELIVERY FEEDBACK"]
desktop_not_ok =  ["DAMRU"]
mobile_ok = ["DOWNLOAD INVOICE","ORDER DATE","SHIPMENT DETAILS"]
mobile_not_ok = ["KAKA"]


for file in dir:
    order_id = '-'
    #file
    path = os.path.join(source_path,file)
    image = Image.open(path)
    text = pytesseract.image_to_string(image)
    text = text.upper()
    #print(text)
    if all(substring in text for substring in desktop_ok):
        ss_type = 'DESKTOP SCREENSHOT - OK'
        print('DESKTOP SCREENSHOT - OK')
        
    elif all(substring in text for substring in mobile_ok):
        ss_type = 'MOBILE SCREENSHOT - OK'
        print('MOBILE SCREENSHOT - OK')
    else:
        ss_type = 'Unable to identify image'
        print('Unable to identify image')
        temp_data = {'ORDER_ID':order_id,'FILENAME':file,'SCREENSHOT_TYPE':ss_type,'RESULT':'Processed'}
        data.append(temp_data)
        continue
    try:
        order_id = ((text.split(start))[1].split(end)[0]).strip()        
        print(order_id)
    except:
        print('Unable to decode order #')
        pass
    
    temp_data = {'ORDER_ID':order_id,'FILENAME':file,'SCREENSHOT_TYPE':ss_type,'RESULT':'Processed'}
    data.append(temp_data)

pixel_df = pd.DataFrame.from_dict(data)
#SAVE DATAFRAME AS AN EXCEL WORKBOOK
pixel_df.to_excel(r"C:\Users\Rish\Documents\Client projects Python\CDM\Order_ID_Extractor\extracted_data.xlsx",index=False)

T_T = str(datetime.now()-s_time).split('.')[0]
print(T_T)
