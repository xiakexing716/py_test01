import urllib.request
import urllib.parse
import json
import time

while True:

	content=input("请输入需要翻译的内容：")
	if content=='q':
		break
	url='http://fanyi.youdao.com/translate'

	head={}
	head['User-Agent']='Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36'


	data={}
	data['i']=content
	data['smartresult']='dict'
	data['client']='fanyideskweb'
	data['salt']='1509718443509'
	data['sign']='5b1fbf4855917ad286012201dd59bb30'
	data['doctype']='json'
	data['version']='2.1'
	data['keyfrom']='fanyi.web'
	data['action']='FY_BY_CLICKBUTTION'
	data['typoResult']='false'
	data=urllib.parse.urlencode(data).encode('utf-8')

	req=urllib.request.Request(url,data,head)
	response=urllib.request.urlopen(req)
	html=response.read().decode('utf-8')

	target=json.loads(html)

	print("翻译结果: %s" % (target['translateResult'][0][0]['tgt']))

	time.sleep(5)