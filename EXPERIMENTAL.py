# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 02:17:39 2024

@author: Rish
"""
import requests
import pandas as pd
from bs4 import BeautifulSoup
import xlwings as xw
import time
from fp.fp import FreeProxy

proxies = ["http://46.16.201.51:3129","http://207.2.120.19:80","http://50.227.121.35:80"]
    # add more proxies as needed]

proxy = FreeProxy().get()

#Open excel workbook and get details
app = xw.App(add_book=False, visible=True)
app = xw.App(visible=True)
app.UpdateLinks = False
app.display_alerts = False
    
#page = "https://www.amazon.in/gp/customer-reviews/R2JG7TSXBWU91R?ref=pf_vv_at_pdctrvw_srp"
    
#soup = BeautifulSoup(requests.get(page).content, "html.parser")
#print(soup)    

#body = soup.find("span", {"data-hook": "review-body"}).text.strip()

#rating = soup.find("i", {"data-hook": "review-star-rating"}).text.strip()
#title = soup.find("a", {"data-hook": "review-title"}).text.strip()


filepath = r"C:\Users\Rish\Documents\GitHub_Repositories\Review_Scraper_Streamlit\Review_sheet.xlsx"
mywb = xw.books.open(filepath, update_links=False)
print(filepath)


ui_ws =  xw.Book("Review_sheet.xlsx").sheets['Ui']
log_ws = xw.Book("Review_sheet.xlsx").sheets['Log'] 
ui_lr = ui_ws.range('A1048576').end('up').row
ui_lr_B = ui_ws.range('B1048576').end('up').row +1
log_lr = log_ws.range('B1048576').end('up').row +1
print(ui_lr)
print(log_lr)

for x in range(ui_lr_B,ui_lr+1):
    print(x)
    
    page = ui_ws.range("A" + str(x)).value
    
    for proxy in proxies:
        
        soup = BeautifulSoup(requests.get(page).content, "html.parser",proxies={"http": proxy, "https": proxy})
        time.sleep((2))


    body = soup.find("span", {"data-hook": "review-body"}).text.strip()
    print(body)
