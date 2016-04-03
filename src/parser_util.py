import constants
from page import getPage
from bs4 import BeautifulSoup
import urllib.parse
import sys


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



def getLetterLink(html, letter):
    prefix = 'Pictures of Celebritries starting with '
    
    element = getElementsByConstraint(html, 'a', 'title', prefix + letter)[0]
    link = urllib.parse.urljoin(constants.SITE_URL, element['href'])
    return link
    
        
    
def getModelPage(letter_page_html, letter_page_link, name):
    element = getElementsByConstraint(letter_page_html, 'a', 'title', name + ' Pictures and Wallpapers')[0]
    link = urllib.parse.urljoin(letter_page_link, element['href'])
    return link



def getElementsByTagName(html, tag):
    document = BeautifulSoup(html, 'html.parser')
    return document.find_all(tag)



def number_of_pages(model_page_html):
    links = getElementsByTagName(model_page_html, 'a')    
    for link in links:
        try:
            if 'prevnext' in link['class'] and link.string.find("Last page") != -1:
                last_page_url = link['href']
                parsed = urllib.parse.urlparse(last_page_url)
                return int(urllib.parse.parse_qs(parsed.query)['page'][0].strip())
        except KeyError:
            pass
    return 1



def get_all_urls_for_model(url, html):
    pages = number_of_pages(html)
    urls = []
    for i in range(1, pages+1):
        urls.append(url + '?page=' + str(i))
    return urls



def print_picture_links(urls):
    for url in urls:
        page = getPage(url)    
        elements = getElementsByConstraint(page, 'a', 'itemprop', 'contentURL')
        for element in elements:
            image_page_link = urllib.parse.urljoin(url, element['href'])
            image_page = getPage(image_page_link)
            if image_page != None:
                images = getElementsByConstraint(image_page, 'img', 'itemprop', 'contentUrl')
                if len(images) > 0:
                    image = images[0]
                    image_link = urllib.parse.urljoin(image_page_link, image['src'])
                    print(image_link)
                    sys.stdout.flush()
                else:
                    print('No img tag with property "itemprop"="contentUrl" for URL:' + image_page_link, file=sys.stderr)
    