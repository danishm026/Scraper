import requests
import constants
import sys
from bs4 import BeautifulSoup

def getPage(url):
	timeouts = 0
	while timeouts < constants.TRIES_ON_TIMEOUT:
		try:
			response = requests.get(url, timeout=constants.TIMEOUT)
			if response.status_code == 200:
				return response.text
			else:
				print('Response Code not 200 for URL: ' + url, file=sys.stderr)
				return None
		except requests.Timeout:
			timeouts += 1
	print('Timeout for URL: ' + url, file=sys.stderr)
	return None
		
		

def getElementsByConstraint(html, tag, attribute_name, attribute_value):
    document = BeautifulSoup(html, constants.PARSER)
    
    tags = document.find_all(tag)
    result = []
    
    for t in tags:
        try:
            if t[attribute_name] == attribute_value:
                result.append(t)
        except KeyError:
            pass
    return result
   
   

def getElementsByTagName(html, tag):
    document = BeautifulSoup(html, 'html.parser')
    return document.find_all(tag)
   
   
 
def getElementById(html, id_value):
 	document = BeautifulSoup(html, constants.PARSER)
 	element = document.find_all(id=id_value)
 	return element[0]
 


def getElementContent(element):
 	return element.string
 

if __name__ == '__main__':
	print(getPage(constants.SITE_URL))