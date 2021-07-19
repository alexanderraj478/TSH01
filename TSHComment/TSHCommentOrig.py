from _ast import Or
        #S MB ME
        #0  0  0 Error. We need at least single comment for MD. Hence Error condition
        #0  0  1 Error. Should have MB and ME
        #0  1  0 Error. Should have MB and ME
        #0  1  1 Error. This is possible given both each column value will be checked for MB and ME. But Not supporting it
        #1  0  0 Valid
        #1  0  1 Error. Same as 1
        #1  1  0 Error. Same as 2
        #1  1  1 Valid

class TSHCommentOrig:
    def __init__(self):
        self.singRowCommentPat = None
        self.multRowCommentBegPat = None
        self.multRowCommentEndPat = None
        
        self.singRowComment = False
        self.multRowComment = False
        self.multRowCommentBeg = False
        self.multRowCommentEnd = False

        self.singColCommentPat = None
        self.multColCommentBegPat = None
        self.multColCommentEndPat = None
        
        self.singColComment = False
        self.multColComment = False
        self.multColCommentBeg = False
        self.multColCommentEnd = False
        
        pass
    
    @property
    def singRowCommentPat(self):
        return self.__singRowCommentPat
    
    @singRowCommentPat.setter
    def singRowCommentPat(self, singRowCommentPat):
        self.__singRowCommentPat = singRowCommentPat
    #------------------------------------------------
    @property
    def multRowCommentBegPat(self):
        return self.__multRowCommentBegPat
    
    @multRowCommentBegPat.setter
    def multRowCommentBegPat(self, multRowCommentBegPat):
        self.__multRowCommentBegPat = multRowCommentBegPat
    #------------------------------------------------    
    @property
    def multRowCommentEndPat(self):
        return self.__multRowCommentEndPat
    
    @multRowCommentEndPat.setter
    def multRowCommentEndPat(self, multRowCommentEndPat):
        self.__multRowCommentEndPat = multRowCommentEndPat
    #------------------------------------------------
    @property
    def singColCommentPat(self):
        return self.__singColCommentPat
    
    @singColCommentPat.setter
    def singColCommentPat(self, singColCommentPat):
        self.__singColCommentPat = singColCommentPat
    #------------------------------------------------ 
    @property
    def multColCommentBegPat(self):
        return self.__multColCommentBegPat
    
    @multColCommentBegPat.setter
    def multColCommentBegPat(self, multColCommentBegPat):
        self.__multColCommentBegPat = multColCommentBegPat
    #------------------------------------------------
    @property
    def multColCommentEndPat(self):
        return self.__multColCommentEndPat
    
    @multColCommentEndPat.setter
    def multColCommentEndPat(self, multColCommentEndPat):
        self.__multColCommentEndPat = multColCommentEndPat
    #------------------------------------------------
    def isARowComment(self, cmdToken):
        self.singRowComment = False
        if (    (None == cmdToken)
            or  ("" == cmdToken)):
            if (True == self.multRowCommentBeg):
                return (0)
            else:
                return (0)
        else:
            cmdTokenOff = cmdToken.find(self.singRowCommentPat)
            if (0 == cmdTokenOff):
                self.singRowComment = True
            
            cmdTokenOff = cmdToken.find(self.multRowCommentBegPat)
            if (0 == cmdTokenOff):
                if (True == self.multRowCommentBeg):
                    print("Error: Already inside a comment")
                    self.multRowComment = False
                    self.multRowCommentBeg = False
                    self.multRowCommentEnd = False
                    return (-1)
                else:
                    self.multRowComment = True
                    self.multRowCommentBeg = True
            
                 
            cmdTokenOff = cmdToken.rfind(self.multRowCommentEndPat)
            if (-1 != cmdTokenOff):
                if (len(self.multRowCommentEndPat) == len(cmdToken) - cmdTokenOff):
                    if (True == self.multRowCommentBeg):
                        self.multRowComment = True
                        self.multRowCommentEnd = True
                    else:
                        print("Error: End comment encountered without a Begin comment")
                        self.multRowComment = False
                        self.multRowCommentBeg = False
                        self.multRowCommentEnd = False
                        return (-1)

        if (True == self.singRowComment) and (True == self.multRowComment):
                print("Error: Please don't mix single row and multiple row comments")
                self.singRowComment = False
                self.multRowComment = False
                self.multRowCommentBeg = False
                self.multRowCommentEnd = False
                return (-1)
        elif (True == self.singRowComment) or (True == self.multRowComment):
            return (0)
        else:
            return (0)

    def ProcessRowCommentStatus(self):
        ercRet = 0 #0 = False 1=True -1=Error
        if (ercRet == -1):
                return ercRet    
        if (True == self.multRowCommentBeg):
            if (True == self.multRowCommentEnd):
                if (True == self.multRowComment):
                    self.multRowCommentBeg = False
                    self.multRowCommentEnd = False
                    self.multRowComment = False
                    ercRet = 1
                elif (False == self.multRowComment):
                    ercRet = -1
            elif (False == self.multRowCommentEnd):
                if (True == self.multRowComment):
                    ercRet = 1
                elif (False == self.multRowComment):
                    ercRet = -1                   
        elif (False == self.multRowCommentBeg):
            if (True == self.multRowCommentEnd):
                if (True == self.multRowComment):
                    ercRet = -1                   
                elif (False == self.multRowComment):
                    ercRet = -1                   
            elif (False == self.multRowCommentEnd):
                if (True == self.multRowComment):
                    ercRet = -1                   
                elif (False == self.multRowComment):
                    ercRet = 0
        if (0 == ercRet):
            if (True == self.singRowComment):
                ercRet = 1
            elif (False == self.singRowComment):
                ercRet = 0
                
        return ercRet

    def isAColComment(self, cmdToken):
        self.singColComment = False        
        if (    (None == cmdToken)
            or  ("" == cmdToken)):
            if (True == self.multColCommentBeg):
                #self.multColComment = True
                return (0)
            else:
                self.multColComment = False
                self.multColCommentEnd = False
                return (0)
        else:
            cmdTokenOff = cmdToken.find(self.singColCommentPat)
            if (0 == cmdTokenOff):
                self.singColComment = True
                
            cmdTokenOff = cmdToken.find(self.multColCommentBegPat)
            if (0 == cmdTokenOff):
                if (True == self.multColCommentBeg):
                    print("Error: Already inside a comment")
                    self.multColComment = False
                    self.multColCommentBeg = False
                    self.multColCommentEnd = False
                    return (-1)
                else:
                    self.multColComment = True
                    self.multColCommentBeg = True
            
                 
            cmdTokenOff = cmdToken.rfind(self.multColCommentEndPat)
            if (-1 != cmdTokenOff):
                if (len(self.multColCommentEndPat) == len(cmdToken) - cmdTokenOff):
                    if (True == self.multColCommentBeg):
                        self.multColComment = True
                        self.multColCommentEnd = True
                    else:
                        print("Error: End comment encountered without a Begin comment")
                        self.multColComment = False
                        self.multColCommentBeg = False
                        self.multColCommentEnd = False
                        return (-1)

        if (True == self.singColComment) and (True == self.multColComment):
                print("Error: Please don't use single column comment in multiple column comments")
                self.singColComment = False
                self.multColComment = False
                self.multColCommentBeg = False
                self.multColCommentEnd = False
                return (-1)
        elif (True == self.singColComment) or (True == self.multColComment):
            return (0)
        else:
            return (0)
        
    def ProcessColCommentStatus(self):
        ercRet = 0 #0 = False 1=True -1=Error
        if (ercRet == -1):
                return ercRet    
        if (True == self.multColCommentBeg):
            if (True == self.multColCommentEnd):
                if (True == self.multColComment):
                    self.multColCommentBeg = False
                    self.multColCommentEnd = False
                    self.multColComment = False
                    ercRet = 1
                elif (False == self.multColComment):
                    ercRet = -1
            elif (False == self.multColCommentEnd):
                if (True == self.multColComment):
                    ercRet = 1
                elif (False == self.multColComment):
                    ercRet = -1                   
        elif (False == self.multColCommentBeg):
            if (True == self.multColCommentEnd):
                if (True == self.multColComment):
                    ercRet = -1                   
                elif (False == self.multColComment):
                    ercRet = -1                   
            elif (False == self.multColCommentEnd):
                if (True == self.multColComment):
                    ercRet = -1                   
                elif (False == self.multColComment):
                    ercRet = 0
        if (0 == ercRet):
            if (True == self.singColComment):
                ercRet = 1
            elif (False == self.singColComment):
                ercRet = 0
                
        return ercRet
