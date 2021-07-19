from TSH.PSHFunc import PSHFunc

class PSHSuite:
    #PSHFuncArr = []
    #suiteName = ""
    #className = ""

    
    def __init__(self, suiteName):
        self.PSHFuncArr = []
        self.suiteName = suiteName
        self.suiteAttrs = {}
    def AddFunc (self, funcName):
        if funcName in self.PSHFuncArr:
            print(funcName)
        else:
            tPSHFunc = PSHFunc(funcName)
            self.PSHFuncArr.append (tPSHFunc)

    def GetSuiteName(self):
        return self.suiteName

    def ShowFuncs(self):
        i = 0
        while (i < len(self.PSHFuncArr)):
            print(self.PSHFuncArr[i].GetFuncName())
            i += 1

    def GetFunc(self, funcName, createMetadataOnTheFly):
        i = 0
        while (i < len(self.PSHFuncArr)):
            if (self.PSHFuncArr[i].GetFuncName() == funcName):
                return self.PSHFuncArr[i]
            i += 1
        if ("yes" == createMetadataOnTheFly):
            self.AddFunc(funcName)
            return self.PSHFuncArr[i]
        return None

    def AddClass(self, className):
        self.className = className
