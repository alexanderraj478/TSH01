from TSHTDM.DataNode1D import DataNode1D

class DataNode2D:  
    def __init__(self):
        self.m_DataNode2D = []

    @property
    def NoneNode(self):
        return self.__NoneNode
    
    @NoneNode.setter
    def NoneNode(self, NoneNode):
        self.__NoneNode = NoneNode
        
    def AddDataNode1D(self, DataNode1D):
        #print("self.m_DataNode2D"+str(len(self.m_DataNode2D)))
        self.m_DataNode2D.append (DataNode1D)
        return len(self.m_DataNode2D)
        #print("self.m_DataNode2D"+str(len(self.m_DataNode2D)))
        
    def PruneDataNode2D(self):
        len = self.GetDataNode2DLen()
        dN1D = self.m_DataNode2D[len-1]
#        if (    (None == dN1D.GetDataNode1D())
#            and (True == dN1D.NoneNode)):
        if (True == dN1D.NoneNode):
            self.m_DataNode2D.pop()
        

        
    def GetDataNode1D(self, DataNode2DInd):
        #print ("DataNode2DInd: " + str(DataNode2DInd))
        return(self.m_DataNode2D[DataNode2DInd])
    
    def GetDataNode2D(self):
        return (self.m_DataNode2D)

    def GetDataNode2DLen(self):
        return (len(self.m_DataNode2D))
    
    def ShowDataVals(self):
        i = 0
        j = 0            
        while (i < len(self.GetDataNode2D())): #m_DataNode2D)):
            j = 0
            while (j < len(self.GetDataNode2D()[i].GetDataNode1D())):
            #while (j < len(self.m_DataNode2D[i].m_DataNode1D)):
                print (self.m_DataNode2D[i].m_DataNode1D[j].GetDataVal())
                j += 1
            i += 1
            
