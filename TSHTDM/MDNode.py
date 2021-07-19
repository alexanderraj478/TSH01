import copy
from TSHTDM.DataNode1D import DataNode1D

class MDNode:                
    def __init__(self, MDAss):
        self.MDAss = MDAss
        self.m_DataNode1D = DataNode1D()
    
    @property
    def MDAss(self):
        return self.__MDAss
    
    @MDAss.setter
    def MDAss(self, MDAss):
        self.__MDAss = copy.deepcopy(MDAss)


    def GetDataNode1D(self):
        return (self.m_DataNode1D)
    