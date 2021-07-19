import sys
from TSHGlobal import constants

class TSHTokenizer:
    lineTokArr = []
    lineTokInd = 0
    lineTokTot = 0
    ipFHArr = []
    ipFHInd = -1
    line = ""
    
    def InvalidateLine(self):
        self.lineTokArr = []
        self.lineTokInd = 0
        self.lineTokTot = 0
        
    def TSHMacroRun(self, scriptFileName):
        self.TSHScriptRun(scriptFileName)
    
    def TSHReturn(self):
        if (self.ipFHInd > -1):
            self.ipFHArr[self.ipFHInd].close()
            self.ipFHInd -= 1

    def TSHScriptRun(self, scriptFileName):
        try:
            fh = open(scriptFileName, 'r')
            self.ipFHInd += 1
            self.ipFHArr.insert(self.ipFHInd, fh)
        except FileNotFoundError:
            print("Error opening file")
            pass

    def TSHLineRun(self, line):
        self.line = line
        self.CreateTokenArray()

    def __init__(self):
        self.lineTokArr = []
        self.lineTokInd = 0
        self.lineTokTot = 0
        self.ipFHArr = []
        self.ipFHInd = -1
        self.cmdLine = ""
        self.batchMode = False
    
    def TSHBatchModeSet(self, batchMode):
        self.batchMode = batchMode
        
    def CreateTokenArray(self):
        self.lineTokArr = self.line.split()
        self.lineTokInd = 0
        self.lineTokTot = len(self.lineTokArr)        

    def ReadFromArray(self, *args):
        if ( self.lineTokTot > self.lineTokInd):
            if (len(args) > 0):
                if (args[0] == "on"):
                    token = self.lineTokArr[self.lineTokInd]
                    ind = self.lineTokInd+1
                    while (ind < self.lineTokTot):
                        token = token + " " + self.lineTokArr[ind]
                        ind += 1
                else:
                    token = self.lineTokArr[self.lineTokInd]
                    self.lineTokInd = self.lineTokInd + 1
            else:
                token = self.lineTokArr[self.lineTokInd]
                self.lineTokInd = self.lineTokInd + 1
            return (token)
        else:
            return (None)
        
    def PeekIntoArray(self, peekInd):
        if ( self.lineTokTot > peekInd):
            token = self.lineTokArr[peekInd]
            return (token)
        else:
            return (None)
        
    def ReadNextLine(self):
        inputAvailable = False
        while (False == inputAvailable):
            if (-1 == self.ipFHInd):
                if (True == self.batchMode):
                    return constants.TSHDone
                else:
                    self.line = sys.stdin.readline()
            else:
                self.line = self.ipFHArr[self.ipFHInd].readline()
            
            if (len(self.line) == 0): #eof test
                self.TSHReturn()
                continue
                
            self.line = self.line.strip()
            print(self.line)
            if self.line in (None, ''): #or not myString.strip()
                continue
            else:
                inputAvailable = True
        return constants.TSHNotDone
        
    def GetNextToken(self, *args):
        debug = len(args)
        ercRet = constants.TSHNotDone
        token = self.ReadFromArray(*args)
        if token in (None, ''):  
            ercRet = self.ReadNextLine()
            if (constants.TSHDone != ercRet):
                self.CreateTokenArray()
            else:
                return(None)
            token = self.lineTokArr[self.lineTokInd]
            self.lineTokInd = self.lineTokInd + 1
        else:
            pass
        return (token)
        #print(self.line)
        #return (self.lineTokArr[self.lineTokInd])
