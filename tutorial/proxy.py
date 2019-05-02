import requests
from bs4 import BeautifulSoup

proxyList = []

response = requests.get('https://free-proxy-list.net/')
bs = BeautifulSoup(response.text, 'lxml')

table = bs.find('table')
rows = table.find_all('tr')

count = 0

for row in rows:
    ip = row.contents[0].text
    port = row.contents[1].text
    anonym = row.contents[4].text
    secconn = row.contents[6].text

    if(secconn == 'yes' and (anonym == 'anonymous' or anonym == 'elite proxy')):
        line = 'http://' + ip + ':' + port
        proxies = { 'http': line, 'https': line }
        
        try:
            testIP = requests.get('https://httpbin.org/ip', proxies = proxies, timeout = 3)
            print(testIP.text)
            resIP = testIP.json()['origin']
            origin = resIP.split(',')
            
            if origin[0] == ip:
                print('  Proxy ok! Appending proxy to proxyList...')
                proxyList.append(line)
                count += 1
                
                if count == 5:
                    break
                
        except:    
            print('Bad proxy')

with open('proxies.txt', 'w') as f:
    for proxy in proxyList:
        f.write("%s\n" % proxy)        
