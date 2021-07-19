from TSHTDM.DataNode1D import DataNode1D
from argparse import Action

class SyntaxRec:
    syntaxID = -1
    action = ""
    resourceType = ""
    
    def __init__(self, syntaxID, action, resourceType):
        self.syntaxID = syntaxID
        self.action = action
        self.resourceType = resourceType
    
    def GetSyntaxID (self):
        return self.syntaxID
    
    def GetAction(self):
        return (self.action)
    
    def GetResourceType(self):
        return self.resourceType
    