import pymysql
import DBDetails
import DBQueries
from Model import Model

def getModelByName(name):
    connection = pymysql.connect(DBDetails.DATABASE_URL, DBDetails.USER, DBDetails.PASSWORD, DBDetails.DATABASE_NAME)
    cur = connection.cursor()
    cur.execute(DBQueries.GET_MODEL_INFO_BY_NAME_QUERY, (name))
    row = cur.fetchone()
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
    cur.execute(DBQueries.INSERT_INTO_PHOTOS_PER_PAGE_TABLE_QUERY)
    
    connection.commit()
    connection.close()
        
if __name__ == '__main__':
    mod = getModelByName('danish')
    print(mod.GetId(), mod.GetBasePageUrl(), mod.GetNoOfPages())
    model = Model()
    model.SetName('holly')
    model.SetBasePageUrl('base')
    model.SetNoOfPages(3)
    model.SetNoOfImages(451)
    save(model, None, None)
    
    