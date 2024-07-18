
import requests
import pandas as pd
import streamlit as st
import time



#-------------------------------------------------------
# FUNCTION TO CHECK IF THE URL IS ABLE TO RETURN STATUS CODE 200
def valid_url(user_url):
    req = requests.get(user_url)
    try:
        if req.status.code != requests.codes['ok']:
            VALIDURL = "VALID"
    except:
        VALIDURL = "INVALID"    
    return user_url  
#-------------------------------------------------------

F_URL = "https://1.rome.api.flipkart.com/api/3/reviews/permalink"
querystring = {"reviewId":"SUPGXBUKZY3WV6PN:35"}
#querystring = {"reviewId":"WICGNJH3SDWZSWYS:15"}


payload = ""
headers = {
    "cookie": "at=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjhlM2ZhMGE3LTJmZDMtNGNiMi05MWRjLTZlNTMxOGU1YTkxZiJ9.eyJleHAiOjE3MjExNTc0NzQsImlhdCI6MTcyMTE1NTY3NCwiaXNzIjoia2V2bGFyIiwianRpIjoiYTI0Y2I2MTItNTBhMy00YzkxLTg1YjUtZWRiYmI1YTE0NWQ3IiwidHlwZSI6IkFUIiwiZElkIjoiY2xzMWVjZGR4MTJpcDB3ZDd2eGIyZXg0bi1CUjE3MDY2ODE5MDk0NDUiLCJiSWQiOiJXSVhTUU0iLCJrZXZJZCI6IlZJRkVDNzBBRTlBQTI0NDJCQUI1MDMzODVEQTFEOEZENzAiLCJ0SWQiOiJtYXBpIiwiZWFJZCI6ImZSZVFrRmktdGg4a1FiVjluS1FtTVR1SkNUakhzelpsIiwidnMiOiJMSSIsInoiOiJDSCIsIm0iOnRydWUsImdlbiI6NH0._cvBOqIWebdx8w1Hbchgoh8FviXOouGKxnFhaJtjpQM; rt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjNhNzdlZTgxLTRjNWYtNGU5Ni04ZmRlLWM3YWMyYjVlOTA1NSJ9.eyJleHAiOjE3MzcwNTMyNzQsImlhdCI6MTcyMTE1NTY3NCwiaXNzIjoia2V2bGFyIiwianRpIjoiMmE1NWMxZmYtMDc2MS00MGJkLWJhODMtNzZkZDY1NzU5OTI1IiwidHlwZSI6IlJUIiwiZElkIjoiY2xzMWVjZGR4MTJpcDB3ZDd2eGIyZXg0bi1CUjE3MDY2ODE5MDk0NDUiLCJiSWQiOiJXSVhTUU0iLCJrZXZJZCI6IlZJRkVDNzBBRTlBQTI0NDJCQUI1MDMzODVEQTFEOEZENzAiLCJ0SWQiOiJtYXBpIiwibSI6eyJ0eXBlIjoibiJ9LCJ2IjoiRUVDUjgxIn0.VmTwgPvqvYzxruFhn9euyrBeOmt-tG4Ih2Umm2x-uuI; S=d1t17UT8%2FPz8%2FRD8%2FP0o%2FPz9gcuE73c6pxfCH8ZsiavCMvb0jrE%2FNFWBRH5%2B20j5CezAmizGhnrHsna755sl8dHmgEg%3D%3D; SN=VIFEC70AE9AA2442BAB503385DA1D8FD70.TOK0E206344536643B881DBBBC872919C1D.1721155691.LI",
    "Accept": "*/*",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8,hi;q=0.7",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
    "Cookie": "T=cls1ecddx12ip0wd7vxb2ex4n-BR1706681909445; _pxvid=8daa5d68-c000-11ee-9822-a314e037ca6a; ULSN=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJjb29raWUiLCJhdWQiOiJmbGlwa2FydCIsImlzcyI6ImF1dGguZmxpcGthcnQuY29tIiwiY2xhaW1zIjp7ImdlbiI6IjEiLCJ1bmlxdWVJZCI6IlVVSTI0MDEzMTExNDkwNzEzM1czQjFVRlEiLCJma0RldiI6bnVsbH0sImV4cCI6MTcyMjQ2MTk0NywiaWF0IjoxNzA2NjgxOTQ3LCJqdGkiOiJlNzBkMzcyMC0yZGE0LTQyZWQtODk0YS0zNjFiMjUzYmI0ZGUifQ.qX17rLeoLWfMqqaY8n-fvlOkxX1kF_jS81XYAgA7Q8U; ud=6.vlZgohnaUd0_DVPJq-kjaplmoUK11FifW4L36x4JNl2f7i396ewrjleHJexcrTPTSIcaN85v8PHN8gNXWrdjPCVU6LnS4AhAA9mHQ5aZzjP9EpIRA2YvAeIs2pSMIHTVlJ3Lch73kwlWVdLJhUgFaoVlBYz4TXnWGvlGfAgQT4t9iGaF9WbztdaFcGimygU0Oi55kcgpgPKp3iJWQFStA5PNgAXXvqz6bCpZhdZN5JoTZ9KkCMXJhV46HOoIYN15GxSGPJtAZ5n2nHnE8dMqqXqCaSf1BPKkkwMq3zX7Ld8wo2hgoIS1qws0569Nc8bgzMXZwYtnBgc40cdyPizARVn1GFy9n6CNFRlw0VxGB15q--9kO-f-lyMTvzbkVVg6cJtV8WwtdITSBmpgRZEjjTRRYNmcfRArLLaMh-Ix-LtymdcyInio3kypZiWiOz2CSXD6jFAfXjwHxx9NKAD5CmEWpPtyxSkvJTkfae_RirnJZ15Q9lSdm-BT663zhoOKX9vUtuaiChgIo0V_e1kDxAU2RKL5tyYp463HDuTG42Mnkb5TTC6sybWX7dw4HT_NC1Yy5ZOWdwbdDlnHOT2T-M7R4SpNXg8EQayLwSQOnlon0doHYz-0BhHYbtMcjayQuq0L7pZvO28BWgqcOUuz3fQkGM1Igzc1oyTsBH0PIJHH1J2g43iguX0fAIm6Ne5yLKIyVDLiK9NHVm-zivkzwrpiZSaYEtr1VQvQQKuxEjM; _gcl_au=1.1.1122277935.1720701041; at=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjhlM2ZhMGE3LTJmZDMtNGNiMi05MWRjLTZlNTMxOGU1YTkxZiJ9.eyJleHAiOjE3MjExNTc0NzQsImlhdCI6MTcyMTE1NTY3NCwiaXNzIjoia2V2bGFyIiwianRpIjoiYTI0Y2I2MTItNTBhMy00YzkxLTg1YjUtZWRiYmI1YTE0NWQ3IiwidHlwZSI6IkFUIiwiZElkIjoiY2xzMWVjZGR4MTJpcDB3ZDd2eGIyZXg0bi1CUjE3MDY2ODE5MDk0NDUiLCJiSWQiOiJXSVhTUU0iLCJrZXZJZCI6IlZJRkVDNzBBRTlBQTI0NDJCQUI1MDMzODVEQTFEOEZENzAiLCJ0SWQiOiJtYXBpIiwiZWFJZCI6ImZSZVFrRmktdGg4a1FiVjluS1FtTVR1SkNUakhzelpsIiwidnMiOiJMSSIsInoiOiJDSCIsIm0iOnRydWUsImdlbiI6NH0._cvBOqIWebdx8w1Hbchgoh8FviXOouGKxnFhaJtjpQM; rt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjNhNzdlZTgxLTRjNWYtNGU5Ni04ZmRlLWM3YWMyYjVlOTA1NSJ9.eyJleHAiOjE3MzcwNTMyNzQsImlhdCI6MTcyMTE1NTY3NCwiaXNzIjoia2V2bGFyIiwianRpIjoiMmE1NWMxZmYtMDc2MS00MGJkLWJhODMtNzZkZDY1NzU5OTI1IiwidHlwZSI6IlJUIiwiZElkIjoiY2xzMWVjZGR4MTJpcDB3ZDd2eGIyZXg0bi1CUjE3MDY2ODE5MDk0NDUiLCJiSWQiOiJXSVhTUU0iLCJrZXZJZCI6IlZJRkVDNzBBRTlBQTI0NDJCQUI1MDMzODVEQTFEOEZENzAiLCJ0SWQiOiJtYXBpIiwibSI6eyJ0eXBlIjoibiJ9LCJ2IjoiRUVDUjgxIn0.VmTwgPvqvYzxruFhn9euyrBeOmt-tG4Ih2Umm2x-uuI; vd=VIFEC70AE9AA2442BAB503385DA1D8FD70-1707123189351-264.1721155674.1721155674.164470814; vh=1198; vw=2056; dpr=2; Network-Type=4g; gpv_pn=HomePage; gpv_pn_t=FLIPKART%3AHomePage; AMCVS_17EB401053DAF4840A490D4C%40AdobeOrg=1; AMCV_17EB401053DAF4840A490D4C%40AdobeOrg=-227196251%7CMCIDTS%7C19920%7CMCMID%7C34055651685231864964004395437315407955%7CMCAAMLH-1721760476%7C6%7CMCAAMB-1721760476%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1721162876s%7CNONE%7CMCAID%7CNONE; pxcts=ea301aff-43a3-11ef-88ef-5f569b3bf814; K-ACTION=null; S=d1t17DGYOP0s/Pz8/P25HWD8EPx7OI6BRUDNkqZ/Ciy/Ks2IS7TSKft39B3zTAvqWIUGlKSj14oTtvEHCTzJyE+4Wkw==; _px3=2a4d2b4f40e33c3b2d5f01f91ac86a170b59165baa0bb44e7cdda79d0e3ecad5:6u9nz7mEebi2OktBwaw5FeaT/H0dQEg2fD0q4eHWBQggAVJryusmJhjgOkg5SRqPcZ6iUy025JzA1K126ZfkwQ==:1000:0/TtCQRC0qUxswsb9WwhozA6/OSnsNllLSCRFcEOV37vZZwpZN69jvHe52RzRHqDFMVvaz1ZxxbYjfd0rLCw3a6bHRECDFJ+5xt+SIqBK9KVoP6J1qMgk/7WRO/viSpDZbU34uoYksijMbrW3pzrgpogECrhA+7O1xS/LKYK5zE5auzNZ6X1z6SXce2VDFxOI2d/JgE7H/PTyWHZHXl1Q2XtCTQ2phkOqiBzQzSilCw=; SN=VIFEC70AE9AA2442BAB503385DA1D8FD70.TOK0E206344536643B881DBBBC872919C1D.1721155691.LI",
    "DNT": "1",
    "Origin": "https://www.flipkart.com",
    "Referer": "https://www.flipkart.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "X-User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 FKUA/website/42/website/Desktop",
    "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "" + "macOS" +"",
}


