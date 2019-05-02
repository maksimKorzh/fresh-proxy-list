import requests
from bs4 import BeautifulSoup

# variable to store working proxies
proxyList = []

# make reguest to 'https://free-proxy-list.net' to scrape proxies
response = requests.get('https://free-proxy-list.net')

# parse response with beautiful soup
bs = BeautifulSoup(response.text, 'lxml')

table = bs.find('table')        # find proxy table element
rows = table.find_all('tr')     # fidn list of all rows in table

def init_proxy_list(*args):
    '''
    Function associates each single row in a table with corresponding values,
    extracts only those proxies that support 'https' and typed as 'anonymous'
    or 'elite proxy', tests each proxy via connecting to 'https://www.httpbin.org/ip'
    and if response returns the corresponding IP then the proxy is appended to list.
    Function can take optional 'limit' argument of integer type to define the number
    of proxies to be scraped and stored.
    '''
    for row in rows:
        ip = row.contents[0].text
        port = row.contents[1].text
        anonym = row.contents[4].text
        secconn = row.contents[6].text
        
        if secconn == 'yes' and anonym == 'anonymous' or anonym == 'elite proxy':
            line = 'http://' + ip + ':' + port
            proxies = { 'http': line, 'https': line }
            print('Probing proxy:', line)
            
            try:
                testIP = requests.get('https://httpbin.org/ip', proxies = proxies, timeout = 3)
                resIP = testIP.json()['origin']
                origin = resIP.split(',')
                
                if origin[0] == ip:
                    print('  Proxy ok! Appending to proxyList...')
                    proxyList.append(line)

            except:
                print('  Bad proxy!')
            
            if len(args) == 1:
                if type(args[0]) == int:
                    if args[0] > 0 and len(proxyList) == args[0]:
                        break
                else:
                    print('"[limit]" agrument must be integer!')
                    break
            
            if len(args) > 1:
                print('Too many arguments!')
                break

def write_to_file():
    '''
    Writes 'proxyList' elements to file 'fresh_proxies.txt' in case
    if at least one entry is available.
    '''
    if len(proxyList) == 0:
        print('Please call "init_proxy_list([limit])" first')
    with open('fresh_proxies.txt', 'w') as f:
        for proxy in proxyList:
            f.write("%s\n" % proxy)
