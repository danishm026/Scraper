import pymysql
import DBDetails
import DBQueries
from Model import Model
from PhotosPerPage import PhotosPerPage
from ImageLinks import ImageLinks

def getModelByName(name):
    connection = pymysql.connect(DBDetails.DATABASE_URL, DBDetails.USER, DBDetails.PASSWORD, DBDetails.DATABASE_NAME)
    cur = connection.cursor()
    cur.execute(DBQueries.GET_MODEL_INFO_BY_NAME_QUERY, (name))
    row = cur.fetchone()
    if row == None:
        return None
    model = Model()
    model.SetId(row[0])
    model.SetName(row[1])
    model.SetBasePageUrl(row[2])
    model.SetNoOfPages(row[3])
    model.SetNoOfImages(row[4])
    connection.close()
    return model
    
def getImageLinksById(id):
    connection = pymysql.connect(DBDetails.DATABASE_URL, DBDetails.USER, DBDetails.PASSWORD, DBDetails.DATABASE_NAME)
    cur = connection.cursor()
    cur.execute(DBQueries.GET_IMAGE_INFO_BY_ID_QUERY, (int(id)))
    imageLinks = []
    rows = cur.fetchall()
    for row in rows:
        imageLinks.append(row[1])
    connection.close()
    return imageLinks 
    
    
    
def save(model, photosPerPageList, imageLinks):
    connection = pymysql.connect(DBDetails.DATABASE_URL, DBDetails.USER, DBDetails.PASSWORD, DBDetails.DATABASE_NAME)
    cur = connection.cursor()
    cur.execute(DBQueries.INSERT_INTO_MODEL_TABLE_QUERY, (model.GetName(), model.GetBasePageUrl(), int(model.GetNoOfPages()), int(model.GetNoOfImages())))
    connection.commit()
    modelId = getModelByName(model.GetName()).GetId()
    for pageDetail in photosPerPageList:
        cur.execute(DBQueries.INSERT_INTO_PHOTOS_PER_PAGE_TABLE_QUERY, (int(modelId), int(pageDetail.GetPageNo()), int(pageDetail.GetImagesOnpage()), int(pageDetail.GetStartImageNumber()), int(pageDetail.GetEndeImageNumber())))
    links = imageLinks.GetImageLinks()
    for link in links:
        cur.execute(DBQueries.INSERT_INTO_IMAGE_LINKS_TABLE_QUERY, (int(modelId), link))
    connection.commit()
    connection.close()
        
    