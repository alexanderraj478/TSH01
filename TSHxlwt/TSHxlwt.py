import xlwt
from xlwt import Workbook
from TSHFS.TSHFile import TSHFile

class TSHxlwt:
    def __init__(self, filePath):
        self.wbObj = None
        self.wsObj = None
        self.vtshFile = TSHFile()
        self.vtshFile.filePath = filePath
        self.xlsRow = 0
        self.xlsCol = 0
        
    def xxx(self):
        pass
    
    def WSAdd(self, sheetName):
        self.wsObj = self.wbObj.add_sheet(sheetName)

    def WSCellWrite(self, row, col, cellVal):
        self.wsObj.write(row, col, cellVal)
