import links
import sys
import constants
import string_util
import page
from Model import Model
from PhotosPerPage import PhotosPerPage
from ImageLinks import ImageLinks
import ScraperDAO


if __name__ == '__main__':
    
    model = Model()
    photosPerPageList = []
    imageLinks = ImageLinks()
    
    print('Enter Name: ', end='', file=sys.stderr)
    name = string_util.sanitize(input())
    
    '''savedModel = ScraperDAO.getModelByName(name)
    if(savedModel != None):
        modelId = savedModel.GetId()
        savedImageLinks = ScraperDAO.getImageLinksById(modelId)
        
        for link in savedImageLinks:
            print(link)
        return 
    '''
    #Set Model name in model object
    model.SetName(name)
    
    #Get Home Page
    home_page_html = page.getPage(constants.SITE_URL)
    
    #Get Letter Page Link
    model_first_letter_page_url = links.getLetterLink(home_page_html, name[0]) 
    model_first_letter_page_html = page.getPage(model_first_letter_page_url)
    
    #Get Model Base Page and set in model Object
    model_base_page_url = links.getModelBasePageUrl(model_first_letter_page_html, model_first_letter_page_url, name)
    model.SetBasePageUrl(model_base_page_url)
    model_base_page_html = page.getPage(model_base_page_url)
    
    
    #Get Number of Pages and Set in model ObjectAll Model URLs
    number_of_pages = links.get_number_of_pages(model_base_page_html)
    model.SetNoOfPages(number_of_pages)
    
    #Get All Model URLs
    model_page_urls = links.get_all_model_urls(model_base_page_url, model_base_page_html)
    
    #Get Number Of Images and set in model Object
    number_of_images = links.getNumberOfImages(model_page_urls[-1])
    model.SetNoOfImages(number_of_images)
    
    #Set PhotosPerPage details
    pageNo = 1
    for model_page_url in model_page_urls:
        photosPerPage = PhotosPerPage()
        photosPerPage.SetPageNo(pageNo)
        startImageNumber, endImageNumber = links.getImageRange(model_page_url)
        photosPerPage.SetStartImageNumber(startImageNumber)
        photosPerPage.SetEndeImageNumber(endImageNumber)
        photosPerPage.SetImagesOnpage(endImageNumber - startImageNumber + 1)
        photosPerPageList.append(photosPerPage)
        pageNo += 1
        
    #Get Image Page URLs
    image_page_urls = []
    for model_page_url in model_page_urls:
        temp = links.getImagePageUrls(model_page_url)
        image_page_urls.extend(temp)
    
    #Get Image URLs
    image_urls = []
    for url in image_page_urls:
        image_urls.append(links.getImageUrl(url))
        print(image_urls[-1])
    
    #Set Image Links in imageLinks Object
    imageLinks.SetImageLinks(image_urls)
    
    #Save in DB
    ScraperDAO.save(model, photosPerPageList, imageLinks)
    
    
    