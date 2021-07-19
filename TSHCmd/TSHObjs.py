from TSHTDM.DataNode1D import DataNode1D
class TSHObjs:
    def __init__(self):
        self.name = None
        self.DataNode1D = DataNode1D()
        pass
    
    @property
    def name(self):
        return(self.__name)
    
    @name.setter
    def name(self, name):
        self.__name = name
        
    def AddObj(self, tshObj):
        
        tshObjTot = self.DataNode1D.GetDataNode1DLen()
        for tshObjInd in range (tshObjTot):
            print (tshObjInd)
            tshObj1 = self.DataNodeID.GetDataNode(tshObjInd)
            if (tshObj.name == tshObj1.name):
                self.DataNodeID.ReplaceDataNode(tshObjInd, tshObj)
            else:
                self.DataNodeID.AddDataNode(tshObj)
            
    