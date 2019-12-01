import requests
from bs4 import BeautifulSoup
import csv

#defining constants
website_url = requests.get('https://en.wikipedia.org/wiki/List_of_telephone_operating_companies').text

def retrieve():
    soup = BeautifulSoup(website_url,'lxml')
    soup_table = soup.find('table',{'class':'wikitable sortable'})
    return soup_table


def transform_load(table):
     # Setting the headers for the csv
    headers = ['Rank','Company','Total Revenue (Billion$)','Country']
    #Cleaning and writing telecom-operators.csv
    with open('telecom-revenue.csv', 'w', newline='', encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=',', lineterminator='\n')
        writer.writerow(headers)
        for tr in table('tr'):
            row = [t.get_text(strip=True).strip('[List]') for t in tr(['td'])]
            if row :
                cell1 = row[0]
                cell2 = row[1].replace('[]','')
                # Removing $ sign and unnecessary brackets
                cell3 = row[2].replace('[','').replace(']', '').replace('$','')
                if len(cell3)>5:
                    #Clipping the garbage values 
                    cell3 = cell3[0:5]
                cell4 = row[3].replace('[', '').replace(']', '')
                row = [cell1,cell2,cell3,cell4]
                writer.writerow(row)
def run():
    table = retrieve()
    transform_load(table)

if __name__ == '__main__':
    run()
