import urllib.request

url='http://www.whatismyip.com.tw'

proxy_support=urllib.request.ProxyHandler({'http':'123.146.235.230:53281'})

opener=urllib.request.build_opener(proxy_support)

opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36')]

urllib.request.install_opener(opener)

response=urllib.request.urlopen(url)
html=response.read().decode('utf-8')

print(html)

