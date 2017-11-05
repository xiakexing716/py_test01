import urllib.request
import re

def open_url(url):
	req=urllib.request.Request(url)
	req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36')
	page=urllib.request.urlopen(req)
	html=page.read().decode('utf-8')

	return html

def get_ip(html):
	p=r'(?:(?:[0,1]?\d?\d|2[0-4]\d|25[0-5])\.){3}(?:[0,1]?\d?\d|2[0-4]\d|25[0-5])'
	iplist=re.findall(p,html)
	p2=r'<td data-title="PORT">(\d{1,})</td>'
	ptlist=re.findall(p2,html)
	for each,port in zip(iplist,ptlist):
		print('ip:',each,'port:',port)
	# for each in iplist:
	# 	filename=each.split("/")[-1]
	# 	urllib.request.urlretrieve(each,filename,None)

if __name__=='__main__':
	url="http://www.kuaidaili.com/free/inha/"
	get_ip(open_url(url))
