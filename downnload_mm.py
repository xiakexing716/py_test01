import urllib.request
import os

def url_open(url):
	req=urllib.request.Request(url)
	req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36')
	# proxy_support=urllib.request.ProxyHandler({'http':'123.146.235.230:53281'})
	# opener=urllib.request.build_opener(proxy_support)
	# opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36')]
	# urllib.request.install_opener(opener)
	response=urllib.request.urlopen(req)
	html=response.read()
	return html


def get_page(url):
	html=url_open(url).decode('utf-8')
	
	a=html.find('current-comment-page')+23
	b=html.find(']',a)
	
	return html[a:b]


def find_imgs(url):
	html=url_open(url).decode('utf-8')
	img_addres=[]

	a=html.find('img src=')
	
	
	while a != -1:
		b=html.find('.jpg',a,a+255)
		if b != -1:
			img_addres.append("http:"+html[a+9:b+4])
		else:
			b=a+9

		a=html.find('img src=',b)

	return img_addres


def save_imgs(folder,img_addres):
	for each in img_addres:
		filename=each.split('/')[-1]
		with open(filename,'wb') as f:
			img=url_open(each)
			f.write(img)





def download_mm(folder="OOXX",pages=10):
	os.mkdir(folder)
	os.chdir(folder)

	url="http://jandan.net/ooxx/"
	page_num=int(get_page(url))

	for  i in range(pages):
		page_num -=1
		page_url=url+"page-"+str(page_num)+"#comments"
		img_addres=find_imgs(page_url)
		save_imgs(folder,img_addres)


if __name__=="__main__":
	download_mm()

