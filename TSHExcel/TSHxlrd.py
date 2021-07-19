import xlrd as tshwb

class TSHxlrd:
    def GetSheetsInfo(self, file_path):
        xls = tshwb.open_workbook(file_path)
        sheets = xls.sheet_names()
        return sheets

#xls = xlrd.open_workbook(r'<path_to_your_excel_file>', on_demand=True)
#print xls.sheet_names() # <- remeber: xlrd sheet_names is a function, not a property
        


