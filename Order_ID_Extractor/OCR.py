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
import time
import numpy as np


# create an empty dataframe with desired columns
df = pd.DataFrame()
df = pd.DataFrame(columns=["ORDER_ID",'FILENAME', 'SCREENSHOT_TYPE',"RESULT","TEXT"])
#EMPTY LIST
data = []
data = []

#capture start time of program
s_time = datetime.now()


def get_order_id(file_path,file):
    
    order_id = '-'
    ss_type = "-"
    text = "-"
    result = "-"
    
    #What contains what to determine which is what
    desktop_ok = ["WRITE A PRODUCT REVIEW","LEAVE SELLER FEEDBACK", "LEAVE DELIVERY FEEDBACK"]
    desktop_not_ok =  ["DAMRU"]
    mobile_ok = ["DOWNLOAD INVOICE","ORDER DATE","SHIPMENT DETAILS","DELIVERY ESTIMATE","QTY:"]
    mobile_not_ok = ["KAKA"]
    
    #FETCH ORDER DETAILS BETWEEN THE FOLLOWING
    start = 'ORDER #'
    end = 'ORDER TOTAL'
    
    try:
        image = Image.open(file_path)
        text = pytesseract.image_to_string(image)
        text = text.upper()
        #print(text)
        
        try:
            order_id = ((text.split(start))[1].split(end)[0]).strip()[:20]
            order_id = order_id.replace('\r', '').replace('\n', '').strip()
            #print(order_id)
        except:
            #print('Unable to decode order #')
            image_data = {'ORDER_ID':order_id,'FILENAME':file,'SCREENSHOT_TYPE':ss_type,'RESULT':'error',"TEXT":text}
            return image_data
        
        #print(text)
        if all(substring in text for substring in desktop_ok):
            ss_type = 'DESKTOP SCREENSHOT - OK'
            result = "ok"
            #print('DESKTOP SCREENSHOT - OK')
            
        elif all(substring in text for substring in mobile_ok):
            ss_type = 'MOBILE SCREENSHOT - OK'
            result = "ok"
            #print('MOBILE SCREENSHOT - OK')
        else:
            ss_type = 'Unable to identify image'
            result = "not ok"
            #print('Unable to identify image')
     
        image_data = {'ORDER_ID':order_id,'FILENAME':file,'SCREENSHOT_TYPE':ss_type,'RESULT':result,"TEXT":text}
        return image_data
    except Exception as ex:
        image_data = {'ORDER_ID':order_id,'FILENAME':file,'SCREENSHOT_TYPE':ss_type,'RESULT':ex,"TEXT":text}
        return image_data
        
    
#mention folder path
source_path = r"/Users/rishabharora/Documents/GitHub/PERSONAL/Review_Scraper_Streamlit/Order_ID_Extractor/SOURCE"
#get all files from said directory
dir = os.listdir(source_path)

current_index = 0
t_list = []
total_files = len(dir)

for file in dir:
    
    ts = time.time()
    ETA = round((np.mean(t_list) * total_files)/60,2)
    current_index = current_index + 1
    progress = round((current_index / total_files) * 100,2)
    print("processing_",current_index,"_of_",total_files,"_ETA_",ETA,"minutes","progress_",progress,"_%")
    
    if ".DS_Store" in file:
        print(file)
        continue
    
    #file = r"2 - aditya goel.jpg"
    image_path = os.path.join(source_path,file)
    image_data = get_order_id(image_path,file)

    data.append(image_data)
    
    #CACULATING TIME ELAPSED IN SECONDS
    ct = time.time(); et = (ct - ts); t_list.append(et)
    
    

df = pd.DataFrame.from_dict(data)
#SAVE DATAFRAME AS AN EXCEL WORKBOOK
df.to_excel(r"/Users/rishabharora/Documents/GitHub/PERSONAL/Review_Scraper_Streamlit/Order_ID_Extractor/extracted_data.xlsx",index=False)

T_T = str(datetime.now()-s_time).split('.')[0]
print(T_T)
