class TSHString:
    def __init__(self):
        self.vStr = None
        
    def TSHIntToStr(self):
        pass
    
    @property
    def vStr(self):
        """Get value of radius"""
        return self._vStr

    @vStr.setter
    def vStr(self, value):
        self._vStr = value
    
