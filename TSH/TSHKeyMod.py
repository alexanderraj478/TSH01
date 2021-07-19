import sys
from keyTree.TSHKTreeNode import TSHKTreeNode
from TSHGlobal import constants as c

debug = 0
class TSHKeyMod:

    def __init__(self, sheetObj, pshComment, MDKDelimiter, UDKDelimiter):
        self.notAppl = "Should not come here: "
        self.vKTree = None
        self.sheetObj = sheetObj
                
        self.UDHdrDict = None
        self.MDHdrDic = None
        
        self.keyTreeColBeg = c.MDKHdrCol["MDK01"]
        self.keyTreeColEnd = 0
                
        self.rootRowInd = 0
        self.rootColInd = 0
        
        self.pArr = []
        self.cArr = []
        
        self.begOfTree = False
        self.endOfTree = False
        self.keyTreeDepth = 0
        
        self.pshComment = pshComment
        self.MDKDelimiter = MDKDelimiter
        self.UDKDelimiter = UDKDelimiter
        
        rowTot, colTot = self.GetEOMDRowAndCol()
        if (-1 == rowTot) or (-1 == colTot):
            sEOMDMaxRowInd = str(c.EOMDMaxRowInd)
            sEOMDMaxColInd = str(c.EOMDMaxColInd)
            print("---SheetName: " + sheetObj.title + "---")
            print("Error: EOMD is not encountered in the region from (1, 1) to (" + sEOMDMaxRowInd + ", " + sEOMDMaxColInd + ")")
            print("Invalid workbook")
            return None

        self.EOMDRowInd = rowTot
        self.EOMDColInd = colTot

        rowTot, colTot = self.GetEOUDRowAndCol(rowTot)
        if (-1 == colTot):
            sEOMDRowInd = str(self.EOMDRowInd)
            sEOUDMaxColInd = str(c.EOUDMaxColInd)
            print("---SheetName: " + sheetObj.title + "---")
            print("Warning: EOUD is not encountered in the region from (" + sEOMDRowInd + ", 1) to (" + sEOMDRowInd + ", " + sEOUDMaxColInd + ")")
            print("In this case it will stop to retrieve grid columns once it encounters a blank AttributeName")
        
        self.EOUDRowInd = rowTot
        self.EOUDColInd = colTot

#        self.GetHeaderRowIndexes()
#        keyTreeColEnd =  self.mdKTreeDepth = self.GetKeySpan(c.MDKeyPrefix, self.mdHdrRowInd, c.MDKHdrCol["MDK01"])
#        c.MDKHdrCol["MDK01"]
#        self.udKTreeDepth = self.GetKeySpan(c.UDKeyPrefix, self.udHdrRowInd, c.UDKHDRCol["UDK01"])
#        c.UDKHDRCol["UDK01"]
        
        self.keyTreeColEnd = self.EOMDColInd
        self.keyTreeDepth = self.keyTreeColEnd - self.keyTreeColBeg
        for ind in range (self.keyTreeDepth):
            self.pArr.append(None)
            self.cArr.append(None)
            
        self.vShell = None
    
    #------------------------------------------------------------------------------------------- 
    @property
    def vShell(self):
        return(self.__vShell)
    
    @vShell.setter
    def vShell(self, vShell):
        self.__vShell = vShell
        
    #------------------------------------------------------------------------------------------- 
    @property
    def vKTree(self):
        return self.__vKTree
    
    @vKTree.setter
    def vKTree(self, vKTree):
        self.__vKTree = vKTree

    #-------------------------------------------------------------------------------------------
    def AddToKey(self, key, val):
        self.MDHdrDic[key] = val
        pass

    #-------------------------------------------------------------------------------------------
    def GetKeySpan(self, treePrefix, rowInd, colInd):        
        while(colInd < self.EOMDRowInd):
            cellVal1 = self.sheetObj.cell(rowInd, colInd).value
            cellVal2 = treePrefix + str(f'{colInd:02}')
            if (cellVal1 == cellVal2):
                colInd += 1
            else:
                break
        return colInd
    #-------------------------------------------------------------------------------------------
            
    def GetTreeSpan(self, **keyValDict):
        keyValTot = len(keyValDict)
        if keyValDict is not None:
            for key, val in keyValDict.items():
                if (key not in ("treePrefix", "rootName", "keyVect", "keyTot", "keyType")):
                    print("Invalid key value found: " + key)
                    print("Valid key values are treePrefix, rootName, keyVect, keyTot, keyType")
                    return
                if (val in (None, '')):
                    print("Invalid value: "  + str(val) + " supplied for " + key)
                    return
                if ("treePrefix" == key):
                    treePrefix = keyValDict["keyType"]
                if ("rootName" == key):
                    suiteName = keyValDict["keyType"]
                if ("keyVect" == key):
                    suiteName = keyValDict["keyType"]
                if ("keyTot" == key):
                    suiteName = keyValDict["keyType"]
                if ("keyType" == key):
                    suiteName = keyValDict["keyType"]
                if ("rowInd" == key):
                    rowInd = keyValDict["rowInd"]
        
        rowInd = 0
        colInd = 1
        while(rowInd < self.EOMDRowInd):
            rowInd += 1
            cellVal1 = self.sheetObj.cell(rowInd, colInd).value
            cellVal2 = treePrefix + str(f'{colInd:02}')
            if (cellVal1 == cellVal2):
                colInd += 1
            else:
                break
        

    #-------------------------------------------------------------------------------------------
    def GetHeaderRowIndexes(self):
        
        mdHdrRowInd = -1
        udHdrRowInd = -1
        rowInd = 0
        colInd = 1
        while(rowInd < self.EOMDRowInd):
            rowInd += 1
            cellVal = self.sheetObj.cell(rowInd, colInd).value