def flip_ID(url):
    
    start = '/REVIEWS/'
    end = '?REVIEWID='
    s = url.upper()
    output = s[s.find(start)+len(start):s.rfind(end)]
    return output
    

def crawl_flip(input_url):
    
    querystring['reviewId'] = flip_ID(input_url)
    
    response = requests.request("GET", F_URL, data=payload, headers=headers, params=querystring)
    print(response.text)
    data = response.json()
    rdata =  data['RESPONSE']['reviewInfo']
    print(rdata)
          
    data_list = []
    data_list.append(rdata)
    df = pd.DataFrame.from_dict(data_list)
    
    result = df
    return result

#print(rdata['title'])
#rdata.get("reviewText")


# INPUT
#input_url = 'https://www.flipkart.com/reviews/ACCGYZF55ZD93YSH:422?reviewId=64ea04a6-18bc-4120-a723-23208e7f6b3c'
#output = crawl_flip(input_url)

#df = pd.DataFrame(columns=['VALIDITY','Review ID','Reviewer name','Purchase verified','Review stars given','Review posted on','Product name','Review title','Word count','Media'])
#df['Review ID'][1] = output['reviewId']




# STREAMLIT FRONT END

branding_title = 'Developed by Arora Consulting Private Limited'
contact_url = 'https://www.linkedin.com/in/r1shabharora/'

txt = st.text_area('ENTER REVIEW LINK')
#txt = "https://www.flipkart.com/reviews/ACCGYZF55ZD93YSH:422?reviewId=64ea04a6-18bc-4120-a723-23208e7f6b3c"


if st.button("Get Data"):
    # Call the function with the movie title as input
    result = crawl_flip(txt)
    st.write('Below is the data:',result)
    

  

#---------------------------------------------------------------------------
#from selenium import webdriver
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC

