class x:
    def y(self):
        keyCompLst = []
        rootName = "ALTC001_01"
        cellValue = "ALTC001_01_01"
        cellValue = "ALTC001_01_01_01"

        
        keyCompLst = cellValue.split(rootName + "_")
        print(keyCompLst)

    def GetUD(self, 
              SyntaxList, 
              MDList0, 
              UDList0, 
              wbObj, 
              sheetName, 
              TCNameInd, 
              udKey, 
              UDRowInd, 
              indentLvl):
        
        sheetObj = self.topUDObj.get_sheetObj(sheetName)
        if (None != sheetObj):
            pass
        else:
            return -1
        
        moreChildren = True
        while(True == moreChildren):
            XLRowInd, XLColInd = self.GetEOMDRowAndCol(sheetObj)
            if ((-1 == XLRowInd)or(-1 == XLColInd)):
                break
            else:
                1#print (":colInd:"+str(XLColInd)+":rowInd:"+str(XLRowInd))
            
            ercRet = -2
            XLColInd = 3
            while (-2 == ercRet):
                XLRowInd += 1
                ercRet, TCName, TCNameInd = self.GetUDLocation(wbObj, sheetObj, XLRowInd, XLColInd, TCNameInd, udKey)
                TCNameInd += 1
            TCNameInd -= 1
                
            XLRowInd = ercRet
            
            if (-1 == XLRowInd):
                moreChildren = False
                break
            #elif (-2 == XLRowInd):
            #    print ("SKIP PROCESSING...")
            #    sys.exit()
            else:
                UD1D = DataNode1D()
                UDList0.AddDataNode1D(UD1D)
                UDRowInd += 1
                
                MDColInd = 0
                UDColInd = 0
                #sheetObj = wbObj[sheetName]
                
                dataVal = sheetObj.cell(XLRowInd, 2).value
                UDNode0 = DataNode(dataVal)
                UDList0.GetDataNode1D(UDRowInd).AddDataNode(UDNode0)