#--------------------------------------------------------------------------------------------------------
#   Check for comment
#----------------------------------------------------------------------------------------------------------
            ercRet = self.pshComment.isAComment(cellVal)
            ercRet = self.pshComment.ProcessCommentStatus()
            if (ercRet == -1):
                return ercRet                
            elif (ercRet == 1):
                continue
            elif (ercRet == 0):
                pass
            else:
                pass
#--------------------------------------------------------------------------------------------------------
#   Check for header Tag
#----------------------------------------------------------------------------------------------------------
            
            if (cellVal == c.mdHdrName):
                mdHdrRowInd = rowInd

            if (cellVal == c.udHdrName):
                udHdrRowInd = rowInd

                
        self.mdHdrRowInd = mdHdrRowInd
        self.udHdrRowInd = udHdrRowInd
        return

    #------------------------------------------------------------------------------------------- 
    def ComparePAndCArr(self):
        NoneIndBeg = -1
        NoneIndEnd = -1
        
        pTot = len(self.pArr)        
        cTot = len(self.cArr)

        ercRet = -1
        if (0 >= cTot):
            return (ercRet)

        #cTreeDepth = 0
        #for cInd in range(cTot):
        #    if (None != self.cArr[cInd]):
        #        cTreeDepth = cInd
                
        cInd = 0
        if (None == self.cArr[cInd]):
            #loop until None
            while (cInd < cTot):
                if (None != self.cArr[cInd]):
                    break
                cInd += 1
            #loop until NonNone
            while (cInd < cTot):
                if (None == self.cArr[cInd]):
                    break
                cInd += 1
            #loop until None
            NoneIndBeg = cInd
            while (cInd < cTot):
                if (None != self.cArr[cInd]):
                    break
                NoneIndEnd = cInd
                cInd += 1
        else:
            #loop until NonNone
            while (cInd < cTot):
                if (None == self.cArr[cInd]):
                    break
                cInd += 1
            #loop until None
            NoneIndBeg = cInd
            while (cInd < cTot):
                if (None != self.cArr[cInd]):
                    break
                NoneIndEnd = cInd
                cInd += 1
            #loop until NonNone
            while (cInd < cTot):
                if (None == self.cArr[cInd]): #bug??? changed != to ==
                    break
                cInd += 1
        
        if (cInd < cTot):
            #print("Invalid String")
            return (ercRet)
        else:
            #print("Valid String")
            
            for cInd in range(cTot):
                pInd = cInd
                if (self.pArr[pInd] != self.cArr[cInd]):
                    if (None != self.cArr[cInd]):
                        self.pArr[pInd] = self.cArr[cInd]
            
            if (NoneIndEnd == cTot - 1):
                for pInd in (NoneIndBeg, NoneIndEnd):
                    self.pArr[pInd] = None
            ercRet = 0
            
        return (ercRet)                
    #------------------------------------------------------------------------------------------- 


    def ComparePAndCArrOld(self):
        pTot = len(self.pArr)        
        cTot = len(self.cArr)
        print ("pTot cTot:"+str(pTot)+":"+str(cTot))
        NotNoneFound = 0
        NoneFound = 0
        
        ercRet = 0
        for cInd in range(cTot):
            pInd = cInd
            if (None == self.cArr[cInd]):
                if (None == self.pArr[pInd]):
                    pass
                elif (None != self.pArr[pInd]):
                    if (cInd == NoneFound):
                        pass
                    elif (cInd > NoneFound):
                        self.pArr[pInd] = self.cArr[cInd]
                    elif (cInd < NoneFound):
                        print("Need to debug if it comes here")
                NoneFound += 1
            elif (None != self.cArr[cInd]):
                if (None == self.pArr[pInd]):
                    self.pArr[pInd] = self.cArr[cInd]
                elif (None != self.pArr[pInd]):
                    if (self.pArr[pInd] == self.cArr[cInd]):
                        pass
                    elif (self.pArr[pInd] != self.cArr[cInd]):
                        if (cInd == NoneFound):
                            self.pArr[pInd] = self.cArr[cInd]
                        elif (cInd > NoneFound):
                            if (cInd == NotNoneFound):
                                self.pArr[pInd] = self.cArr[cInd]
                            elif (cInd > NotNoneFound):
                                print("Error. Partial Child Vector specified")
                                ercRet = -1
                            elif (cInd < NotNoneFound):
                                print("Need to debug if it comes here")
                        elif (cInd < NoneFound):
                            print("Need to debug if it comes here")
                NotNoneFound += 1
            
        return (ercRet)                
    #------------------------------------------------------------------------------------------- 

        
    def GetKTree(self, name, keyElRowInd, keyElColInd):
        if (self.vKTree == None):
            self.vKTree = TSHKTreeNode(name, keyElRowInd, keyElColInd, "")
            return self.vKTree
    
        if (self.vKTree.GetData() == name):
            return self.vKTree
        else:
            return None
        
    #------------------------------------------------------------------------------------------- 
    def TSHTreeDisp(self, parNode, indentLvl):
        if (None != parNode):
            padStr = ""
            for indentInd in range(indentLvl):
                padStr += "    "
                
            print(padStr + str(parNode.GetSSRowInd()) + ":" + str(parNode.GetData()))

            for nodeInd in range(len(parNode.nodeArr)):
                if (None != parNode.nodeArr):
                    if (None != parNode.nodeArr[nodeInd]):
                        self.TSHTreeDisp (parNode.nodeArr[nodeInd], indentLvl + 1)
        else:
            pass
    
    #------------------------------------------------------------------------------------------- 
    def GetMDKeys(self, rootName, keyType):
        rowInd = 4
        colInd = self.keyTreeColBeg
        return self.GetKeys(rootName, rowInd, colInd, keyType, c.MDKRegion)
        
    #------------------------------------------------------------------------------------------- 
    def GetUDKeys(self, rootName, keyType):
        rowInd = self.EOMDRowInd + 1
        colInd = self.keyTreeColBeg
        return self.GetKeys(rootName, rowInd, colInd, keyType, c.UDKRegion)
                    
    #------------------------------------------------------------------------------------------- 
    def ReadNextRowOfTree(self, keyRegion, keyType, rootName, ssRowNum, colInd):
            if (keyType == "S"):
                (ercRet, nullRow) = self.ReadNextRowAsSingKey(rootName, ssRowNum, colInd, keyRegion)
            else:
                (ercRet, nullRow) = self.ReadNextRowAsMultKey(ssRowNum, colInd)
            return (ercRet, nullRow)
    #-------------------------------------------------------------------------------------------
    def IsANullRow(self):
        nullRow = True
        nonzeroChildren = 0
        for y in range(len(self.cArr)):
            if (None != self.cArr[y]):
                nullRow = False
                if (y > 0):
                    nonzeroChildren += 1
        return (nullRow, nonzeroChildren)

    #-------------------------------------------------------------------------------------------
    def ReadNextRowAsSingKey(self, rootName, ssRowNum, colInd, keyRegion):
        self.cArr=[]
        cellValStr = self.sheetObj.cell(ssRowNum, colInd).value

        if (None == cellValStr):
            self.ReadNextRowAsMultKey(ssRowNum, colInd)
            (nullRow, nonzeroChildren) = self.IsANullRow()
            if (True == nullRow):
                return (c.TSH_TREE_NT_EOR, nullRow)
            else:
                return (c.TSH_TREE_CONT_SRCH, nullRow)
        else:
            cellValOff = cellValStr.find(rootName)
            if (0 == cellValOff):
                #found
                #self.cArr.append(rootName)
                if (c.MDKRegion == keyRegion):
                    sep = self.MDKDelimiter
                else:
                    sep = self.UDKDelimiter
                self.cArr = cellValStr.split(sep)
                
                
