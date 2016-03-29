import requests
import constants
import sys

def getPage(url):
	timeouts = 0
	while timeouts < 5:
		try:
			response = requests.get(url, timeout=constants.TIMEOUT)
			if response.status_code == 200:
				return response.text
			else:
				return None
		except requests.Timeout:
			timeouts += 1
	print('Timeout for URL: ' + url, file=sys.stderr)
	return None
		
if __name__ == '__main__':
	print(getPage(constants.SITE_URL))