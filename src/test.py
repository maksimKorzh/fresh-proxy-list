import FreshProxyList as proxy

proxy.init_proxy_list(5)
proxy.write_to_file()

print('\n\nFresh proxies:\n')

for proxy in proxy.proxyList:
    print(proxy)