#                if ((2 == len(t1Arr)) and (t1Arr[0] == "") and (t1Arr[1] == "")):
#                    pass
#                else:
#                    t2Arr = t1Arr[1].split(sep)
#                    val = t1Arr[1]
#                    t2Arr = val.split(sep)
#                    for t2Ind in range(1, len(t2Arr)):
#                        self.cArr.append(t2Arr[t2Ind])    
                pass
            elif(-1 == cellValOff):
                #not found
                self.cArr.append(cellValStr)
                pass
            else:
                #mid section of another key most likely but surely not part of this tree
                print("Should debug this scenario")
                self.cArr.append(cellValStr)
                pass
            return (0, False)
    #------------------------------------------------------------------------------------------- 
    def ReadNextRowAsMultKey(self, ssRowNum, colInd):
        self.cArr=[]        
        for y in range(self.keyTreeDepth):
            self.cArr.append(self.sheetObj.cell(ssRowNum, colInd+y).value)
        (nullRow, nonzeroChildren) = self.IsANullRow()
        return (0, nullRow)
    #------------------------------------------------------------------------------------------- 
    def GetKeys(self, rootName, rowInd, colInd, keyType, keyRegion):
        #DEBUG START
        if(keyRegion == c.UDKRegion):
            debug = 1
        #DEBUG END

        if ("MDKR" == keyRegion):
            keyDelimiter = self.MDKDelimiter
        elif ("UDKR" == keyRegion):
            keyDelimiter = self.UDKDelimiter
        else:
            print("Invalid choice:" + keyRegion)
            return
        
        for pInd in range(len(self.pArr)):
            self.pArr[pInd] = None
            
        mdKeyAss = {}
        ssRowNum = rowInd
        endOfRecords = False
        x = -1
        while(False == endOfRecords):
            x += 1
            ssRowNum = rowInd+x
            commentCellValue = self.sheetObj.cell(ssRowNum, 1).value
