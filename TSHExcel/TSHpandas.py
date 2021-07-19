import pandas as pd

class TSHpandas:
    def __init__(self):
        self.wb = None
        self.aws = None
        
    def GetSheetsInfo(self, file_path):
        self.wb = pd.ExcelFile(file_path)
        sheets = self.wb.sheet_names
        return sheets
    
        
    def ExcelWriter(self):
        writer = pd.ExcelWriter('demo.xlsx', engine='xlsxwriter')
        writer.save()
        
    def TSHcreate_sheet(self):
        self.wb.create_sheet(title=None, index=None)
        
    def TSHget_index(self, ws):
        self.wb.get_index(ws)
        
    def TSHremove(self, ws):
        self.wb.remove(ws)
    
    def TSHactive(self):
        self.aws = self.wb.active