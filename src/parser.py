import requests
from bs4 import BeautifulSoup




url = 'https://koopteh.onego.ru/student/lessons/'
res = requests.get(url)
bs = BeautifulSoup(res.text, 'lxml')
line = bs.find("table", class_ = 'styled').find('tbody').find_all('a')
for row in line:
    # col = row.find_all('a').get('href')
    row.get('href')

url2 = row.get("href") + 'export?format=csv'
respon2e = urllib.request.urlopen(url2)
with io.TextIOWrapper(respon2e, encoding='utf-8') as f:
    reader = csv.reader(f)

    for ro in reader:
        print(ro)
