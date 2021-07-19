from TSHExcel.TSHopenpyxl import TSHopenpyxl #TSHopenpyxl
from TSHGlobal import constants

class test:
    def __init__(self, file_path):
        self.file_path = file_path
    
#    def PrintMsg(self, msg, paramLst):
#        print (msg, paramLst)
    
    def alex(self):
        pass
    
    def test1(self):
        self.alex()
        aws = None
        top = TSHopenpyxl()
        invalid_file_path = "foobar.xls"
        valid_file_path = "/home/alex/learn/python/data/xls/yaml05.xlsm"
        top.Initialize(valid_file_path)
        #top.load_workbook(self.file_path)
        if (None != top.load_workbook()):
            top.workbookActiveSheetSet("S3")
            top.get_sheetObj("S2")
            
        #print(top.get_sheetnames())
        #print(top.get_worksheets())
        #aws = top.get_worksheets()[1]
            
            aws = top.get_sheetObj("foobar")
            if (0):
                #constants.PrintMsg1("Error: %d:%s" %(-1, constants.TSHFailDict["-1"]))
                constants.PrintMsg1("Error: %d:%s", (-1, constants.TSHFailDict["-1"]))
                my_string = "gvjhh The value in cell C4={} and C5={}"
                constants.PrintMsg2("msg3 The value in cell C4={} and C5={}", (aws['C4'].value, aws['C5'].value))            
                constants.PrintMsg3("msg2 The value in cell C4={} and C5={}".format(aws['C4'].value, aws['C5'].value))
            print(aws)
        pass
    

t = test("/home/alex/learn/python/data/xls/yaml03.xlsm")
t.test1()

