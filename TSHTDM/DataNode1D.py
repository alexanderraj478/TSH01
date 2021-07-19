class DataNode1D:
    def __init__(self):
        self.m_DataNode1D = []
        
    @property
    def NoneNode(self):
        return self.__NoneNode
    
    @NoneNode.setter
    def NoneNode(self, NoneNode):
        self.__NoneNode = NoneNode
    
    
    def AddDataNode(self, DataNode):
        self.m_DataNode1D.append (DataNode)
        return len(self.m_DataNode1D)
    
    def ReplaceDataNode(self, DataNode1DInd, DataNode):
        if (DataNode1DInd < len(self.m_DataNode1D)):
            self.m_DataNode1D[DataNode1DInd] = DataNode
            
    def GetDataNode(self, DataNode1DInd):
        if (DataNode1DInd < len(self.m_DataNode1D)):
            return(self.m_DataNode1D[DataNode1DInd])
        else:
            print("Incorrect Index value:" + str(DataNode1DInd))
            print("Needs to less than:" + str(len(self.m_DataNode1D)))
            return None
    
    def GetLastDataNode(self):
        return self.m_DataNode1D[self.GetDataNode1DLen()-1]
    
    def GetDataNode1D(self):
        return (self.m_DataNode1D)
    
    def GetDataNode1DLen(self):
        return len(self.m_DataNode1D)
    
    def ShowDataVals(self, methodToRun):
        i = 0
        while (i < len(self.m_DataNode1D)):
            methodToRun.call()
            #print(self.m_DataNode1D[i].GetDataVal())
            i += 1
            
            
            
