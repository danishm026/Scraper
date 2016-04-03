class Model:
    def __init__(self):
        self.__id = 0
        self.__name = ''
        self.__basePageUrl = ''
        self.__noOfPages = 0
        self.__noOfImages = 0
        
    def GetId(self):
        return self.__id
    
    def GetName(self):
        return self.__name
    
    def GetBasePageUrl(self):
        return self.__basePageUrl
    
    def GetNoOfPages(self):
        return self.__noOfPages
    
    def GetNoOfImages(self):
        return self.__noOfImages
    
    def SetId(self, id):
        self.__id = id
    
    def SetName(self, name):
        self.__name = name
        
    def SetBasePageUrl(self, basePageUrl):
        self.__basePageUrl = basePageUrl
        
    def SetNoOfPages(self, noOfPages):
        self.__noOfPages = noOfPages
        
    def SetNoOfImages(self, noOfImages):
        self.__noOfImages = noOfImages
        
        
        
