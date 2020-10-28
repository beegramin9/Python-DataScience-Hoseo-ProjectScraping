import datetime
dt = datetime.datetime.now()
df = dt.strftime('%Y_%m_%d')

import requests
from bs4 import BeautifulSoup

import openpyxl
excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = 'Question list'

url = 'https://hashcode.co.kr/?page='

for page in range(5):
    res = requests.get(url+str(page+1))
    raw = res.text
    html = BeautifulSoup(raw,'html.parser')

    title_list = html.select('div.top a')
    
    for title in title_list:
        sheet.append([title.text])

excel.save('9_hashcode_'+df+'.xlsx')