from bs4 import BeautifulSoup
from urllib.parse import urljoin
import sys
import urllib.request
import urllib.parse
import urllib.error

#method to get page html
def getPage(url):
	html = None	
	try:
		response = urllib.request.urlopen(url, timeout=10)
		html = response.read()
	except urllib.error.URLError:
		print('timeout on ' + url, file=sys.stderr)		
	return html


#method to get all links in a page
def getElementsByTagName(html, tag):
	document = BeautifulSoup(html, 'html.parser')
	return document.find_all(tag)


#method to get number of pages for current model
def number_of_pages(html):
	links = getElementsByTagName(html, 'a')	
	for link in links:
		try:
			if 'prevnext' in link['class'] and link.string.find("Last page") != -1:
				last_page_url = link['href']
				parsed = urllib.parse.urlparse(last_page_url)
				return int(urllib.parse.parse_qs(parsed.query)['page'][0].strip())
		except KeyError:
			pass
	return 1	


#method to get all urls for current model from a base url
def get_all_urls(url, html):
	pages = number_of_pages(html)
	urls = []
	for i in range(1, pages+1):
		urls.append(url + '?page=' + str(i))
	return urls
	

#method to get link to photo pages
def get_photo_page_links(url, page):
	result = []
	links = getElementsByTagName(page, 'a')
	for link in links:
		try:
			if link['itemprop'] == 'contentURL':
				result.append(urljoin(url, link['href']))
		except KeyError:
			pass
	return result			 


#method to get image url
def get_photo_link(link):
	photo_page = getPage(link)
	if photo_page == None:
		return None
	images = getElementsByTagName(photo_page, 'img')
	for image in images:
		try:
			if image['itemprop'] == 'contentUrl':
				return urljoin(link, image['src'])
		except KeyError:
			pass

if __name__ == '__main__':
	base_url = input().strip()
	base_page = getPage(base_url)
	if base_page == None:
		print('Failed to download base page, try agin.', file=sys.stderr)
	urls = get_all_urls(base_url, base_page)
	
	for url in urls:
		page = getPage(url)
		if page == None:
			print('Failed to download page: ' + url, file=sys.stderr)
			continue
		links_to_photo_page = get_photo_page_links(url, page)
		for link in links_to_photo_page:
			print(get_photo_link(link))
			sys.stdout.flush()
	
