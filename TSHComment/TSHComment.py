        #S MB ME
        #0  0  0 Error. We need at least single comment for MD. Hence Error condition
        #0  0  1 Error. Should have MB and ME
        #0  1  0 Error. Should have MB and ME
        #0  1  1 Error. This is possible given both each column value will be checked for MB and ME. But Not supporting it
        #1  0  0 Valid
        #1  0  1 Error. Same as 1
        #1  1  0 Error. Same as 2
        #1  1  1 Valid

class TSHComment:
    def __init__(self):
        self.singCommentPat = None
        self.multCommentBegPat = None
        self.multCommentEndPat = None
        
        self.singComment = False
        self.multComment = False
        self.multCommentBeg = False
        self.multCommentEnd = False        
        pass
    
    @property
    def singCommentPat(self):
        return self.__singCommentPat
    
    @singCommentPat.setter
    def singCommentPat(self, singCommentPat):
        self.__singCommentPat = singCommentPat
    #------------------------------------------------
    @property
    def multCommentBegPat(self):
        return self.__multCommentBegPat
    
    @multCommentBegPat.setter
    def multCommentBegPat(self, multCommentBegPat):
        self.__multCommentBegPat = multCommentBegPat
    #------------------------------------------------    
    @property
    def multCommentEndPat(self):
        return self.__multCommentEndPat
    
    @multCommentEndPat.setter
    def multCommentEndPat(self, multCommentEndPat):
        self.__multCommentEndPat = multCommentEndPat
    #------------------------------------------------
    def isAComment(self, cmdToken):
        self.singComment = False
        if (    (None == cmdToken)
            or  ("" == cmdToken)):
            if (True == self.multCommentBeg):
                return (0)
            else:
                return (0)
        else:
            cmdTokenOff = cmdToken.find(self.singCommentPat)
            if (0 == cmdTokenOff):
                self.singComment = True
            
            cmdTokenOff = cmdToken.find(self.multCommentBegPat)
            if (0 == cmdTokenOff):
                if (True == self.multCommentBeg):
                    print("Error: Already inside a comment")
                    self.multComment = False
                    self.multCommentBeg = False
                    self.multCommentEnd = False
                    return (-1)
                else:
                    self.multComment = True
                    self.multCommentBeg = True
            
                 
            cmdTokenOff = cmdToken.rfind(self.multCommentEndPat)
            if (-1 != cmdTokenOff):
                if (len(self.multCommentEndPat) == len(cmdToken) - cmdTokenOff):
                    if (True == self.multCommentBeg):
                        self.multComment = True
                        self.multCommentEnd = True
                    else:
                        print("Error: End comment encountered without a Begin comment")
                        self.multComment = False
                        self.multCommentBeg = False
                        self.multCommentEnd = False
                        return (-1)

        if (True == self.singComment) and (True == self.multComment):
                print("Error: Please don't mix single row and multiple row comments")
                self.singComment = False
                self.multComment = False
                self.multCommentBeg = False
                self.multCommentEnd = False
                return (-1)
        elif (True == self.singComment) or (True == self.multComment):
            return (0)
        else:
            return (0)

    def ProcessCommentStatus(self):
        ercRet = 0 #0 = False 1=True -1=Error
        if (ercRet == -1):
                return ercRet    
        if (True == self.multCommentBeg):
            if (True == self.multCommentEnd):
                if (True == self.multComment):
                    self.multCommentBeg = False
                    self.multCommentEnd = False
                    self.multComment = False
                    ercRet = 1
                elif (False == self.multComment):
                    ercRet = -1
            elif (False == self.multCommentEnd):
                if (True == self.multComment):
                    ercRet = 1
                elif (False == self.multComment):
                    ercRet = -1          
        elif (False == self.multCommentBeg):
            if (True == self.multCommentEnd):
                if (True == self.multComment):
                    ercRet = -1             
                elif (False == self.multComment):
                    ercRet = -1                   
            elif (False == self.multCommentEnd):
                if (True == self.multComment):
                    ercRet = -1                   
                elif (False == self.multComment):
                    ercRet = 0
        if (0 == ercRet):
            if (True == self.singComment):
                ercRet = 1
            elif (False == self.singComment):
                ercRet = 0
                
        return ercRet