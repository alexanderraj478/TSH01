import copy
from TSHPrint.TSHPrintLst import TSHPrintLst

class TSHDict:
    def __init__(self):
        self.vAss1 = {}
        self.vAss2 = {"k1": "v1", "k2": "v2"}
        pass
    
    def printAss(self):
        print (self.vAss2)
        pass
    
    def printKeys(self):
        for key in (self.vAss2):
            print (key)
        pass
    
    def getKeys(self, oDict):
        return (oDict.keys())
    
    def doesKeyExist(self, oDict, keyName):
        for key in (self.vAss2):
            if (keyName == key):
#                print ("found key:" + keyName)
                return True
        return False
        pass
    
    def doesKeyExist02(self, oDict, keyName):
        #Fruits = {'a': "Apple", 'b':"Banana", 'c':"Carrot"}
        #key_to_lookup = 'a'
        #if Fruits.has_key(key_to_lookup):
        #    print "Key exists"
        #else:
        #    print "Key does not exist"
  
        if oDict.has_key(keyName):
            return True
        else:
            return False
        pass

    def doesKeyExist03(self, oDict, keyName):
        #Fruits = {'a': "Apple", 'b':"Banana", 'c':"Carrot"}
        #key_to_lookup = 'a'
        #if key_to_lookup in Fruits:
        #    print "Key exists"
        #else:
        #    print "Key does not exist"
        if keyName in oDict:
            return True
        else:
            return False
        pass
    
    def getVal(self, oDict, keyName):
        if (True == self.doesKeyExist(oDict, keyName)):
            print ("key{" + keyName + "}=" + oDict[keyName])
        pass
    
    def incr(self, i):
        i += 1
        return (str(i))
    
    #deep copy
    def DictCopy01(self, d1, d2):
        d2 = copy.deepcopy(d1)

    #Copy a dictionary with a for loop
    def DictCopy02(self, d1, d2):
        d2 = {}
        for key in d1:
            d2[key] = d1[key]
    
    #Copy a dictionary with copy()
    def DictCopy03(self, d1, d2):
        d2 = d1.copy()
        
    #Copy a dictionary with dict()
    def DictCopy04(self, d1, d2):
        d2 = dict(d1)
    #Copy a dictionary using the = operator. NOT A REAL COPY!!!
    def DictCopy05(self, d1, d2):
        d2 = d1
  
    def DictKeyLen(self):
        print (len(self.vAss2))
        return 
    
def addition(n): 
    return str(n + n)
 
if (__name__ == "__main__"):
    prtLstObj = TSHPrintLst()
    oDict1 = TSHDict()
    
    oDict1.DictKeyLen()
    
    print(oDict1.getKeys(oDict1.vAss2))    
    keyLst = oDict1.getKeys(oDict1.vAss2)
    
    x = (1,2,3)
    y = ','.join (map(addition, x))
    z = list (y)
    str1 = ""
    w = str1.join(z)
    print(w)
    i = "Eye"
    numbers1 = [1, 2, 3] 
    numbers2 = [4, 5, 6] 
  
    result = map(lambda x, y: x - y, numbers1, numbers2)
    print(list(result))
    result = map(lambda x, y: x + y, numbers1, numbers2) 
    print(list(result))

    #oDict1.printAss()
    #oDict1.printKeys()
    #key = "k2"
    #if (oDict1.doesKeyExist(oDict1.vAss2, key)):
    #    oDict1.getVal(oDict1.vAss2, key)
    