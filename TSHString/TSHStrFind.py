
class TSHStrFind:
#str.find(sub[, start[, end]])

    def __init__(self):
        pass
    
    def format(self):
        pass
        
    def split(self):
        pass
    
    def join(self):
        pass
    
    def strip(self):
        pass
    
    def format_map(self):
        pass
    
    def upper(self):
        pass
    
    def lower(self):
        pass
    
    def replace(self):
        pass

#By using find() method
#By using in operator
#By using count() method
#By using str.index() method
#By using operator.contains() method
#https://www.askpython.com/python/string/check-string-contains-substring-python


    def find01(self):
        
        cellValue = "cALTC001_01b"
        rootName = "ALTC001_01"
        x = cellValue.find(rootName)
        print ("In my string function")
        pass
    
    def find02(self):
        key = "YAML_TSH_TSH_AttributeName01_TSH_AttributeName01"
        partialAttr = "TSH_AttributeName"
        partialAttr = "TSH"
        x = key.find(partialAttr, 0, len(key)-2)

        y = 0
        while (y < len(key)):
            x = key.find(partialAttr, y, len(key))
            y = x + len(partialAttr)
            print (x)
        
    def rfind01(self):
        key = "YAML_TSH_TSH_AttributeName01_"
        print(len(key))
        key = "YAML_TSH_TSH_AttributeName01_TSH_AttributeName01"
        partialAttr = "TSH_AttributeName"
        y = 0
        x = key.rfind(partialAttr, y, len(key))
        
        y = 0
        key = "YAML_TSH_TSH_AttributeName01_TSH_AttributeName01"
        partialAttr = "01"
        print(len(key))
        x = key.rfind(partialAttr, y, len(key))
        pass
    
    def translate(self):
        pass
    
    def CallAppRegisteredFunction(self, padStr, MwareKeyAss, MwareDatAss, dataVal):
        AttributeNameAttr = self.mdKey + "_TSH_AttributeName"
        DataTypeAttr = self.mdKey + "_TSH_DataType"
        TabAttr = self.mdKey + "_TSH_Tab"
        
        AttributeNameCol = -1
        DataTypeCol = -1
        TabCol = -1

        for key in (MwareKeyAss):
            #print("MDNode:MwareKeyAss:" + str(key) + ":" + MwareKeyAss[key])
            val = MwareKeyAss[key]
            
            x = val.rfind(AttributeNameAttr, 0, len(val))
            if (-1 != x):
                AttributeNameCol = key

            x = val.rfind(DataTypeAttr, 0, len(val))
            if (-1 != x):
                DataTypeCol = key
                    
            x = val.rfind(TabAttr, 0, len(val))
            if (-1 != x):
                TabCol = key
                
        print(padStr + str(MwareDatAss[AttributeNameCol]) + ": " + str(dataVal))
        pass
    
    
    def pHW(self):
        print("Hello World from funcPtr")
        
    def rfind03(self):
        val = "YAML:TSH:AttributeName:v1"
        AttributeNameAttr = ":TSH:AttributeName:v1"
        x = val.rfind(AttributeNameAttr, len(val) - len(AttributeNameAttr), len(val))
        print (x)
        
        x = val.rfind(AttributeNameAttr)
        print (x)
    
if __name__ == "__main__":
    o = TSHStrFind()
    o.rfind03()
    