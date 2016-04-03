import constants
import page
from bs4 import BeautifulSoup
import urllib.parse
import sys
import re


def getLetterLink(html, letter):
    prefix = 'Pictures of Celebritries starting with '
    
    element = page.getElementsByConstraint(html, 'a', 'title', prefix + letter)[0]
    link = urllib.parse.urljoin(constants.SITE_URL, element['href'])
    return link
    
        
    
def getModelBasePageUrl(model_first_letter_page_html, model_first_letter_page_url, name):
    element = page.getElementsByConstraint(model_first_letter_page_html, 'a', 'title', name + ' Pictures and Wallpapers')[0]
    url = urllib.parse.urljoin(model_first_letter_page_url, element['href'])
    return url



def get_number_of_pages(model_page_html):
    links = page.getElementsByTagName(model_page_html, 'a')    
    for link in links:
        try:
            if 'prevnext' in link['class'] and link.string.find("Last page") != -1:
                last_page_url = link['href']
                parsed = urllib.parse.urlparse(last_page_url)
                return int(urllib.parse.parse_qs(parsed.query)['page'][0].strip())
        except KeyError:
            pass
    return 1



def get_all_model_urls(url, html):
    pages = get_number_of_pages(html)
    urls = []
    for i in range(1, pages+1):
        urls.append(url + '?page=' + str(i))
    return urls


def getImageRange(model_page_url):
    html = page.getPage(model_page_url)
    pagingstats = page.getElementContent(page.getElementById(html, 'pagingstats'))
    image_range = re.findall('\d+', pagingstats)
    start_image, end_image = int(image_range[0]), int(image_range[1])
    return (start_image, end_image)



def getNumberOfImages(model_last_page_url):
    return getImageRange(model_last_page_url)[1]
    
    
def getImagePageUrls(model_page_url):
    html = page.getPage(model_page_url)
    elements = page.getElementsByConstraint(html, 'a', 'itemprop', 'contentURL')
    image_page_urls = []
    
    for element in elements:
        image_page_url = urllib.parse.urljoin(model_page_url, element['href'])
        image_page_urls.append(image_page_url)
        
    return image_page_urls

def getImageUrl(image_page_url):
    image_page = page.getPage(image_page_url)
    images = page.getElementsByConstraint(image_page, 'img', 'itemprop', 'contentUrl')
    if len(images) > 0:
        image = images[0]
        image_url = urllib.parse.urljoin(image_page_url, image['src'])
    return image_url