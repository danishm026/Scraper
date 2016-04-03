import DBDetails

CREATE_DATABASE_QUERY = 'CREATE DATABASE ' + DBDetails.DATABASE_NAME + ';'
DROP_DATABSE_QUERY = 'DROP DATABASE ' + DBDetails.DATABASE_NAME + ';'

CREATE_MODEL_TABLE_QUERY = '''
                               CREATE TABLE MODEL (
                                   id                int AUTO_INCREMENT,
                                   name              varchar(255),
                                   basePageUrl       varchar(1000),
                                   noOfPages         int,
                                   noOfImages        int,
                                   primary key       (id)
                                );  
                           '''
                           

CREATE_PHOTOS_PER_PAGE_TABLE_QUERY = '''
                                   CREATE TABLE PHOTOS_PER_PAGE (
                                       id                  int,
                                       pageNo              int,
                                       imagesOnpage        int,
                                       startImageNumber    int,
                                       endImageNumber      int
                                    );
                               '''     
                               
CREATE_IMAGE_LINKS_TABLE_QUERY = '''
                                    CREATE TABLE IMAGE_LINKS (
                                        id                int,
                                        imageLink         varchar(1000)
                                    );
                                        
                           '''
                           
INSERT_INTO_MODEL_TABLE_QUERY = '''
                                    INSERT INTO MODEL (name, basePageUrl, noOfpages, noOfimages) VALUES (%s, %s, %s, %s);
                                '''
                                


INSERT_INTO_PHOTOS_PER_PAGE_TABLE_QUERY = '''
                                              INSERT INTO PHOTOS_PER_PAGE VALUES (%s, %s, %s, %s, %s);
                                          '''
                                          

INSERT_INTO_IMAGE_LINKS_TABLE_QUERY = '''
                                              INSERT INTO IMAGE_LINKS VALUES (%s, %s);
                                      '''
                                      
    
GET_MODEL_INFO_BY_NAME_QUERY = '''
                                    SELECT * FROM MODEL WHERE name = %s;
                               ''' 

GET_MODEL_INFO_BY_ID_QUERY = '''
                                    SELECT * FROM MODEL WHERE id = %s;
                             '''
                            
GET_PHOTOS_INFO_BY_ID_QUERY = '''
                                    SELECT * FROM PHOTOS_PER_PAGE WHERE id = %s;
                                    
                              '''

GET_IMAGE_INFO_BY_ID_QUERY = '''
                                SELECT * FROM IMAGE_LINKS WHERE id = %s;
                             '''