#            if ("S" == keyType):
#                if (None != self.sheetObj.cell(ssRowNum, colInd).value):
#                    self.pArr[0] = self.sheetObj.cell(ssRowNum, colInd).value
#--------------------------------------------------------------------------------------------------------
#   Check for comment
#----------------------------------------------------------------------------------------------------------
            ercRet = self.pshComment.isAComment(commentCellValue)
            ercRet = self.pshComment.ProcessCommentStatus()
            if (ercRet == -1):
                return ercRet                
            elif (ercRet == 1):
                continue
            elif (ercRet == 0):
                pass
            else:
                pass
#--------------------------------------------------------------------------------------------------------
#This check is done to disable MDKey routine to goto UD Region
#----------------------------------------------------------------------------------------------------------
            if (keyRegion == c.MDKRegion):
                if (ssRowNum == self.EOMDRowInd):
                    endOfRecords = True
                    continue
            
            (retVal, nullRow) = self.ReadNextRowOfTree(keyRegion, keyType, rootName, ssRowNum, colInd)
            if (retVal == c.TSH_TREE_CONT_SRCH):
                continue
            elif (retVal == c.TSH_TREE_EOR):
                endOfRecords = True
                continue
            elif (ercRet == 0):
                pass
            else:
                pass 
            
            #DEBUG START
            if (0):
                cArrStr = ""
                pArrStr = ""
                for y in range(len(self.cArr)):
                    cArrStr = cArrStr + "," + str(self.cArr[y])
                    pArrStr = pArrStr + "," + str(self.pArr[y])
                print(rootName + "cArr " + cArrStr)
                print(rootName + "pArr " + pArrStr)
            #DEBUG END

            keyPrefArr = rootName.split(keyDelimiter)
            retVal = self.ValidateNextRowOfTree(keyType, self.begOfTree, nullRow, keyPrefArr[0])    
            if (retVal == c.TSH_TREE_CONT_SRCH):
                continue
            elif (retVal == c.TSH_TREE_ST_BEG):
                self.rootRowInd = ssRowNum
                self.rootColInd = self.keyTreeColBeg
            elif (retVal == c.TSH_TREE_ST_EOR):
                endOfRecords = True
                continue
            elif (retVal == c.TSH_TREE_NT_EOR):
                endOfRecords = True
                continue
                
            ercRet = self.ComparePAndCArr()
            if (-1 == ercRet):
                return

            key = ""
            keyTot = 0
            for dataInd in range(len(self.pArr)):
                if (self.pArr[dataInd] == None):
                    break
                else:
                    keyTot = keyTot  + 1
                    if (0 == dataInd):
                        key = str(self.pArr[dataInd])
                    else:
                        key = key + keyDelimiter + str(self.pArr[dataInd])
            
            if (0 == key.find(rootName)):
                mdKeyAss[str(ssRowNum)] = key
                rootName = self.pArr[0]
                if(None != self.GetKTree(rootName, self.rootRowInd, self.rootColInd)):
                    self.vKTree.TSHTreeNodesAdd(self.vKTree, self.pArr, keyTot, ssRowNum, self.keyTreeColBeg, keyDelimiter)
                else:
                    print("End of records for root Node")
                    pass
            
                srchArr = ["K8SDEMO1", "01"]
                #srchArr = ["K8SDEMO1"]
                currNode = self.vKTree
                childArr = self.vKTree.TSHTreeNodesGet(currNode, srchArr, keyDelimiter)
        if(0):#(keyRegion == c.UDKRegion):
            print("------ children start")
            self.vKTree.TSHTreeNodesPrint(childArr)
            print("------ children end")
        return (mdKeyAss)
        
           
        #for mdKey in mdKeyAss.keys():
        #    print("mdKeyAss{" + mdKey + "}=" + mdKeyAss[mdKey]) 
