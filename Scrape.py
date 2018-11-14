import requests
import string
import xlwt
from bs4 import BeautifulSoup

url = 'http://myboot.com.au/vic/'
suburl = '/suburblist.aspx'
letters = list(string.ascii_lowercase)
excel = xlwt.Workbook()
sh = excel.add_sheet('output', cell_overwrite_ok=True)
col1 = 'Suburb'
col2 = 'Postcode'

sh.write(0, 0, col1)
sh.write(0, 1, col2)

i = 1

for l in letters:
    reqUrl = url + l + suburl
    r = requests.get(reqUrl)
    soup = BeautifulSoup(r.content, 'html.parser')
    divs = soup.findAll("div", {"class": "cssSUBURBDESC"})
    for div in divs:
        try:
            text = div.find('a').contents[0]
            suburb = text.split('(')[0]
            post = text.split('(')[1].split(')')[0]
            sh.write(i, 0, suburb)
            sh.write(i, 1, post)
            i += 1
            pass
        except IndexError:
            continue

excel.save('out.xls')





