from TSH.PSHSuite import PSHSuite

class PSHMD:
    PSHSuiteArr = []

#    def DMT(self):
#        self.PSHSuiteArr = []

    def AddSuite(self, suiteName):
        if suiteName in self.PSHSuiteArr:
            print(suiteName)
        else:
            tPSHSuite = PSHSuite(suiteName)
            self.PSHSuiteArr.append (tPSHSuite)

    def ShowSuites(self):
        i = 0
        while (i < len(self.PSHSuiteArr)):
            print(self.PSHSuiteArr[i].GetSuiteName())
            i += 1

    def GetSuite(self, suiteName, createMetadataOnTheFly):
        i = 0
        while (i < len(self.PSHSuiteArr)):
            if (self.PSHSuiteArr[i].GetSuiteName() == suiteName):
                return self.PSHSuiteArr[i]
            i += 1
        if ("yes" == createMetadataOnTheFly):
            self.AddSuite(suiteName)
            return self.PSHSuiteArr[i]
        return None
