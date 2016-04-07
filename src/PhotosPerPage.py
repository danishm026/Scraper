class PhotosPerPage:
    def __init__(self):
        self.__id = 0
        self.__pageNo = 0
        self.__imagesOnPage = 0
        self.__starImageNumber = 0
        self.__endImageNumber = 0
        
    def GetId(self):
        return self.__id
    
    def GetPageNo(self):
        return self.__pageNo
    
    def GetImagesOnpage(self):
        return self.__imagesOnPage
    
    def GetStartImageNumber(self):
        return self.__starImageNumber
    
    def GetEndeImageNumber(self):
        return self.__endImageNumber
    
    def SetId(self, id):
        self.__id = id
        
    def SetPageNo(self, pageNo):
        self.__pageNo = pageNo
    
    def SetImagesOnpage(self, imageOnPage):
        self.__imagesOnPage = imageOnPage
    
    def SetStartImageNumber(self, startImageNumber):
        self.__starImageNumber = startImageNumber
    
    def SetEndImageNumber(self, endImageNumber):
        self.__endImageNumber = endImageNumber
    





