class ImageLinks:
    def __init__(self):
        self.__id = 0
        self.__imageLinks = []
        
    def GetId(self):
        return self.__id
    
    def GetImageLinks(self):
        return self.__imageLinks
    
    def SetId(self, id):
        self.__id = id
        
    def SetImageLinks(self, imageLinks):
        self.__imageLinks = imageLinks