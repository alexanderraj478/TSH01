from TSHTDM.DataNode2D import DataNode2D
from .DataNode2D import DataNode2D

class DataNode:
    #m_DataNode1D = None
    
    def __init__(self, dataVal):
        self.dataVal = None
        self.objType = 1
        #self.m_DataNode2D = [] #???
        self.dataVal = dataVal
        self.m_DataNode2D = DataNode2D()
            
    @property
    def NoneNode(self):
        return self.__NoneNode
    
    @NoneNode.setter
    def NoneNode(self, NoneNode):
        self.__NoneNode = NoneNode
    def SetDataVal(self, dataVal):
        self.dataVal = dataVal
        
    def GetDataVal(self):
        return (self.dataVal)
    
    def DispObjVal(self, padStr, MDAttributeName):
        if (self.dataVal is None):
            opStr = padStr+MDAttributeName+"=None"
            #print(opStr)
        else:
            opStr = padStr+MDAttributeName+"="+str(self.dataVal)
            #print(opStr)
        return (opStr)
        
    def GetDataType(self):
        return ("UD")

    def GetDataNode2D(self):
        return (self.m_DataNode2D)
    
    def SumChildCount(self):
        count = 0
        dNode2DTot = self.GetDataNode2D().GetDataNode2DLen()
        for dNode2DInd in range(dNode2DTot):
            dNode1DTot = self.GetDataNode2D().GetDataNode1D(dNode2DInd).GetDataNode1DLen()
            for dNode1DInd in range(dNode1DTot):
                dNode = self.GetDataNode2D().GetDataNode1D(dNode2DInd).GetDataNode(dNode1DInd)
                dataVal = dNode.GetDataVal()
                if (None == dataVal):
                    count += dNode.SumChildCount()
                    pass
                elif (None != dataVal):
                    count += 1
                    pass
                pass
            pass
        return count
        pass        
    