#        self.TSHTreeDisp(self.vKTree, 0)

        #nodeNameInd = 0
        #nodeNameTot = 3
        #nodeNameLst = ("Anu", "Derek", "Erla", "Sean")
        
        #currNode = self.TSHTreeNodesFind(self.vKTree, self.vKTree, nodeNameLst, nodeNameTot, nodeNameInd)
        #if (None != currNode):
        #    print(currNode.GetData())
        #    for tNode in currNode.nodeArr:
        #        print("  " + tNode.GetData())
        
    #------------------------------------------------------------------------------------------- 
    def GetTreeNodeGetChildren(self, parNode):
        if (None == parNode):
            return None
        else:
            return parNode.nodeArr()
        pass
    
    #------------------------------------------------------------------------------------------- 
    def TSHTreeNodesFind(self, parNode, currNode, nodeNameLst, nodeNameTot, nodeNameInd):
        if (nodeNameInd < nodeNameTot):
            if (currNode.GetData() != nodeNameLst[nodeNameInd]):
                return None
            else:
                pass                
        else:
            return parNode    
 

        for nodeInd in range(len(currNode.nodeArr)):
            retNode = self.TSHTreeNodesFind(currNode, currNode.nodeArr[nodeInd], nodeNameLst, nodeNameTot, nodeNameInd+1)
            if (None == retNode):
                pass
            else:
                return retNode

    #------------------------------------------------------------------------------------------- 
    def GetEOUDRowAndCol(self, rowInd):
        colMaxForEndOfHeader = c.EOUDMaxColInd
        colInd = 1
        
        while (colInd < colMaxForEndOfHeader):
            cellVal = self.sheetObj.cell(rowInd, colInd).value
            if ((cellVal is not None) and ("EOUD" == cellVal)):
                return (rowInd, colInd)
            colInd += 1
        return (-1, -1)

    def GetEOMDRowAndCol(self):
        rowMaxForEndOfHeader = c.EOMDMaxRowInd
        colMaxForEndOfHeader = c.EOMDMaxColInd
        rowInd = 1
        colInd = 1
        
        while (rowInd < rowMaxForEndOfHeader):
            while (colInd < colMaxForEndOfHeader):
                cellVal = self.sheetObj.cell(rowInd, colInd).value
                if ((cellVal is not None) and ("EOMD" == cellVal)):
                    return (rowInd, colInd)
                colInd += 1
            colInd = 1
            rowInd += 1

        return (-1, -1)
    
    #------------------------------------------------------------------------------------------- 
    def DispRows(self):
        for row in self.sheetObj.iter_rows():
            for cell in row:
                print(cell.value)

    #------------------------------------------------------------------------------------------- 
    def DispRows02(self, rowTot, colTot):
        for row in range(rowTot):
            for col in range(colTot):
                print(self.sheetObj.cell(row+1, col+1).value)

    #------------------------------------------------------------------------------------------- 
    def ValidateNextRowOfTree(self, keyType, begOfTree, nullRow, rootName):
        retVal = c.TSH_TREE_ERR
        
        if ("S" == keyType):
        ##########################################
            if (True == begOfTree):
                #=================================
                if (True == nullRow):
                    #-----------------------------
                    if (self.cArr[0] == rootName):
                        retVal = c.TSH_TREE_ERR
                        print(self.notAppl + str(retVal) + ":" + str(begOfTree) + ":" + str(nullRow) + ":" + str(rootName))
                        sys.exit()
                        pass
                    elif (self.cArr[0] == None):
                        self.begOfTree = False
                        retVal = c.TSH_TREE_ST_EOR
                        pass
                    else:
                        retVal = c.TSH_TREE_ERR
                        print(self.notAppl + str(retVal) + ":" + str(begOfTree) + ":" + str(nullRow) + ":" + str(rootName))
                        sys.exit()
                        pass
                    #-----------------------------
                elif (False == nullRow):
                    #-----------------------------
                    if (self.cArr[0] == rootName):
                        retVal = c.TSH_TREE_ST_CONT
                        pass
                    elif (self.cArr[0] == None):
                        self.begOfTree = False
                        retVal = c.TSH_TREE_ST_EOR
                        pass
                    else:
                        self.begOfTree = False
                        retVal = c.TSH_TREE_ST_EOR
                        pass
                    #-----------------------------
                else:
                    print(self.notAppl)
                #=================================
            elif (False == begOfTree):
                #=================================
                if (True == nullRow):
                    if (self.cArr[0] == rootName):
                        retVal = c.TSH_TREE_ERR
                        print(self.notAppl + str(retVal) + ":" + str(begOfTree) + ":" + str(nullRow) + ":" + str(rootName))
                        sys.exit()
                        pass
                    elif (self.cArr[0] == None):
                        retVal = c.TSH_TREE_NT_EOR
                        pass
                    else:
                        retVal = c.TSH_TREE_ERR
                        print(self.notAppl + str(retVal) + ":" + str(begOfTree) + ":" + str(nullRow) + ":" + str(rootName))
                        sys.exit()
                        pass
                elif (False == nullRow):
                    if (self.cArr[0] == rootName):
                        self.begOfTree = True
                        retVal = c.TSH_TREE_ST_BEG
                        pass
                    elif (self.cArr[0] == None):
                        self.begOfTree = False
                        retVal = c.TSH_TREE_ST_EOR
                        pass
                    else:
                        self.begOfTree = False
                        retVal = c.TSH_TREE_CONT_SRCH
                        pass
                else:
                    print(self.notAppl)
                #=================================
            else:
                print(self.notAppl)
        ##########################################
        elif ("M" == keyType):
            if (True == begOfTree):
                if (True == nullRow):
                    if (self.cArr[0] == rootName):
                        retVal = c.TSH_TREE_ERR
                        print(self.notAppl + str(retVal) + ":" + str(begOfTree) + ":" + str(nullRow) + ":" + str(rootName))
                        sys.exit()
                        pass
                    elif (self.cArr[0] == None):
                        self.begOfTree = False
                        retVal = c.TSH_TREE_ST_EOR
                        pass
                    else:
                        retVal = c.TSH_TREE_ERR
                        print(self.notAppl + str(retVal) + ":" + str(begOfTree) + ":" + str(nullRow) + ":" + str(rootName))
                        sys.exit()
                        pass
                elif (False == nullRow):
                    if (self.cArr[0] == rootName):
                        retVal = c.TSH_TREE_DT_EXP_REF
                        pass
                    elif (self.cArr[0] == None):
                        retVal = c.TSH_TREE_DT_IMP_REF
                        pass
                    else:
                        #retVal = c.TSH_TREE_DT_BEG # this could be returned as tuple with additional information
                        retVal = c.TSH_TREE_ST_EOR
                        pass
                else:
                    print(self.notAppl)
            elif (False == begOfTree):
                if (True == nullRow):
                    if (self.cArr[0] == rootName):
                        retVal = c.TSH_TREE_ERR
                        print(self.notAppl + str(retVal) + ":" + str(begOfTree) + ":" + str(nullRow) + ":" + str(rootName))
                        sys.exit()
                        pass
                    elif (self.cArr[0] == None):
                        retVal = c.TSH_TREE_NT_EOR
                        pass
                    else:
                        retVal = c.TSH_TREE_ERR
                        print(self.notAppl + str(retVal) + ":" + str(begOfTree) + ":" + str(nullRow) + ":" + str(rootName))
                        sys.exit()
                        pass
                elif (False == nullRow):
                    if (self.cArr[0] == rootName):
                        self.begOfTree = True
                        retVal = c.TSH_TREE_ST_BEG
                        pass
                    elif (self.cArr[0] == None):
                        self.begOfTree = False
                        retVal = c.TSH_TREE_CONT_SRCH
                        pass
                    else:
                        retVal = c.TSH_TREE_CONT_SRCH
                        pass
                else:
                    print(self.notAppl + "1 else")
                    sys.exit()
            else:
                print(self.notAppl + "2 else")
                sys.exit()
        else:
            print(self.notAppl + "3 else")
            sys.exit()
        return retVal
    
    #------------------------------------------------------------------------------------------- 
    #FUTURE CLEANUP/RESTORE ONLY IF NEEDED
    #------------------------------------------------------------------------------------------- 
    def ReadNextRowAsSingKey01(self, rootName, ssRowNum, colInd, keyRegion):
        self.cArr=[]
        cellValStr = self.sheetObj.cell(ssRowNum, colInd).value

        if (None == cellValStr):
            self.ReadNextRowAsMultKey(ssRowNum, colInd)
            (nullRow, nonzeroChildren) = self.IsANullRow()
            if (True == nullRow):
                return (c.TSH_TREE_NT_EOR, nullRow)
            else:
                return (c.TSH_TREE_CONT_SRCH, nullRow)
        else:
            cellValOff = cellValStr.find(rootName)
            if (0 == cellValOff):
                #found
                self.cArr.append(rootName)
                t1Arr = cellValStr.split(rootName)
                
                if (c.MDKRegion == keyRegion):
                    sep = self.MDKDelimiter
                else:
                    sep = self.UDKDelimiter
                
                if ((2 == len(t1Arr)) and (t1Arr[0] == "") and (t1Arr[1] == "")):
                    pass
                else:
                    t2Arr = t1Arr[1].split(sep)
                    val = t1Arr[1]
                    t2Arr = val.split(sep)
                    for t2Ind in range(1, len(t2Arr)):
                        self.cArr.append(t2Arr[t2Ind])    
                pass
            elif(-1 == cellValOff):
                #not found
                self.cArr.append(cellValStr)
                pass
            else:
                #mid section of another key most likely but surely not part of this tree
                print("Should debug this scenario")
                self.cArr.append(cellValStr)
                pass
            return (0, False)
    #------------------------------------------------------------------------------------------- 
