class TSHLst:
    def __init__(self):
        self.lst = []
        pass
            
    def insert(self, val, ind):
        self.lst.insert(val, ind)
        pass
    
    def append(self, val):
        self.lst.append(val)
        pass
    
    def printLst01(self):
        print(self.lst)
        
    def printLst02(self):
        for ind in range(len(self.lst)):
            print(self.lst[ind])
            

if ( __name__ == '__main__'):
    tshLst = TSHLst()
    for val in range (10):
        print(val)
        tshLst.insert(0, val)
    print(tshLst.printLst01())
    print("----------")

    tshLst1 = TSHLst()
    for val in range (10):
        print(val)
        tshLst1.append(val)
    print(tshLst1.printLst01())
    print("----------")
