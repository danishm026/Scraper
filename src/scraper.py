import parser_util
import sys
import constants
import string_util

from page import getPage

if __name__ == '__main__':
    print('Enter Name: ', end='', file=sys.stderr)
    name = string_util.sanitize(input())
    
    
    #Get Home Page
    home_page_html = getPage(constants.SITE_URL)
    
    #Get Model First Letter Page
    letter_page_link  = parser_util.getLetterLink(home_page_html, name[0])
    letter_page_html = getPage(letter_page_link)
    
    #Get Model Page
    model_page_link = parser_util.getModelPage(letter_page_html, letter_page_link, name)
    model_page_html = getPage(model_page_link)
  
    #get All Model Page URLs  
    model_page_urls = parser_util.get_all_urls_for_model(model_page_link, model_page_html)

    parser_util.print_picture_links(model_page_urls)
    
    print('Done...', file=sys.stderr)