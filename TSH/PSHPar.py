class PSHPar:
    #parName = ""
    #parVal = ""
    
    def __init__(self, parName):
        self.parName = parName
        self.parVal = ""
        self.parAttrs = {}
        
    def GetParName(self):
        return self.parName
    
    def SetParVal(self, parVal):
        if ("None" == parVal):
            parVal = None
        self.parVal = parVal
        
    def GetParVal(self):
        return self.parVal
