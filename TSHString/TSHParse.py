
class TSHParse:
    SINGLE_QUOTE = "'"
    DOUBLE_QUOTE = '"'
    InSingQuotStr = False
    InDoubQuotStr = False
    stk = []
    def split01(self, word):
        return [char for char in word]

# Python3 program to Split string into characters
    def split02(self, word):
        return list(word)

    def parseStr01(self, str):
        strElArr = self.split01(str)
        print (strElArr)
        pass
    
    def parseStr02(self, str):
        strElArr = self.split02(str)
        strElInd = 0
        strLen = len(str)
        token = ""
        while (strElInd < strLen):
            print(str[strElInd])
            strElInd += 1
            if (self.SINGLE_QUOTE == str[strElInd]):
                if (True == self.InSingQuotStr):
                    if (True == self.InDoubQuotStr):
                        return (-1, token)
                        #not possible
                        pass
                    elif (False == self.InDoubQuotStr):
                        self.InSingQuotStr = True
                        pass
                elif (False == self.InSingQuotStr):
                    if (True == self.InDoubQuotStr):
                        pass
                    elif (False == self.InDoubQuotStr):
                        pass
                
            elif (self.DOUBLE_QUOTE == str[strElInd]):
                if (True == self.InSingQuotStr):
                    if (True == self.InDoubQuotStr):
                        pass
                    elif (False == self.InDoubQuotStr):
                        pass
                elif (False == self.InSingQuotStr):
                    if (True == self.InDoubQuotStr):
                        pass
                    elif (False == self.InDoubQuotStr):
                        self.InDoubQuotStr = True
                        
                        pass
    
            elif (self.SLASH == str[strElInd]):
                if (True == self.InSingQuotStr):
                    if (True == self.InDoubQuotStr):
                        pass
                    elif (False == self.InDoubQuotStr):
                        pass
                elif (False == self.InSingQuotStr):
                    if (True == self.InDoubQuotStr):
                        pass
                    elif (False == self.InDoubQuotStr):
                        pass

            elif (self.BLANK == str[strElInd]):
                if (True == self.InSingQuotStr):
                    if (True == self.InDoubQuotStr):
                        pass
                    elif (False == self.InDoubQuotStr):
                        pass
                elif (False == self.InSingQuotStr):
                    if (True == self.InDoubQuotStr):
                        pass
                    elif (False == self.InDoubQuotStr):
                        pass
            
            elif (self.TAB == str[strElInd]):
                if (True == self.InSingQuotStr):
                    if (True == self.InDoubQuotStr):
                        pass
                    elif (False == self.InDoubQuotStr):
                        pass
                elif (False == self.InSingQuotStr):
                    if (True == self.InDoubQuotStr):
                        pass
                    elif (False == self.InDoubQuotStr):
                        pass
            
            else:
                if (True == self.InSingQuotStr):
                    if (True == self.InDoubQuotStr):
                        return (-1, token)
                        pass
                    elif (False == self.InDoubQuotStr):
                        pass
                elif (False == self.InSingQuotStr):
                    if (True == self.InDoubQuotStr):
                        pass
                    elif (False == self.InDoubQuotStr):
                        pass
                pass
if (__name__ == "__main__"):
    str = "set JSON dump inputStr       '{\"id\":1, \"name\":\"Pankaj\"}'"
    tshParse = TSHParse()
    tshParse.parseStr02(str)