import copy

class TSHObj:
    def __init__(self):
        self.name = None
        self.type = None
        self.val  = None
        self.attrAss = None
    
    @property
    def name(self):
        return (self.__name)
    
    @name.setter
    def name(self, name):
        self.__name = name
        
    @property
    def val(self):
        return (self.__val)
    
    @val.setter
    def val (self, val):
        self.__val = val
    
    @property
    def attrAss(self):
        return (self.__attrAss)
    
    @attrAss.setter
    def attrAss(self, attrAss):
        self.__attrAss = copy.deepcopy(attrAss)
    