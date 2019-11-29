import requests
from bs4 import BeautifulSoup
import csv
import re





website_url = requests.get('https://en.wikipedia.org/wiki/List_of_mobile_network_operators').text
#from bs4 import BeautifulSoup
soup = BeautifulSoup(website_url,'lxml')
#print(soup.prettify())
ti = 0

My_table = soup.find('table',{'class':'wikitable sortable'})
headers = ['Rank','Company','Main Markets','Technology','Total Subscription','Ownership']
with open('telecom-operators.csv', 'w', newline='', encoding="utf-8") as f:
    writer = csv.writer(f, delimiter=',', lineterminator='\n')
    writer.writerow(headers)
    for tr in My_table('tr'):
    	row = [t.get_text(strip=True).strip('[List]') for t in tr(['td'])]
    	if row :
            cell1 = row[0]
            cell2 = row[1].replace('[', '').replace(']', '')
            cell3 = row[2].replace('[', '').replace(']', '')
            cell4 = row[3].replace('[', '').replace(']', '')
            cell5 = row[4].replace('[','').replace(']','')
            row = [cell1,cell2,cell3,cell4,cell5]
            writer.writerow(row)
        