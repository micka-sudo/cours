# -*- coding: utf-8 -*-
import requests, json
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

with open('scrap/json/passengers.json', 'r', encoding='utf-8') as f:
    urls = json.loads(f.read())

i = 0
rows = []
for url in urls:
    soup = BeautifulSoup(requests.get('https://www.encyclopedia-titanica.org%s'%(url)).text, 'html.parser')
    
    ticket = home = job = nat = None
    for strong in soup.find_all('strong'):
        if strong.text.strip() == 'Ticket No':
            ticket = strong.parent.text.split(',')[0].split('.')[1].strip()
        if strong.text.strip() == 'Nationality':
            nat = strong.parent.text.split(':')[1].strip()
        if strong.text.strip() == 'Last Residence':
            home = ' '.join([s for s in strong.parent.text.replace('\n' , '').split(' ') if s != ''][3:])
        if strong.text.strip() == 'Occupation':
            job = strong.parent.text.split(':')[1].strip()
   
    rows.append([
        url,
        ticket,
        nat,
        home,
        job
    ])
    
    i+=1
    print('%s/%s - %s - %s'%(i, len(urls), np.round(i / len(urls) * 100, 2), url))

pd.DataFrame(rows, columns=['url', 'ticket', 'nat', 'home', 'job']).to_csv('csv/portraits.csv', index=False, encoding='utf-8')

# with open('scrap/html/a.html', 'w', encoding='utf-8') as f:
#     f.write(BeautifulSoup(requests.get('https://www.encyclopedia-titanica.org/titanic-victim/anthony-abbing.html').text, 'html.parser').prettify())

# 

############### Get Passengers list ###############

# urls = []
# for url in ['https://www.encyclopedia-titanica.org/titanic-first-class-passengers/', 
#             'https://www.encyclopedia-titanica.org/titanic-second-class-passengers/',
#             'https://www.encyclopedia-titanica.org/titanic-third-class-passengers/']:
#     urls += [
#         a['href'] for a in BeautifulSoup(requests.get(url).text, 'html.parser').
#         find('table', attrs={'id':'manifest'}).
#         find_all('a', attrs={'itemprop':'url'})
#     ]
# print(len(urls))

# with open('scrap/json/passengers.json', 'w', encoding='utf-8') as f:
#     f.write(json.dumps(urls))

##################################################
