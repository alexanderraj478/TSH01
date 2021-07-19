#https://www.askpython.com/python/examples/add-a-newline-character-in-python
from TSHGlobal.constants import *
class TSHSTRJoin:
    def PrintStr01(self, str):
        print(str)
    
    def PrintLst01(self):
        print(xsltLst)
        
    def PrintLst02(self):
        xsltStrTmp = '\n'.join(xsltLst)
        print(xsltStrTmp)
    
    def ReadFile(self, ):
        with open("/home/alex/test/file.txt", "r") as f:
            print(f.readlines())

    def WriteFile(self):
        name = "/home/alex/test/file.txt"
        mode = "w"
        fh = open(name, mode)
        fh.write(xsltStr03)
        fh.close()
        pass

tshSTRJoin = TSHSTRJoin()

tshSTRJoin.PrintStr01(xsltStr01)
print("")
tshSTRJoin.PrintStr01(xsltStr02)
print("")
tshSTRJoin.PrintStr01(xsltStr03)
print("")

tshSTRJoin.PrintLst01()
print("")
tshSTRJoin.PrintLst02()
print("---------")
tshSTRJoin.WriteFile()
print("---------")
tshSTRJoin.ReadFile()
print("---------")
