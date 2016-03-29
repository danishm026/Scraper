import requests
import constants

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
	return None
		
if __name__ == '__main__':
	print(getPage(constants.SITE_URL))