#                opStr = UDList0.GetDataNode1D(UDRowInd).GetDataNode(0).DispObjVal(self.GetPadStr(indentLvl), "TestCaseDelimiter")

              
#                dataVal = sheetObj.cell(XLRowInd, 2).value
#                print ("2:" + str(dataVal))
#                UDNode0 = DataNode(dataVal)
#                UDList0.GetDataNode1D(UDRowInd).AddDataNode(UDNode0)
#                opStr = UDList0.GetDataNode1D(UDRowInd).GetDataNode(0).DispObjVal(self.GetPadStr(indentLvl), "TestCaseDelimiter")
                #print(UDList0.GetDataNode1D(UDRowInd).GetDataNode(0).DispObjVal(self.GetPadStr(indentLvl), "TestCaseDelimiter"))
                
                #if (1 == self.debugId):
                dataVal = sheetObj.cell(XLRowInd, 3).value
                UDNode0 = DataNode(dataVal)
                UDList0.GetDataNode1D(UDRowInd).AddDataNode(UDNode0)
 #               opStr = UDList0.GetDataNode1D(UDRowInd).GetDataNode(1).DispObjVal(self.GetPadStr(indentLvl), "TestCase")
                    #print (opStr)
                #else:
                    #print (opStr)
                    #pass
                
                while(MDColInd < MDList0.GetDataNode1DLen()):
                    MDNode0 = MDList0.GetDataNode(MDColInd)
            
                    XLColInd = MDNode0.GetCol()
                    ScopeId = MDNode0.GetScopeId()
                    SyntaxId = MDNode0.GetSyntaxId()
                    dataVal = sheetObj.cell(XLRowInd, XLColInd).value
                    cell  = sheetObj.cell(XLRowInd, XLColInd)
                    if (cell is not None):
                        if (cell.comment is not None):
                            comment = str(cell.comment)
                            #xArr = comment.split()
                            xArr = comment.splitlines()
                            #xArr = comment.split('\n')
                            for xEl in (xArr):
                                xEl = xEl.replace("Comment: ", "", 1)
                                xEl = xEl.replace(" by Alexander Raj", "", 1)
                                #print ("Line:" + xEl)
                                xArr1 = xEl.split('=')
                                print (len(xArr1))
                                if (len(xArr1) == 2):
                                    xArr1[0] = xArr1[0].strip()
                                    xArr1[1] = xArr1[1].strip()
                                    #xArr1[0] = strip(xArr1[0])
                                    #xArr1[1] = strip(xArr1[1])
                                    print("key:", xArr1[0])
                                    print("val:", xArr1[1])
                            #print ("-------------comment:" + str(comment))
                    
    #                    print(sheetObj.cell(XLRowInd, XLColInd). .comment.text)
                    
                    #print (":WBS:"+sheetName+":TCP:"+udKey+":TC:"+TCName+":MD:"+str(MDColInd)+":UD:"+str(UDRowInd)+":"+str(UDColInd)+":XL:"+str(XLRowInd) + ":" + str(XLColInd)+":DT:"+MDNode0.GetDataType()+":val:"+str(dataVal))        
                    #print (str(dataVal))
                    opStr = ""
                    if (SyntaxId is not None):
                        xRec = self.LookupSyntaxRec(SyntaxList, SyntaxId)
                        if (xRec is not None):
                            if (xRec.GetAction() is not None):
                                #opStr += xRec.GetAction() + " "
                                pass
                            if (xRec.GetResourceType() is not None):
                                #opStr += xRec.GetResourceType() + " "
                                pass
    
                    UDNode0 = DataNode(dataVal)
                    UDList0.GetDataNode1D(UDRowInd).AddDataNode(UDNode0) #Add after rowAttrs from header definition such as testCaseName, headerIndex?
                    #opStr += UDList0.GetDataNode1D(UDRowInd).GetDataNode(UDColInd+2).DispObjVal(self.GetPadStr(indentLvl), MDNode0.GetAttributeName())
                    
                    if ("array" == MDNode0.GetDataType()):
                            opStr = self.GetPadStr(indentLvl) + MDNode0.GetAttributeName() + ": "
                    else:
                        opStr = self.GetPadStr(indentLvl) + MDNode0.GetAttributeName() + ": " + str(UDList0.GetDataNode1D(UDRowInd).GetDataNode(UDColInd+2).GetDataVal())
                        
                    print (opStr)
                    
                    if ("array" == MDNode0.GetDataType()):
                        if ("n" != dataVal):
                            #break
                        #print ("recur..." + MDNode0.GetTab())
                            ercRet = self.GetUD(SyntaxList, MDNode0.GetDataNode1D(), UDNode0.GetDataNode2D(), wbObj, MDNode0.GetTab(), 1, TCName, -1, indentLvl+1)
                        #print ("AFTER GETUD...")
                    MDColInd += 1
                    UDColInd += 1
                    #print ("end of while2")
            TCNameInd += 1
            #print ("end of while1")
        return 0
    
    def GetUDLocation(self, wbObj, sheetObj, row, col, TCNameInd, udKey):
        
        TCName = udKey + "_" + str(f'{TCNameInd:02}')
        comment = ""
        #print("testCaseName:"+TCName)
    
        #sheetObj = wbObj[sheetName]
        #sheetObj = wbObj.get_sheet_by_name(sheetName)
        retVal = -1
        endOfData = -1
        skip = -2
            
        loop = True
           
        while (True == loop):
            comment = sheetObj.cell(row, 1).value
            TestCaseDelimiter = sheetObj.cell(row, 2).value
            if (TestCaseDelimiter is None):
                TestCaseDelimiter = "_"
                
            XLTCName = sheetObj.cell(row, 3).value
            TCName = udKey + TestCaseDelimiter + str(f'{TCNameInd:02}')        
            
            #print(":comment:" + str(comment) + ":cellObj:" + str(XLTCName))
            
            if ("#" == comment):
                if (TCName == XLTCName):
                    #print("retVal:"+str(retVal)+":TCName:"+str(TCName)+":TCNameInd:"+str(TCNameInd))
    #                TCNameInd += 1
    #                TCName = udKey + "_" + str(f'{TCNameInd:02}')
                    retVal = skip
                    loop = False
                else:
                    row += 1
            else:
                if (TCName == XLTCName):
                    retVal = row
                    loop = False
                elif (XLTCName is None):
                    retVal = endOfData
                    loop = False
                else:
                    row += 1
                
                #if((cellObj.value is not None)):
                    #print("testcasenames:" + cellObj.value)
    
    
        return (retVal, TCName, TCNameInd)
    
vx = x()
vx.y()