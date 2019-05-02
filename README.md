# Fresh proxy list
A simple library that scrapes proxies from 'https://free-proxy-list.net' website, tests
whether the REMOTE_ADDR has been changed using 'https://www.httpbin.org/ip' and stores
them into list. Writing 'proxyList' into file is also supported.

# Documentation
                 proxyList - variable that stores tested proxies
    
    init_proxy_list(limit) - main routine, initializes proxyList.
                             'limit' arg  is optional, it defines
                             how many proxies to store.
    
           write_to_file() - write 'proxyList' to file. 'proxyList' must
                             contain at least one entry.

# Usage example

    import FreshProxyList as proxy      # import module

    proxy.init_proxy_list(5)            # get 5 proxies
    proxy.write_to_file()               # write them to file

    print('\n\nFresh proxies:\n')

    for proxy in proxy.proxyList:
        print(proxy)
