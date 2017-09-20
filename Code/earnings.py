import requests
import csv
from BeautifulSoup import BeautifulSoup

url = 'http://www.nasdaq.com/earnings/earnings-calendar.aspx'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)
table = soup.findAll("table")
list_of_rows = []
for elmt in table[3:-5]:
    for row in elmt.findAll('tr'):
        list_of_cells = []
        for cell in row.findAll('td'):
            text = cell.text.replace('&nbsp;', '')
            list_of_cells.append(text)
        list_of_rows.append(list_of_cells)
outfile = open("./earnings-calendar.csv", "wb")
writer = csv.writer(outfile)
#writer.writerow(["Last", "First", "Middle", "Gender", "Race", "Age", "City", "State"])
writer.writerows(list_of_rows)
