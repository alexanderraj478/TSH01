from TSHCmd.TSHObjs import TSHObjs
from TSHCmd.TSHObj import TSHObj

class TSHNS:
    def __init__(self):
        self.ns = {}
    
    def GetNS(self, name):
        if name in self.ns:
            tshObjs = self.ns["name"]
            return tshObjs
        else:
            return None
        
    def CreateNS(self, name):
        if name in self.ns:
            print("Namespace: " + name + " already exists")
            tshObjs = self.ns[name]
        else:
            tshObjs = TSHObjs()
            tshObjs.name = name
            self.ns[name] = tshObjs
        return tshObjs
    
    def GetObj(self, ns, name, type):
        pass
    
    def AddObj(self, name, type, val, attrAss):
        tshObj = TSHObj()
        tshObj.name = name
        tshObj.type = type
        tshObj.val = val
        tshObj.attrAss = attrAss
        tshObjs = self.GetNS(name)
        if (None != tshObjs):
            tshObjs.AddObj(tshObj)
        else:
            tshObjs = self.GetNS(self, "global")
            if (None == tshObjs):
                self.CreateNS("global")
                pass
            else:
                pass
            tshObjs = self.ns["global"]
            tshObjs.AddObj(tshObj)
        pass