from TSH.PSHPar import PSHPar

class PSHFunc:
    #PSHParArr = []
    #funcName = ""

    def __init__(self, funcName):
        self.PSHParArr = []
        self.funcName = funcName
        self.funcAttrs = {}
        
    def AddPar (self, parName):
        if parName in self.PSHParArr:
            print(parName)
        else:
            tPSHPar = PSHPar(parName)
            self.PSHParArr.append (tPSHPar)

    def GetFuncName(self):
        return self.funcName

    def ShowPars(self):
        i = 0
        while (i < len(self.PSHParArr)):
            print(self.PSHParArr[i].GetParName())
            i += 1

    def GetPar(self, parName, createMetadataOnTheFly):
        i = 0
        while (i < len(self.PSHParArr)):
            if (self.PSHParArr[i].GetParName() == parName):
                return self.PSHParArr[i]
            i += 1
        if ("yes" == createMetadataOnTheFly):
            self.AddPar(parName)
            return self.PSHParArr[i]
        return None