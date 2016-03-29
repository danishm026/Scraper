import urllib.request

def getPage(url):
	response = urllib.request.urlopen(url)
	html = response.read()
	return html

def getResource(resourceUrl):
	filename, headers = urllib.request.urlretrieve(resourceUrl)
	return filename 
