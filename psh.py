try:
    from StringIO import StringIO ## for Python 2
except ImportError:
    from io import StringIO ## for Python 3
    from io import BytesIO
    
import copy
from zipfile import ZipFile
import os
from os.path import basename
from binstar_client.scripts.cli import main

#import os
import sys
#import fileinput
#import importlib

#-----------------------------------------------------
#sys.path.append('/home/alex/learn/python/src/PYSH/DMT')
#For python3

#import from sibling: from .user import User
#import from nephew: from .usr.user import User
from TSHjson.TSHjson import TSHjson
from TSHModule.TSHModule import TSHModule

from TSHExcel.TSHxlrd import TSHxlrd
from TSHExcel.TSHpandas import TSHpandas
from TSHExcel.TSHxmltodict import TSHxmltodict

#TriSHul harness specific imports
from TSHGlobal import constants as c
from TSHGlobal.TSHGlobal import *
#debug_print
from TSHProcess.TSHProc import TSHProc
from TSHyaml.TSHyaml import TSHyaml
from TSH.PSHMD import PSHMD
from TSH.TSHTokenizer import TSHTokenizer
#from TSH.PSHFunc import PSHFunc
#from TSH.PSHPar import PSHPar
#from TSH.PSHMod import PSHMod
#from TSHFS.PSHFile import PSHFile
from TSHFS.PSHDir import PSHDir
from TSHString import TSHStrFind
from TSHComment.TSHComment import TSHComment
from TSHTDM.RecurseMD import RecurseMD
#from TSHCmd.TSHCmd import TSHCmd
from TSHos.TSHos import TSHos
from numexpr.expressions import LeafNode
from astropy.table import row
from TSHSelenium.TSHSelenium import TSHSelenium

#import RecurseMD
#from ABC.ABC import TSHSeleniumClass

#from MyTest import MyFunction

#To debug code on console
#add import pdb; 
#pdb.set_trace()

#plugins for testing language specific functionality
#from RecurseMD import RecurseMD
#from keyTree import keyTree

#plugins for testing product specific functionality

class TSHShell:
	
#------------------------------------------------------------------------------------------------------------------------------------

	def TSHConvertStrToBool(self, parVal):
		if parVal == "True":
			return True
		else:
			return False
		
#------------------------------------------------------------------------------------------------------------------------------------

	def __init__(self):
		self.PSHInst0 = PSHMD()
		self.tshTokenizer = TSHTokenizer()
		self.pshDir = PSHDir()
		self.pshYAML = TSHyaml()
		self.token = ""
		self.cmdToken = ""
		self.suiteName = ""
		self.funcName = ""
		self.parName = ""
		self.parVal = ""
		self.cmdLine = ""
		self.prevCommentChg = 0
		self.currCommentChg = 0
		
		#self.singRowComment = False
		#self.multRowCommentBeg = False
		#self.multRowCommentEnd = False

		self.THarnComment = TSHComment()
		self.TwareComment = TSHComment()
		self.MwareComment = TSHComment()
		self.DwareComment = TSHComment()

		self.silentMode = True
		self.batchMode = "off"
		self.pshMod = TSHModule()

#------------------------------------------------------------------------------------------------------------------------------------

	def ReadCommandLine(self):
		self.cmdLine = ""
		for arg in (sys.argv[1:]):
			self.cmdLine = self.cmdLine + arg + " "		
#------------------------------------------------------------------------------------------------------------------------------------

	def ProcessInputSource(self):
		self.eop = False
		debug_print("Executing...", "off")
		while (False == self.eop):
			ipDict = {}
			opDict = {}
			ipDict = {"DriverObj":self}

			print('PSH> ', end='', flush=True)
			(self.cmdToken) = self.tshTokenizer.GetNextToken()
			if (None == self.cmdToken):
				self.eop = True
				continue
			elif ("" == self.cmdToken):
				continue
			
			self.InitializeComment()
			ercRet = self.TwareComment.isAComment(self.cmdToken)
			ercRet = self.TwareComment.ProcessCommentStatus()
			
			if (ercRet == -1):
				debug_print("Fix issues with comments in script")
				self.eop = True
				continue
			if (ercRet == 1):
				self.ProcessTSHComment()
				continue
			elif (ercRet == 0):
				self.ReadAndUpdateSetup()
			

			#if (0 == ercRet) and (True == comment):
			#	self.ProcessTSHComment()
			#	if (True == self.pshComment.multRowCommentEnd):
			#		self.pshComment.multRowCommentBeg = False
			#		self.pshComment.multRowCommentEnd = False
			#		self.pshComment.multRowComment = False
					
			#	if (True == self.pshComment.singRowComment):
			#		self.pshComment.singRowComment = False
			#	continue
			#elif (-1 == ercRet): #doesn't matter what value comment takes on
			#elif (0 == ercRet) and (False == comment):
			#	pass
			#else:
			#	print("I am guessing it should never come here :)")
			
				if ("RegisterSuite" == self.cmdToken):
					self.ProcessTSHRegisterSuite()

				elif ("RegisterFunction" == self.cmdToken):
					self.ProcessTSHRegisterFunction()
				elif ("RegisterParameter" == self.cmdToken):
					self.ProcessTSHRegisterParameter()
				elif ("set" == self.cmdToken):
					self.ProcessTSHSet()
				elif ("get" == self.cmdToken):
					parVal = self.ProcessTSHGet()
					print(parVal)
				elif ("return" == self.cmdToken):
					self.ProcessTSHReturn()
				elif ("@" == self.cmdToken):
					self.ProcessTSHMacroRun()
				elif ("run" == self.cmdToken):
					self.ProcessTSHScriptRun()
				elif ("system" == self.cmdToken):
					pass
				elif ("GenerateYAML" == self.cmdToken):
					pass
				elif ("getData" == self.cmdToken):
					ercRet = self.ProcessGetData(ipDict, opDict)
				elif ("LoadModule" == self.cmdToken):
					pass
				elif ("mkdir" == self.cmdToken):
					dirName = self.ProcessTSHGet(suiteName="TSH", functionName="TSH", parameterName="dirName")
					tshOS = TSHos()
					tshOS.TSHOSmkdir(dirName)
				elif ("cd" == self.cmdToken):
					dirName = self.ProcessTSHGet(suiteName="TSH", functionName="TSH", parameterName="dirName")
					tshOS = TSHos()
					tshOS.TSHOSchdir(dirName)
				elif ("RunProcess" == self.cmdToken):
					tshProc = TSHProc()
					ercRet = tshProc.TSHSubProcessRun(ipDict, opDict)
					pass
				elif ("dump" == self.cmdToken):
					tshJSON = TSHjson()
					tshJSON.mainFunc(ipDict, opDict)
				elif ("cwd" == self.cmdToken):
					#tshSelenium = ABC()
					#kvDict = {"DriverObj":self}
					#tshSelenium.TSHSelSubmit(keyValDict=kvDict)
					
					#vc3 = c3()
					#vc1 = c1()
					#vc2 = c2()
					
					#tshOS = TSHos()
					#tshOS.GetClassInfo1()
					#tshOS.GetClassInfo2()

					#keyValDict = {"DriverObj": self, 
					#			"moduleName" : "MyTest"}
		
					
					#module = self.pshMod.FindAndLoadModule(keyValDict=keyValDict)

#					module.GetClassInfo1()
					pass
					if (0):
					#module = __import__("PSHFile")
					#my_class = getattr(module, "PSHFile")
					#print (my_class)
					#instance = PSHFile()
					#funcAddr = GetFunctionAddr(self, "ZipDirectory")
					#funcAddr()	
						pass

				elif ("quit" == self.cmdToken or "exit" == self.cmdToken):
					self.eop = True
				elif ("CreateNamespace" == self.cmdToken):
					#ipDict = {"DriverObj":self}
					ercRet = self.pshNS.CreateNS(self, ipDict, opDict)
					#set Namespace Name a
					#CreateNamespace
				elif ("CreateObject" == self.cmdToken):
					ercRet = self.pshObj.CreateObject(self, ipDict, opDict)
					pass

#set Object Namespace a
#set Object Type PSH
#set Object Name b
#CreateObject
#can be only invoked internally. Not for external exposure.
#setByVar TSH TSH SuiteInScope variableName

				elif ("SetByValue" == self.cmdToken):
#set TSH TSH SuiteInScope TSH
#setByValue
					self.ProcessTSHSet()
					pass
				elif ("SetByName" == self.cmdToken):
					ercRet = self.pshCmd.SetByName(self, ipDict, opDict)
#setByName
					pass
				else:
					self.ProcessTSHInvalidCmd()
			else:
				print("Should not return this error. Bailing out...")
				return

#------------------------------------------------------------------------------------------------------------------------------------
	def ProcessTSHCreateNamespace(self):
		Name = self.ProcessTSHGet(suiteName="TSH", functionName="Namespace", parameterName="Name")
		for key, val in self.ns.items():
			if (Name == key):
				print("Namespace " + Name + " already exists")
			else:
				self.ns[Name] = None
		pass

	def	ProcessTSHCreateObject(self):
		Namespace = self.ProcessTSHGet(suiteName="TSH", functionName="Object", parameterName="Namespace")
		Type = self.ProcessTSHGet(suiteName="TSH", functionName="Object", parameterName="Type")
		Name = self.ProcessTSHGet(suiteName="TSH", functionName="Object", parameterName="Name")
		pass
#------------------------------------------------------------------------------------------------------------------------------------
	def ProcessTSHGet(self, **keyValDict):
		keyValTot = 0
		if keyValDict is not None:
			keyValTot = len(keyValDict)
			
		if (0 < keyValTot):    # via API call
			if (3 == keyValTot):
				for key, val in keyValDict.items():
					if (key not in ("suiteName", "functionName", "parameterName")):
						print("Invalid key value found: " + key)
						print("Valid key values are suiteName, functionName, parameterName" )
						return -1
					if (val in (None, '')):
						print("Invalid value: "  + str(val) + " supplied for " + key)
						return -1
					#print (key, '==>', value)
				suiteName = keyValDict["suiteName"]
				funcName =  keyValDict["functionName"]
				parName = keyValDict["parameterName"]			
			elif (1 == keyValTot):
				for key, val in keyValDict.items():
					if (key not in ("parameterName")):
						print("Invalid key value found: " + key)
						print("Valid key values are parameterName")
						return -1
					if (val in (None, '')):
						print("Invalid value: "  + str(val) + " supplied for " + key)
						return -1
				parName = keyValDict["parameterName"]

				#the following two calls are recursive in nature.
				#we can always pull them out and create+populate variables for ex. self.suiteName & self.funcName
				suiteName = self.SuiteInScope   #self.ProcessTSHGet(suiteName="TSH", functionName="TSH", parameterName="SuiteInScope")
				funcName = self.FunctionInScope #self.ProcessTSHGet(suiteName="TSH", functionName="TSH", parameterName="FunctionInScope")
				retVal = self.ValidateSuiteAndFunction(suiteName, funcName)
				if (0 == retVal):
					return -1
				elif (1 == retVal):
					return -1
				elif (2 == retVal):
					return -1
				elif (2 == retVal):
					pass
				else:
					print("should not come here")
					return -1
				
			else:
				print ("Invalid # of parameters" + str(keyValTot))
				return -1

		elif (0 == keyValTot): # via get command
			suiteName = self.SuiteInScope   #self.ProcessTSHGet(suiteName="TSH", functionName="TSH", parameterName="SuiteInScope")
			funcName = self.FunctionInScope #self.ProcessTSHGet(suiteName="TSH", functionName="TSH", parameterName="FunctionInScope")
			
			
			setCmdSuiteName = self.tshTokenizer.PeekIntoArray(1)
			setCmdFunctionName = self.tshTokenizer.PeekIntoArray(2)
			setCmdParName = self.tshTokenizer.PeekIntoArray(3)
			
			if (0):
				#keeping code somewhat identical to the set command
				pass			
			else:
				#SIS = SuiteInScope
				#FIS = FunctionInScope
				
				#SIS FIS
				#0   0
				#0   1
				#1   0
				#1   1
				
				#ES = Explicit Syntax
				#IS = Implicit Syntax
				
				#     0   1 2 3 4
				#ES = set S F P V
				#IS = set P V
				
				retVal = self.ValidateSuiteAndFunction(suiteName, funcName)
				if (0 == retVal):
					if (None == setCmdParName): #IS
						print("Specify SuiteInScope and FunctionInScope to use")
						return -1
					elif (None != setCmdParName): #ES
						suiteName = self.tshTokenizer.GetNextToken()
						funcName = self.tshTokenizer.GetNextToken()
						parName = self.tshTokenizer.GetNextToken()
						pass
				elif (1 == retVal):
					if (None == setCmdParName): #IS
						print("Specify SuiteInScope and FunctionInScope to use")
						return -1
					elif (None != setCmdParName): #ES
						suiteName = self.tshTokenizer.GetNextToken()
						funcName = self.tshTokenizer.GetNextToken()
						parName = self.tshTokenizer.GetNextToken()
						pass
				elif (2 == retVal):
					if (None == setCmdParName): #IS
						print("Specify SuiteInScope and FunctionInScope to use")
						return -1
					elif (None != setCmdParName): #ES
						suiteName = self.tshTokenizer.GetNextToken()
						funcName = self.tshTokenizer.GetNextToken()
						parName = self.tshTokenizer.GetNextToken()
						pass
				elif (3 == retVal):
					if (None == setCmdParName): #IS
						parName = self.tshTokenizer.GetNextToken()
						pass
					elif (None != setCmdParName): #ES
						suiteName = self.tshTokenizer.GetNextToken()
						funcName = self.tshTokenizer.GetNextToken()
						parName = self.tshTokenizer.GetNextToken()
						pass
				else:
					print("should not come here")
					return -1
		else:
			print ("should not come here")
			return -1

		tPSHSuite = self.PSHInst0.GetSuite(suiteName, "no")
		if (tPSHSuite is None):
			if (self.silentMode == False):
				print ("Suite: " + suiteName + " does not exist")
			if ("on" != self.batchMode):
				self.PSHInst0.ShowSuites()
				
			
		else:
			tPSHFunc = tPSHSuite.GetFunc(funcName, "no")
			if (tPSHFunc is None):
				if (self.silentMode == False):
					print ("Function: " + funcName + " does not exist")
				if ("on" == self.batchMode):
					print ("Valid values are:")
					tPSHSuite.ShowFuncs()
			else:
				tPSHPar = tPSHFunc.GetPar(parName, "no")
				if (tPSHPar is None):
					if (self.silentMode == False):
						print ("Parameter: " + parName + " does not exist")
					if ("on" == self.batchMode):
						print ("Valid values are:")
						tPSHFunc.ShowPars()
						#return None
				else:
					parVal = tPSHPar.GetParVal()
					return (parVal)
			return None
		return None

#					print("suiteName and funcName is set to None")
#					print("Using API call, if you want to exercise getting of parameter values,")
#					print("without entering suiteName and functionName arguments")
#					print("then you have to enter both suiteName and funcName using the set command")
#					print("either via API or via command line")
	
#------------------------------------------------------------------------------------------------------------------------------------

	def ProcessTSHSet(self, **keyValDict):
		createMetadataOnTheFly = self.ProcessTSHGet(suiteName="TSH",
												functionName="TSH",
												parameterName="createMetadataOnTheFly")
		cmdLineMode	= self.ProcessTSHGet(suiteName="TSH",
												functionName="TSH",
												parameterName="cmdLineMode")
		keyValTot = 0
		if keyValDict is not None:
			keyValTot = len(keyValDict)
			
		if (0 < keyValTot):    # via API call
			if (4 == keyValTot):
				for key, val in keyValDict.items():
					if (key not in ("suiteName", "functionName", "parameterName", "parameterValue")):
						print("Invalid key value found: " + key)
						print("Valid key values are suiteName, functionName, parameterName" )
						return -1
					if (val in (None, '')):
						print("Invalid value: "  + str(val) + " supplied for " + key)
						return -1
				suiteName = keyValDict["suiteName"]
				funcName = keyValDict["functionName"]
				parName = keyValDict["parameterName"]
				parVal = keyValDict["parameterValue"]
				
			elif (2 == keyValTot):
				for key, val in keyValDict.items():
					if (key not in ("parameterName", "parameterValue")):
						print("Invalid key value found: " + key)
						print("Valid key values are parameterName parameterValue")
						return -1
					if (val in (None, '')):
						print("Invalid value: "  + str(val) + " supplied for " + key)
						return -1
				parName = keyValDict["parameterName"]
				parVal = keyValDict["parameterValue"]

				suiteName = self.ProcessTSHGet(suiteName="TSH", functionName="TSH", parameterName="SuiteInScope")
				funcName = self.ProcessTSHGet(suiteName="TSH", functionName="TSH", parameterName="FunctionInScope")
				retVal = self.ValidateSuiteAndFunction(suiteName, funcName)

				if (0 == retVal):
					return -1					
				elif (1 == retVal):
					return -1
				elif (2 == retVal):
					return -1
				elif (3 == retVal):
					pass
				else:
					print("should not come here")
					return -1					
			else:
				print ("Invalid # of parameters" + str(keyValTot))
				return -1

		elif (0 == keyValTot): # via set command
			
			suiteName = self.ProcessTSHGet(suiteName="TSH", functionName="TSH", parameterName="SuiteInScope")
			funcName = self.ProcessTSHGet(suiteName="TSH", functionName="TSH", parameterName="FunctionInScope")
			
			
			setCmdSuiteName = self.tshTokenizer.PeekIntoArray(1)
			setCmdFunctionName = self.tshTokenizer.PeekIntoArray(2)
			setCmdParName = self.tshTokenizer.PeekIntoArray(3)
			setCmdParVal = self.tshTokenizer.PeekIntoArray(4)
			
			if 	(		("TSH" == setCmdSuiteName)
				and 	("TSH" == setCmdFunctionName)
				and 	(	("SuiteInScope" == setCmdParName)
							or
							("FunctionInScope" == setCmdParName)
						)
				):
				suiteName = self.tshTokenizer.GetNextToken()
				funcName = self.tshTokenizer.GetNextToken()
				parName = self.tshTokenizer.GetNextToken()
				parVal = self.tshTokenizer.GetNextToken(cmdLineMode)
				pass

			elif 	(	("TSH" == suiteName)
				and 	("TSH" == funcName)
				and		(None == setCmdParName)
				and 	(	("SuiteInScope" == setCmdSuiteName)
							or
							("FunctionInScope" == setCmdSuiteName)
						)
				):
				parName = self.tshTokenizer.GetNextToken()
				parVal = self.tshTokenizer.GetNextToken(cmdLineMode)
				pass			
			
			else:
				#SIS = SuiteInScope
				#FIS = FunctionInScope
				
				#SIS FIS
				#0   0
				#0   1
				#1   0
				#1   1
				
				#ES = Explicit Syntax
				#IS = Implicit Syntax
				
				#     0   1 2 3 4
				#ES = set S F P V
				#IS = set P V
				
				retVal = self.ValidateSuiteAndFunction(suiteName, funcName)
				if (0 == retVal):
					if (None == setCmdParName): #IS
						print("Specify SuiteInScope and FunctionInScope to use")
						return -1
					elif (None != setCmdParName): #ES
						suiteName = self.tshTokenizer.GetNextToken()
						funcName = self.tshTokenizer.GetNextToken()
						parName = self.tshTokenizer.GetNextToken()
						parVal = self.tshTokenizer.GetNextToken(cmdLineMode)
						pass
				elif (1 == retVal):
					if (None == setCmdParName): #IS
						print("Specify SuiteInScope and FunctionInScope to use")
						return -1
					elif (None != setCmdParName): #ES
						suiteName = self.tshTokenizer.GetNextToken()
						funcName = self.tshTokenizer.GetNextToken()
						parName = self.tshTokenizer.GetNextToken()
						parVal = self.tshTokenizer.GetNextToken(cmdLineMode)
						pass
				elif (2 == retVal):
					if (None == setCmdParName): #IS
						print("Specify SuiteInScope and FunctionInScope to use")
						return -1
					elif (None != setCmdParName): #ES
						suiteName = self.tshTokenizer.GetNextToken()
						funcName = self.tshTokenizer.GetNextToken()
						parName = self.tshTokenizer.GetNextToken()
						parVal = self.tshTokenizer.GetNextToken(cmdLineMode)
						pass
				elif (3 == retVal):
					if (None == setCmdParName): #IS
						parName = self.tshTokenizer.GetNextToken()
						parVal = self.tshTokenizer.GetNextToken(cmdLineMode)
						pass
					elif (None != setCmdParName): #ES
						suiteName = self.tshTokenizer.GetNextToken()
						funcName = self.tshTokenizer.GetNextToken()
						parName = self.tshTokenizer.GetNextToken()
						parVal = self.tshTokenizer.GetNextToken(cmdLineMode)
						pass
				else:
					print("should not come here")
					return -1
		else:
			print ("should not come here")
			return -1

		tPSHSuite = self.PSHInst0.GetSuite(suiteName, createMetadataOnTheFly)
		if (tPSHSuite is None):
			if (self.silentMode == False):
				print ("Suite: " + suiteName + " does not exist")
			if ("on" == self.batchMode):
				print ("Valid values are:")
				self.PSHInst0.ShowSuites()
		else:
			tPSHFunc = tPSHSuite.GetFunc(funcName, createMetadataOnTheFly)
			if (tPSHFunc is None):
				if (self.silentMode == False):
					print ("Function: " + funcName + " does not exist")
				if ("on" == self.batchMode):
					print ("Valid values are:")
					tPSHSuite.ShowFuncs()
			else:
				tPSHPar = tPSHFunc.GetPar(parName, createMetadataOnTheFly)
				if (tPSHPar is None):
					if (self.silentMode == False):
						print ("Parameter: " + parName + " does not exist")
					if ("on" == self.batchMode):
						print ("Valid values are:")
						tPSHFunc.ShowPars()
				else:
					tPSHPar.SetParVal(parVal)
#------------------------------------------------------------------------------------------------------------------------------------

	def	ZipDirectory(self):
		dirName = "/home/alex/stage"
		zipFileName = '/home/alex/stage/sampleDir.zip' 
		# create a ZipFile object
		with ZipFile(zipFileName, 'w') as zipObj:
			# Iterate over all the files in directory
			for folderName, subfolders, filenames in os.walk(dirName):
				for filename in filenames:
					#create complete filepath of file in directory
					filePath = os.path.join(folderName, filename)
					print(filePath)
					# Add file to zip
					zipObj.write(filePath, basename(filePath))
	
		# close the Zip File
		zipObj.close()
#------------------------------------------------------------------------------------------------------------------------------------

	def	TestTSHExcel(self):
		file_path = "/home/alex/learn/python/data/xls/yaml03.xlsm"
		vTSHxmltodict = TSHxmltodict()
		vTSHxmltodict.GetSheetsInfo(file_path)
		
		vTSHxlrd = TSHxlrd()
		vTSHxlrd.GetSheetsInfo(file_path)
		
		vTSHpandas = TSHpandas()
		vTSHpandas.GetSheetsInfo(file_path)
		
#------------------------------------------------------------------------------------------------------------------------------------

	def ProcessGetData(self, ipDict, opDict):
		rMD = RecurseMD()
		rMD.MDKDelimiter = self.ProcessTSHGet(suiteName="WB", functionName="getData", parameterName="MDKDelimiter")
		rMD.UDKDelimiter = self.ProcessTSHGet(suiteName="WB", functionName="getData", parameterName="UDKDelimiter")
		if (None == rMD.MDKDelimiter):
			rMD.MDKDelimiter = c.TSH_MDKDelimiter
		if (None == rMD.UDKDelimiter):
			rMD.UDKDelimiter = c.TSH_UDKDelimiter
		
		rMD.udFile = self.ProcessTSHGet(suiteName="WB", functionName="getData", parameterName="udFile")
		#rMD.udFile = self.ProcessTSHGet(suiteName="WB", functionName="getData", parameterName="udFile")
		rMD.mdFile = self.ProcessTSHGet(suiteName="WB", functionName="getData", parameterName="mdFile")		
		
		rMD.sheetName = self.ProcessTSHGet(suiteName="WB", functionName="getData", parameterName="sheetName")
		
		rMD.budKey = self.ProcessTSHGet(suiteName="WB", functionName="getData", parameterName="budKey")
		rMD.udKey = self.ProcessTSHGet(suiteName="WB", functionName="getData", parameterName="udKey")
		rMD.mdKey = self.ProcessTSHGet(suiteName="WB", functionName="getData", parameterName="mdKey")
		
		rMD.mdkType = self.ProcessTSHGet(suiteName="WB", functionName="getData", parameterName="mdkType")
		rMD.udkType = self.ProcessTSHGet(suiteName="WB", functionName="getData", parameterName="udkType")
		
		rMD.indentWidth = self.ProcessTSHGet(suiteName="WB", functionName="getData", parameterName="indentWidth")
		rMD.indentWithChar = self.ProcessTSHGet(suiteName="WB", functionName="getData", parameterName="indentWithChar")

		rMD.funcNameToProcessTreeNode = self.ProcessTSHGet(suiteName="WB", functionName="getData", parameterName="funcNameToProcessTreeNode")
		
		rMD.TwareComment = self.TwareComment
		rMD.DwareComment = self.DwareComment
		rMD.MwareComment = self.MwareComment
		rMD.THarnComment = self.THarnComment
		#rMD.funcAddr = self.GetFunctionAddr("AppRegisteredFunction")
		rMD.funcAddr = GetFunctionAddr(self, rMD.funcNameToProcessTreeNode)
		
		ipDict["gwObj"] = TSHSelenium()
		#ipDict["DriverObj"] = self
		rMD.mainFunc(ipDict, opDict)
	
#------------------------------------------------------------------------------------------------------------------------------------
	def ProcessTSHComment(self):
		self.tshTokenizer.InvalidateLine()
		
#------------------------------------------------------------------------------------------------------------------------------------
	def ProcessTSHInvalidCmd(self):
		self.tshTokenizer.InvalidateLine()
		print ("Invalid command:", self.cmdToken)

#------------------------------------------------------------------------------------------------------------------------------------
	def ProcessTSHAlias(self):
		pass
	
#------------------------------------------------------------------------------------------------------------------------------------
	def ProcessTSHReturn(self):
		self.tshTokenizer.TSHReturn ()

#------------------------------------------------------------------------------------------------------------------------------------
	def ProcessTSHScriptRun(self):
		scriptFileName = self.tshTokenizer.GetNextToken()
		self.tshTokenizer.TSHScriptRun (scriptFileName)
		
#------------------------------------------------------------------------------------------------------------------------------------
	def ProcessTSHMacroRun(self):
		macroFileName = self.tshTokenizer.GetNextToken()
		self.tshTokenizer.TSHMacroRun (macroFileName)
	
#------------------------------------------------------------------------------------------------------------------------------------
	def ExecAFuncAddr(self, f):
		f()

#------------------------------------------------------------------------------------------------------------------------------------
	def FutureWrappers(self):
		#ipFHInd += 1
		#ipFHArr.insert(ipFHInd, open(lineTokArr[1], "rt"))

		#print (locals())
		#print (keyValDict)
		
	#ipFHArr.append(open(lineTokArr[1], "rt"))
	#ipFHArr[ipFHInd] = open(lineTokArr[1], "rt")
		if (0):
			self.pshDir.PSHcwd()
			print(self.pshDir.__file__)
			parVal = self.ProcessTSHGet(suiteName="YAML", functionName="cwd", parameterName="fileName")
			print("parVal" + parVal)
			self.pshYAML.FileNameSet(parVal)

			parVal = self.ProcessTSHGet(suiteName="YAML", functionName="cwd", parameterName="sort_keys")
			self.pshYAML.sort_keysSet(self.TSHConvertStrToBool(parVal))
			
			#self.pshYAML.TSHYAMLLoad()
			self.pshYAML.TSHYAMLFullLoad()
			#self.pshYAML.TSHYAMLDump()
			#self.pshYAML.TSHYAMLDump02()
	
#------------------------------------------------------------------------------------------------------------------------------------

	def PrintMsg(self, msg, paramLst):
		print (msg, paramLst)
#------------------------------------------------------------------------------------------------------------------------------------


	def	getMatchingKeys(self, ipDict, opDict):
		MwareKeyAss  = ipDict["MwareKeyAss"]
		MDKDelimiter = ipDict["MDKDelimiter"]
		driverObj    = ipDict["DriverObj"]
		nodeVctAss   = ipDict["nodeVct"]

		outputAss = {}
		MwareKeyInd = 0

		for key, val in (MwareKeyAss.items()):
			found = True
			print("key" + key + ":val:" + val)
			MwareKeyTokArr = val.split(MDKDelimiter)
			for nodeVctKey, nodeVctKeyVal in (nodeVctAss.items()):
				nodeVctInd = nodeVctKey - 1
				if (nodeVctInd < len(MwareKeyTokArr)):
					if (MwareKeyTokArr[nodeVctInd] == nodeVctKeyVal):
						print (nodeVctKeyVal)
					else:
						found = False
						print (MwareKeyTokArr[nodeVctInd] + ":" + nodeVctKeyVal)
						break
				else:
					found = False
			if (True == found):
				outputAss[key] = val
		
		opDict["outputAss"] = outputAss
		pass
#------------------------------------------------------------------------------------------------------------------------------------
	
	def CBFuncForSelAuto(self, ipDict, opDict):
		yamlOPFile   = ipDict["yamlOPFile"]
		xlsOPFileObj = ipDict["xlsOPFileObj"] 
		padStr       = ipDict["padStr"]
		MwareKeyAss  = ipDict["MwareKeyAss"]
		MwareDatAss  = ipDict["MwareDatAss"]
		dataVal      = ipDict["dataVal"]
		#if ipDict.has_key("bdataVal"):
		if "bdataVal" in ipDict:
			bdataVal     = ipDict["bdataVal"]
		else:
			bdataVal     = None
		childCount   = ipDict["childCount"]
		MDKDelimiter = ipDict["MDKDelimiter"]
		UDKDelimiter = ipDict["UDKDelimiter"]
		driverObj    = ipDict["DriverObj"]
		gwObj        = ipDict["gwObj"]
		SyntaxList   = ipDict["SyntaxList"]
		xlsRow       = xlsOPFileObj.xlsRow
		xlsCol       = 1
		
		
		nodeVct = {2: "BrowserInfo"}
		ipDict["nodeVct"] = nodeVct
		ercRet = self.getMatchingKeys(ipDict, opDict)

		nodeVct = {3: "defaultFindCriteria"}
		ipDict["nodeVct"] = nodeVct
		ipDict["MwareKeyAss"] = opDict["outputAss"]
		ercRet = self.getMatchingKeys(ipDict, opDict)
		


		#get columns for base and version for a row with  input = attribute
		
		
		ipDict["MwareKeyAss"] = opDict["outputAss"]
		leafNodeName = driverObj.ProcessTSHGet(suiteName="WB", functionName="getData", parameterName="leafNodeName")
		baseNodeName = driverObj.ProcessTSHGet(suiteName="WB", functionName="getData", parameterName="baseNodeName")
		
		ipDict["baseNodeName"] = baseNodeName
		ipDict["leafNodeName"] = leafNodeName
		ipDict["attrStr"]      = "id"
		val = self.GetMDInfo(ipDict, opDict)
		
		#get value for key.attribute = defaultFindCriteria
		#where key.table = BrowserInfo
		#and mdKey = any
		
		
		gwObj.TSHSelFindElement
		AttributeNameBaseCol, AttributeNameVerCol = self.GetMDBaseAndVerRowInd(ipDict, opDict)
		
		ipDict["baseCol"]      = AttributeNameBaseCol
		ipDict["verCol"]       = AttributeNameVerCol
		AttributeNameVal = self.GetMDVal(ipDict, opDict)
				
		nodeVct = ["FusionUI", "FusionUI", "SyntaxId"]

		ipDict["nodeVct"]      = nodeVct
		SyntaxIdBaseCol = self.GetMDRowIndWithFullVct(ipDict, opDict)
		
		ipDict["baseCol"]      = SyntaxIdBaseCol
		ipDict["verCol"]       = -1
		SyntaxId = self.GetMDVal(ipDict, opDict)
				
		if (None == dataVal):
			dataVal = ""
		#print(str(SyntaxId) + ":" + str(dataVal))

		if (SyntaxId is not None):
			xRec = self.LookupSyntaxRec(SyntaxList, SyntaxId)
			if (xRec is not None):
				action = xRec.GetAction()
				resourceType = xRec.GetResourceType()
				
				print(padStr + str(action) + " " + str(resourceType) + " " + str(AttributeNameVal) + "= " + str(dataVal))
				xlsOPFileObj.WSCellWrite(xlsRow, xlsCol, str(action))
				xlsOPFileObj.WSCellWrite(xlsRow, xlsCol+1, str(resourceType))
				xlsOPFileObj.WSCellWrite(xlsRow, xlsCol+2, str(AttributeNameVal))
				xlsOPFileObj.WSCellWrite(xlsRow, xlsCol+3, "=")
				xlsOPFileObj.WSCellWrite(xlsRow, xlsCol+4, str(dataVal))
				xlsOPFileObj.xlsRow = xlsRow + 1
				if (action is not None):
					#opStr += xRec.GetAction() + " "
					pass
				if (resourceType is not None):
					#opStr += xRec.GetResourceType() + " "
					pass
			else:
				print("SyntaxId not specified")

#------------------------------------------------------------------------------------------------------------------------------------
	def	GetMDValFromSS(self, ipDict, opDict):
		MwareKeyAss  = ipDict["MwareKeyAss"]
		MwareDatAss  = ipDict["MwareDatAss"]
		MDKDelimiter = ipDict["MDKDelimiter"]
		UDKDelimiter = ipDict["UDKDelimiter"]
		driverObj    = ipDict["DriverObj"]
		leafNodeName = ipDict["leafNodeName"]
		attrStr      = ipDict["attrStr"]
		baseCol      = ipDict["baseCol"]
		verCol       = ipDict["verCol"]
		col          = ipDict["col"]
		sheetObj     = ipDict["sheetObj"]

		if (-1 == verCol):
			if (-1 == baseCol):
				print("both base and custom MD is not defined")
				val = None
				pass
			else:
				val = sheetObj.cell(int(baseCol), col).value
				pass
		else:
			if (-1 == baseCol):
				val = sheetObj.cell(int(verCol), col).value
				pass
			else:
				baseVal = sheetObj.cell(int(baseCol), col).value
				verVal  = sheetObj.cell(int(verCol), col).value
				if (None != verVal):
					if (None != baseVal):
						val = verVal
					else:
						val = verVal
				else:
					if (None != baseVal):
						val = baseVal
					else:
						val = None
							
		#if (val is None): val = "None"
		return(val)
	
#------------------------------------------------------------------------------------------------------------------------------------
	def	GetMDVal(self, ipDict, opDict):
		#yamlOPFile   = ipDict["yamlOPFile"]
		#padStr       = ipDict["padStr"]
		MwareKeyAss  = ipDict["MwareKeyAss"]
		MwareDatAss  = ipDict["MwareDatAss"]
		#dataVal      = ipDict["dataVal"]
		#childCount   = ipDict["childCount"]
		MDKDelimiter = ipDict["MDKDelimiter"]
		UDKDelimiter = ipDict["UDKDelimiter"]
		driverObj    = ipDict["DriverObj"]
		leafNodeName = ipDict["leafNodeName"]
		attrStr      = ipDict["attrStr"]
		baseCol      = ipDict["baseCol"]
		verCol       = ipDict["verCol"]
		takeTheNonNoneVal = "" #ipDict["takeTheNonNoneVal"]
		
		if (-1 == verCol):
			if (-1 == baseCol):
				print("both base and custom MD is not defined")
				val = ""
				pass
			else:
				val = MwareDatAss[baseCol]
				pass
		else:
			if (-1 == baseCol):
				val = MwareDatAss[verCol]
				pass
			else:
				if (verCol is None):
					if (baseCol is None):
						val = MwareDatAss[verCol]
						pass
					else:
						val = MwareDatAss[baseCol]
						pass
				else:
					if (0):
						if (takeTheNonNoneVal == "y"):
							if (None == MwareDatAss[verCol]):
								val = MwareDatAss[baseCol]
							if (None == MwareDatAss[baseCol]):
								val = MwareDatAss[verCol]
						else:
							val = MwareDatAss[verCol]
					if (None == MwareDatAss[verCol]):
						val = MwareDatAss[baseCol]
					else:
						val = MwareDatAss[verCol]
				pass
		return(val)
#------------------------------------------------------------------------------------------------------------------------------------

	def	GetMDRowIndWithFullVct(self, ipDict, opDict):
#		yamlOPFile   = ipDict["yamlOPFile"]
#		padStr       = ipDict["padStr"]
		MwareKeyAss  = ipDict["MwareKeyAss"]
		MwareDatAss  = ipDict["MwareDatAss"]
#		dataVal      = ipDict["dataVal"]
#		childCount   = ipDict["childCount"]
		MDKDelimiter = ipDict["MDKDelimiter"]
		UDKDelimiter = ipDict["UDKDelimiter"]
		driverObj    = ipDict["DriverObj"]
		nodeVct      = ipDict["nodeVct"]
		attrStr      = ipDict["attrStr"]

		col  = -1
		nodeNameAttr = ""
		
		nodeLen = len(nodeVct)
		for nodeInd in (range(nodeLen-1)):
			nodeNameAttr = nodeNameAttr + nodeVct[nodeInd] + MDKDelimiter
			
		nodeNameAttr  = nodeNameAttr + nodeVct[len(nodeVct)-1]
		#print("nod:" + nodeNameAttr)
		for key in (MwareKeyAss):
			val = MwareKeyAss[key]
			#print("val:" + val)
			x = val.rfind(nodeNameAttr, len(val) - len(nodeNameAttr), len(val))
			if (-1 != x):
				col = key
				
		return(col)
#------------------------------------------------------------------------------------------------------------------------------------
	def	GetMDRowIndWithVct(self, ipDict, opDict):
#		yamlOPFile   = ipDict["yamlOPFile"]
#		padStr       = ipDict["padStr"]
		MwareKeyAss  = ipDict["MwareKeyAss"]
		MwareDatAss  = ipDict["MwareDatAss"]
#		dataVal      = ipDict["dataVal"]
#		childCount   = ipDict["childCount"]
		MDKDelimiter = ipDict["MDKDelimiter"]
		UDKDelimiter = ipDict["UDKDelimiter"]
		driverObj    = ipDict["DriverObj"]
		nodeVct      = ipDict["nodeVct"]
		attrStr      = ipDict["attrStr"]

		col  = -1
		nodeNameAttr = ""
		
		nodeLen = len(nodeVct)
		for nodeInd in (range(nodeLen-1)):
			nodeNameAttr = nodeNameAttr + nodeVct[nodeInd] + MDKDelimiter
			
		nodeNameAttr  = nodeNameAttr + nodeVct[len(nodeVct)-1]
		#print("nod:" + nodeNameAttr)
		for key in (MwareKeyAss):
			val = MwareKeyAss[key]
			#print("val:" + val)
			x = val.rfind(nodeNameAttr, len(val) - len(nodeNameAttr), len(val))
			if (-1 != x):
				col = key
				
		return(col)
#------------------------------------------------------------------------------------------------------------------------------------

	def	FinGetMDBaseAndVerRowInd(self, ipDict, opDict):
#		yamlOPFile   = ipDict["yamlOPFile"]
#		padStr       = ipDict["padStr"]
		MwareKeyAss  = ipDict["MwareKeyAss"]
		MwareDatAss  = ipDict["MwareDatAss"]
#		dataVal      = ipDict["dataVal"]
#		childCount   = ipDict["childCount"]
		MDKDelimiter = ipDict["MDKDelimiter"]
		UDKDelimiter = ipDict["UDKDelimiter"]
		driverObj    = ipDict["DriverObj"]
		leafNodeName = ipDict["leafNodeName"]
		baseNodeName = ipDict["baseNodeName"]
		attrStr      = ipDict["attrStr"]

		debugLvl = 0
									
		baseCol = -1
		verCol  = -1
		
		if ((leafNodeName == None) or (leafNodeName == "")):
			pass
		else:
			leafNodeNameAttr = MDKDelimiter + "TSH" + MDKDelimiter + attrStr + MDKDelimiter + leafNodeName 
			for key in (MwareKeyAss):
				val = MwareKeyAss[key]
				
				x = val.rfind(leafNodeNameAttr, len(val) - len(leafNodeNameAttr), len(val))
				if (-1 != x):
					verCol = key

		if ((baseNodeName == None) or (baseNodeName == "")):
			baseNodeNameAttr = MDKDelimiter + "TSH" + MDKDelimiter + attrStr
		else:
			baseNodeNameAttr = MDKDelimiter + "TSH" + MDKDelimiter + attrStr + MDKDelimiter + baseNodeName


		for key in (MwareKeyAss):
			val = MwareKeyAss[key]
			x = val.rfind(baseNodeNameAttr, len(val) - len(baseNodeNameAttr), len(val))
			if (-1 != x):
				baseCol = key
				
		return(baseCol, verCol)

#------------------------------------------------------------------------------------------------------------------------------------
	def	GetMDBaseAndVerRowInd(self, ipDict, opDict):
#		yamlOPFile   = ipDict["yamlOPFile"]
#		padStr       = ipDict["padStr"]
		MwareKeyAss  = ipDict["MwareKeyAss"]
		MwareDatAss  = ipDict["MwareDatAss"]
#		dataVal      = ipDict["dataVal"]
#		childCount   = ipDict["childCount"]
		MDKDelimiter = ipDict["MDKDelimiter"]
		UDKDelimiter = ipDict["UDKDelimiter"]
		driverObj    = ipDict["DriverObj"]
		leafNodeName = ipDict["leafNodeName"]
		baseNodeName = ipDict["baseNodeName"]
		attrStr      = ipDict["attrStr"]

		debugLvl = 0
									
		baseCol = -1
		verCol  = -1
		
		if ((leafNodeName == None) or (leafNodeName == "")):
			pass
		else:
			leafNodeNameAttr = MDKDelimiter + "TSH" + MDKDelimiter + attrStr + MDKDelimiter + leafNodeName 
			for key in (MwareKeyAss):
				val = MwareKeyAss[key]
				
				x = val.rfind(leafNodeNameAttr, len(val) - len(leafNodeNameAttr), len(val))
				if (-1 != x):
					verCol = key

		if ((baseNodeName == None) or (baseNodeName == "")):
			baseNodeNameAttr = MDKDelimiter + "TSH" + MDKDelimiter + attrStr
		else:
			baseNodeNameAttr = MDKDelimiter + "TSH" + MDKDelimiter + attrStr + MDKDelimiter + baseNodeName


		for key in (MwareKeyAss):
			val = MwareKeyAss[key]
			x = val.rfind(baseNodeNameAttr, len(val) - len(baseNodeNameAttr), len(val))
			if (-1 != x):
				baseCol = key
				
		return(baseCol, verCol)

#------------------------------------------------------------------------------------------------------------------------------------
	def	GetMDInfo(self, ipDict, opDict):
		baseCol, verCol = self.GetMDBaseAndVerRowInd(ipDict, opDict)
		ipDict["baseCol"]      = baseCol
		ipDict["verCol"]       = verCol
		val = self.GetMDVal(ipDict, opDict)
		return (val)
	
#------------------------------------------------------------------------------------------------------------------------------------

	def	ValidateSuiteAndFunction(self, SuiteInScope, FunctionInScope):
		if (None == SuiteInScope):
			if (None == FunctionInScope):
				retVal = 0
			elif ("None" == FunctionInScope):
				retVal = 0
			else:
				retVal = 1
		elif ("None" == SuiteInScope):
			if (None == FunctionInScope):
				retVal = 0
			elif ("None" == FunctionInScope):
				retVal = 0
			else:
				retVal = 1
		else:
			if (None == FunctionInScope):
				retVal = 2
			elif ("None" == FunctionInScope):
				retVal = 2
			else:
				retVal = 3
				pass
			pass
		
		return retVal

#------------------------------------------------------------------------------------------------------------------------------------

	def ProcessTSHRegisterSuite(self, **keyValDict):
		createMetadataOnTheFly = self.ProcessTSHGet(suiteName="TSH", functionName="TSH", parameterName="createMetadataOnTheFly")

		keyValTot = len(keyValDict)
		if (1 == keyValTot):
			if keyValDict is not None:
				for key, val in keyValDict.items():
					if (key not in ("suiteName")):
						print("Invalid key value found: " + key)
						print("Valid key values is suiteName")
						return
					if (val in (None, '')):
						print("Invalid value: "  + str(val) + " supplied for " + key)
						return
				suiteName = keyValDict["suiteName"]
		else:
			suiteName = self.tshTokenizer.GetNextToken()
		
		
		
		tPSHSuite = self.PSHInst0.GetSuite(suiteName, createMetadataOnTheFly)
		if (tPSHSuite is None):
			self.PSHInst0.AddSuite(suiteName)
		else:
			if (self.silentMode == False):
				print ("Suite: " + suiteName + " already exists")
			
#------------------------------------------------------------------------------------------------------------------------------------

	def ProcessTSHRegisterFunction(self, **keyValDict):
		createMetadataOnTheFly = self.ProcessTSHGet(suiteName="TSH", functionName="TSH", parameterName="createMetadataOnTheFly")
		keyValTot = len(keyValDict)
		if (2 == keyValTot):
			if keyValDict is not None:
				for key, val in keyValDict.items():
					if (key not in ("suiteName", "functionName")):
						print("Invalid key value found: " + key)
						print("Valid key values are suiteName, functionName" )
						return
					if (val in (None, '')):
						print("Invalid value: "  + str(val) + " supplied for " + key)
						return
				suiteName = keyValDict["suiteName"]
				funcName = keyValDict["functionName"]
		else:
			suiteName = self.tshTokenizer.GetNextToken()
			funcName = self.tshTokenizer.GetNextToken()
		
		tPSHSuite = self.PSHInst0.GetSuite(suiteName, createMetadataOnTheFly)
		if (tPSHSuite is None):
			if (self.silentMode == False):
				print ("Suite: " + suiteName + " does not exist")
			if ("on" == self.batchMode):
				print ("Valid values are:")
				self.PSHInst0.ShowSuites()
		else:
			tPSHFunc = tPSHSuite.GetFunc(funcName, createMetadataOnTheFly)
			if (tPSHFunc is None):
				tPSHSuite.AddFunc(funcName)
			else:
				if (self.silentMode == False):
					print ("Function: " + funcName + " already exists")

#------------------------------------------------------------------------------------------------------------------------------------

	def ProcessTSHRegisterParameter(self, **keyValDict):
		createMetadataOnTheFly = self.ProcessTSHGet(suiteName="TSH", functionName="TSH", parameterName="createMetadataOnTheFly")
		keyValTot = len(keyValDict)
		if (3 == keyValTot):
			if keyValDict is not None:
				for key, val in keyValDict.items():
					if (key not in ("suiteName", "functionName", "parameterName")):
						print("Invalid key value found: " + key)
						print("Valid key values are suiteName, functionName, parameterName" )
						return
					if (val in (None, '')):
						print("Invalid value: "  + str(val) + " supplied for " + key)
						return
				suiteName = keyValDict["suiteName"]
				funcName = keyValDict["functionName"]
				parName = keyValDict["parameterName"]
		else:
			suiteName = self.tshTokenizer.GetNextToken()
			funcName = self.tshTokenizer.GetNextToken()
			parName = self.tshTokenizer.GetNextToken()
		
		tPSHSuite = self.PSHInst0.GetSuite(suiteName, createMetadataOnTheFly)
		if (tPSHSuite is None):
			if (self.silentMode == False):
				print ("Suite: " + suiteName + " does not exist")
			if ("on" == self.batchMode):
				print ("Valid values are:")
				self.PSHInst0.ShowSuites()
		else:
			tPSHFunc = tPSHSuite.GetFunc(funcName, createMetadataOnTheFly)
			if (tPSHFunc is None):
				if (self.silentMode == False):
					print ("Function: " + funcName + " does not exist")
				if ("on" == self.batchMode):
					print ("Valid values are:")
					tPSHSuite.ShowFuncs()
			else:
				tPSHPar = tPSHFunc.GetPar(parName, createMetadataOnTheFly)
				if (tPSHPar is None):
					tPSHFunc.AddPar(parName)
				else:
					if (self.silentMode == False):
						print ("Parameter: " + parName + " already exists")

#------------------------------------------------------------------------------------------------------------------------------------

	def	SetupCommentMD(self):
		self.silentMode = True
		self.ProcessTSHRegisterSuite(suiteName="TSH")
		
		self.ProcessTSHRegisterFunction(suiteName="TSH", functionName="TSH")
		
		self.ProcessTSHRegisterParameter(suiteName="TSH", functionName="TSH", parameterName="batchMode")
		self.ProcessTSHSet(suiteName="TSH", functionName="TSH", parameterName="batchMode", parameterValue="on")
		
		self.ProcessTSHRegisterParameter(suiteName="TSH", functionName="TSH", parameterName="createMetadataOnTheFly")
		self.ProcessTSHSet(suiteName="TSH", functionName="TSH", parameterName="createMetadataOnTheFly", parameterValue="no")

		self.ProcessTSHRegisterParameter(suiteName="TSH", functionName="TSH", parameterName="cmdLineMode")
		self.ProcessTSHSet(suiteName="TSH", functionName="TSH", parameterName="cmdLineMode", parameterValue="off")
		
		self.silentMode = False


		self.ProcessTSHRegisterParameter(suiteName="TSH", functionName="TSH", parameterName="SuiteInScope")
		self.ProcessTSHSet(suiteName="TSH", functionName="TSH", parameterName="SuiteInScope", parameterValue="None")

		self.ProcessTSHRegisterParameter(suiteName="TSH", functionName="TSH", parameterName="FunctionInScope")
		self.ProcessTSHSet(suiteName="TSH", functionName="TSH", parameterName="FunctionInScope", parameterValue="None")



		self.ProcessTSHRegisterFunction(suiteName="TSH", functionName="Tware")
		self.ProcessTSHRegisterFunction(suiteName="TSH", functionName="Dware")
		self.ProcessTSHRegisterFunction(suiteName="TSH", functionName="Mware")
		self.ProcessTSHRegisterFunction(suiteName="TSH", functionName="THarn")
		
		self.ProcessTSHRegisterParameter(suiteName="TSH", functionName="Tware", parameterName="singleComment")
		self.ProcessTSHRegisterParameter(suiteName="TSH", functionName="Tware", parameterName="multipleCommentBegin")
		self.ProcessTSHRegisterParameter(suiteName="TSH", functionName="Tware", parameterName="multipleCommentEnd")

		self.ProcessTSHRegisterParameter(suiteName="TSH", functionName="Dware", parameterName="singleComment")
		self.ProcessTSHRegisterParameter(suiteName="TSH", functionName="Dware", parameterName="multipleCommentBegin")
		self.ProcessTSHRegisterParameter(suiteName="TSH", functionName="Dware", parameterName="multipleCommentEnd")

		self.ProcessTSHRegisterParameter(suiteName="TSH", functionName="Mware", parameterName="singleComment")
		self.ProcessTSHRegisterParameter(suiteName="TSH", functionName="Mware", parameterName="multipleCommentBegin")
		self.ProcessTSHRegisterParameter(suiteName="TSH", functionName="Mware", parameterName="multipleCommentEnd")

		self.ProcessTSHRegisterParameter(suiteName="TSH", functionName="THarn", parameterName="singleComment")
		self.ProcessTSHRegisterParameter(suiteName="TSH", functionName="THarn", parameterName="multipleCommentBegin")
		self.ProcessTSHRegisterParameter(suiteName="TSH", functionName="THarn", parameterName="multipleCommentEnd")

		self.ProcessTSHSet(suiteName="TSH", functionName="Tware", parameterName="singleComment", parameterValue=c.TSH_SingRCComment)		
		self.ProcessTSHSet(suiteName="TSH", functionName="Tware", parameterName="multipleCommentBegin", parameterValue=c.TSH_MultRCCommentBeg)
		self.ProcessTSHSet(suiteName="TSH", functionName="Tware", parameterName="multipleCommentEnd", parameterValue=c.TSH_MultRCCommentEnd)

		self.ProcessTSHSet(suiteName="TSH", functionName="Dware", parameterName="singleComment", parameterValue=c.TSH_SingRCComment)
		self.ProcessTSHSet(suiteName="TSH", functionName="Dware", parameterName="multipleCommentBegin", parameterValue=c.TSH_MultRCCommentBeg)
		self.ProcessTSHSet(suiteName="TSH", functionName="Dware", parameterName="multipleCommentEnd", parameterValue=c.TSH_MultRCCommentEnd)

		self.ProcessTSHSet(suiteName="TSH", functionName="Mware", parameterName="singleComment", parameterValue=c.TSH_SingRCComment)
		self.ProcessTSHSet(suiteName="TSH", functionName="Mware", parameterName="multipleCommentBegin", parameterValue=c.TSH_MultRCCommentBeg)
		self.ProcessTSHSet(suiteName="TSH", functionName="Mware", parameterName="multipleCommentEnd", parameterValue=c.TSH_MultRCCommentEnd)
		
		self.ProcessTSHSet(suiteName="TSH", functionName="THarn", parameterName="singleComment", parameterValue=c.TSH_SingRCComment)
		self.ProcessTSHSet(suiteName="TSH", functionName="THarn", parameterName="multipleCommentBegin", parameterValue=c.TSH_MultRCCommentBeg)
		self.ProcessTSHSet(suiteName="TSH", functionName="THarn", parameterName="multipleCommentEnd", parameterValue=c.TSH_MultRCCommentEnd)

#------------------------------------------------------------------------------------------------------------------------------------

	def InitializeComment(self):
		self.TwareComment.singCommentPat = self.ProcessTSHGet(suiteName="TSH", functionName="Tware", parameterName="singleComment")
		if (None == self.TwareComment.singCommentPat):
			exitLoop = True
			return (-1, exitLoop, False)
		
		self.TwareComment.multCommentBegPat = self.ProcessTSHGet(suiteName="TSH", functionName="Tware", parameterName="multipleCommentBegin")
		self.TwareComment.multCommentEndPat = self.ProcessTSHGet(suiteName="TSH", functionName="Tware", parameterName="multipleCommentEnd")
			
		if (not((None == self.TwareComment.multCommentBegPat) and (None == self.TwareComment.multCommentEndPat)
			or  (None != self.TwareComment.multCommentBegPat) and (None != self.TwareComment.multCommentEndPat))):
			exitLoop = True
			return (-1, exitLoop, False)
		
		x = self.TwareComment.multCommentBegPat.find(self.TwareComment.singCommentPat)
		if (-1 != x):
			print("Please select character sequence different for single and multiple Rows to keep things simpler")
			exitLoop = True
			return (-1, exitLoop, False)
		
		x = self.TwareComment.multCommentEndPat.find(self.TwareComment.singCommentPat)
		if (-1 != x):
			print("Please select character sequence different for single and multiple Rows to keep things simpler")
			exitLoop = True
			return (-1, exitLoop, False)

#----------------------------------------------------------------------------------------------------------------
		self.DwareComment.singCommentPat = self.ProcessTSHGet(suiteName="TSH", functionName="Dware", parameterName="singleComment")
		if (None == self.DwareComment.singCommentPat):
			exitLoop = True
			return (-1, exitLoop, False)
		
		self.DwareComment.multCommentBegPat = self.ProcessTSHGet(suiteName="TSH", functionName="Dware", parameterName="multipleCommentBegin")
		self.DwareComment.multCommentEndPat = self.ProcessTSHGet(suiteName="TSH", functionName="Dware", parameterName="multipleCommentEnd")
			
		if (not((None == self.DwareComment.multCommentBegPat) and (None == self.DwareComment.multCommentEndPat)
			or  (None != self.DwareComment.multCommentBegPat) and (None != self.DwareComment.multCommentEndPat))):
			exitLoop = True
			return (-1, exitLoop, False)
		
		x = self.DwareComment.multCommentBegPat.find(self.DwareComment.singCommentPat)
		if (-1 != x):
			print("Please select character sequence different for single and multiple Column to keep things simpler")
			exitLoop = True
			return (-1, exitLoop, False)
		
		x = self.DwareComment.multCommentEndPat.find(self.DwareComment.singCommentPat)
		if (-1 != x):
			print("Please select character sequence different for single and multiple Column to keep things simpler")
			exitLoop = True
			return (-1, exitLoop, False)
#-------------------------------------------------------------------------------------------------------------------------------------
		self.MwareComment.singCommentPat = self.ProcessTSHGet(suiteName="TSH", functionName="Mware", parameterName="singleComment")
		if (None == self.MwareComment.singCommentPat):
			exitLoop = True
			return (-1, exitLoop, False)
		
		self.MwareComment.multCommentBegPat = self.ProcessTSHGet(suiteName="TSH", functionName="Mware", parameterName="multipleCommentBegin")
		self.MwareComment.multCommentEndPat = self.ProcessTSHGet(suiteName="TSH", functionName="Mware", parameterName="multipleCommentEnd")
			
		if (not((None == self.MwareComment.multCommentBegPat) and (None == self.MwareComment.multCommentEndPat)
			or  (None != self.MwareComment.multCommentBegPat) and (None != self.MwareComment.multCommentEndPat))):
			exitLoop = True
			return (-1, exitLoop, False)
		
		x = self.MwareComment.multCommentBegPat.find(self.MwareComment.singCommentPat)
		if (-1 != x):
			print("Please select character sequence different for single and multiple Column to keep things simpler")
			exitLoop = True
			return (-1, exitLoop, False)
		
		x = self.MwareComment.multCommentEndPat.find(self.MwareComment.singCommentPat)
		if (-1 != x):
			print("Please select character sequence different for single and multiple Column to keep things simpler")
			exitLoop = True
			return (-1, exitLoop, False)

#----------------------------------------------------------------------------------------------------------------

		self.THarnComment.singCommentPat = self.ProcessTSHGet(suiteName="TSH", functionName="THarn", parameterName="singleComment")
		if (None == self.THarnComment.singCommentPat):
			exitLoop = True
			return (-1, exitLoop, False)
		
		self.THarnComment.multCommentBegPat = self.ProcessTSHGet(suiteName="TSH", functionName="THarn", parameterName="multipleCommentBegin")
		self.THarnComment.multCommentEndPat = self.ProcessTSHGet(suiteName="TSH", functionName="THarn", parameterName="multipleCommentEnd")
			
		if (not((None == self.THarnComment.multCommentBegPat) and (None == self.THarnComment.multCommentEndPat)
			or  (None != self.THarnComment.multCommentBegPat) and (None != self.THarnComment.multCommentEndPat))):
			exitLoop = True
			return (-1, exitLoop, False)
		
		x = self.THarnComment.multCommentBegPat.find(self.THarnComment.singCommentPat)
		if (-1 != x):
			print("Please select character sequence different for single and multiple Column to keep things simpler")
			exitLoop = True
			return (-1, exitLoop, False)
		
		x = self.THarnComment.multCommentEndPat.find(self.THarnComment.singCommentPat)
		if (-1 != x):
			print("Please select character sequence different for single and multiple Column to keep things simpler")
			exitLoop = True
			return (-1, exitLoop, False)

#----------------------------------------------------------------------------------------------------------------
	def ReadAndUpdateSetup(self):
		self.SuiteInScope = self.ProcessTSHGet(suiteName="TSH", functionName="TSH", parameterName="SuiteInScope")
		self.FunctionInScope = self.ProcessTSHGet(suiteName="TSH", functionName="TSH", parameterName="FunctionInScope")
		self.batchMode = self.ProcessTSHGet(suiteName="TSH", functionName="TSH", parameterName="batchMode")
		
#----------------------------------------------------------------------------------------------------------------
	def main(self):
		#setup required default settings
		#self.singRowComment = False
		#self.multRowComment = False
		#self.multRowCommentBeg = False
		#self.multRowCommentEnd = False
		self.SetupCommentMD()
		
		#initialize environment specific setup script
		self.tshTokenizer.TSHBatchModeSet(True)
		self.tshTokenizer.TSHScriptRun('../../../scripts/init/startup02.scr')
		self.ProcessInputSource()
		
		#process command line arguments to PYSH
		self.tshTokenizer.TSHBatchModeSet(True)
		self.ReadCommandLine()
		self.tshTokenizer.TSHLineRun(self.cmdLine)
		self.ProcessInputSource()
		
		#Interactively process commands
		self.tshTokenizer.TSHBatchModeSet(False)
		self.ProcessInputSource()

	def	TestFunction(self, sessionObj, ipDict, opDict, **kwargs):
		print(self)
		print(ipDict)
		print(opDict)

#------------------------------------------------------------------------------------------------------------------------------------
	def CBFuncForXSLT(self, ipDict, opDict):
		#print("Executing function: " + self.AppRegisteredFunction.__name__)

		padStr       = ipDict["padStr"]
		MwareKeyAss  = ipDict["MwareKeyAss"]
		MwareDatAss  = ipDict["MwareDatAss"]
		dataVal      = ipDict["dataVal"]
		childCount   = ipDict["childCount"]
		MDKDelimiter = ipDict["MDKDelimiter"]
		UDKDelimiter = ipDict["UDKDelimiter"]
		
	#XML		
	#XML01	
	#	BegSection
	#	EndSection
	#	BegTag
	#	EndTag
#MDNode:MwareKeyAss:26:XSLT:XSLT01:XSLT01#STEP01:DisplayName
#MDNode:MwareKeyAss:27:XSLT:XSLT01:XSLT01#STEP01:BegSection
#MDNode:MwareKeyAss:28:XSLT:XSLT01:XSLT01#STEP01:EndSection
#MDNode:MwareKeyAss:29:XSLT:XSLT01:XSLT01#STEP01:BegTag
#MDNode:MwareKeyAss:30:XSLT:XSLT01:XSLT01#STEP01:EndTag

		debugLvl = 1
		if (1==debugLvl):
			for key in (MwareKeyAss):
				if (None == MwareKeyAss[key]):
					val = ""
				else:
					val = MwareKeyAss[key]
				print("MDNode:MwareKeyAss:" + str(key) + ":" + val)
			
			for key in (MwareDatAss):
				if (None == MwareDatAss[key]):
					val = ""
				else:
					val = MwareDatAss[key]
				print("MDNode:MwareDatAss:" + str(key) + ":" + str(val) + "<EOS>")

		AttributeNameAttr = MDKDelimiter + "TSH" + MDKDelimiter + "AttributeName" 
		DataTypeAttr = MDKDelimiter + "TSH" + MDKDelimiter + "DataType"
		TabAttr = MDKDelimiter + "TSH" + MDKDelimiter + "Tab"
		
		AttributeNameCol = -1
		DataTypeCol = -1

		for key in (MwareKeyAss):
			#print("MDNode:MwareKeyAss:" + str(key) + ":" + MwareKeyAss[key])
			val = MwareKeyAss[key]
			
			x = val.rfind(AttributeNameAttr, 0, len(val))
			if (-1 != x):
				AttributeNameCol = key

			x = val.rfind(DataTypeAttr, 0, len(val))
			if (-1 != x):
				DataTypeCol = key
					

		if (None == dataVal):
			dataVal = ""
		
		keyVal = MwareDatAss[AttributeNameCol]
		
		if (None != MwareDatAss[DataTypeCol]):
			if ("array" == MwareDatAss[DataTypeCol]):
				if (childCount > 0):
					print(padStr + str(keyVal) + ":") #This line has been changed
			else:
				if (None != dataVal) and ("" != dataVal):
					print(padStr + str(keyVal) + ":" + str(dataVal))
		else:
			#print("Please specify Data Type...")
			if (None != dataVal) and ("" != dataVal):
				#str(childCount)
				print(padStr + str(keyVal) + ":" + str(dataVal))
			
#------------------------------------------------------------------------------------------------------------------------------------

	def CBFuncForYAML(self, ipDict, opDict):
		#print("Executing function: " + self.AppRegisteredFunction.__name__)
		yamlOPFile   = ipDict["yamlOPFile"]
		padStr       = ipDict["padStr"]
		MwareKeyAss  = ipDict["MwareKeyAss"]
		MwareDatAss  = ipDict["MwareDatAss"]
		dataVal      = ipDict["dataVal"]
		childCount   = ipDict["childCount"]
		MDKDelimiter = ipDict["MDKDelimiter"]
		UDKDelimiter = ipDict["UDKDelimiter"]
		driverObj    = ipDict["DriverObj"]
		
		leafNodeName = driverObj.ProcessTSHGet(suiteName="WB", functionName="getData", parameterName="leafNodeName")
		baseNodeName = driverObj.ProcessTSHGet(suiteName="WB", functionName="getData", parameterName="baseNodeName")
		
		ipDict["baseNodeName"] = baseNodeName
		ipDict["leafNodeName"] = leafNodeName
		ipDict["attrStr"]      = "AttributeName"
		AttributeNameBaseCol, AttributeNameVerCol = self.GetMDBaseAndVerRowInd(ipDict, opDict)
		
		ipDict["baseCol"]      = AttributeNameBaseCol
		ipDict["verCol"]       = AttributeNameVerCol
		AttributeNameVal = self.GetMDVal(ipDict, opDict)
		
		ipDict["attrStr"]      = "DataType"
		DataTypeBaseCol, DataTypeVerCol = self.GetMDBaseAndVerRowInd(ipDict, opDict)

		ipDict["baseCol"]      = DataTypeBaseCol
		ipDict["verCol"]       = DataTypeVerCol
		DataTypeVal = self.GetMDVal(ipDict, opDict)
		
		if (None == dataVal):
			dataVal = ""
		
		keyVal = AttributeNameVal #MwareDatAss[AttributeNameCol]
		
		if (None != DataTypeVal): #MwareDatAss[DataTypeCol]):
			if ("array" == DataTypeVal): #MwareDatAss[DataTypeCol]):
				if (childCount > 0):
					print(padStr + str(childCount) + ":" + str(keyVal) + ":")
					yamlOPFile.write(padStr + str(keyVal) + ":" + "\n")
			else:
				if (None != dataVal) and ("" != dataVal):
					print(padStr + str(childCount) + ":" + str(keyVal) + ":" + str(dataVal))
					yamlOPFile.write(padStr + str(keyVal) + ": " + str(dataVal) + "\n")
		else:
			#print("Please specify Data Type...")
			if (None != dataVal) and ("" != dataVal):
				print(padStr + str(childCount) + ":" + str(keyVal) + ":" + str(dataVal))
				yamlOPFile.write(padStr + str(keyVal) + ": " + str(dataVal) + "\n")
		
		
#------------------------------------------------------------------------------------------------------------------------------------
	
	def LookupSyntaxRec(self, SyntaxList, SyntaxID):
		totCnt = SyntaxList.GetDataNode1DLen()
		ind = 0
		while (ind < totCnt):
			tSyntaxRec = SyntaxList.GetDataNode(ind)
			if (SyntaxID == tSyntaxRec.GetSyntaxID()):
				return tSyntaxRec
			else:
				ind += 1
		return None
	#------------------------------------------------------------------------------------------- 
#------------------------------------------------------------------------------------------------------------------------------------
	def CBFuncForUIDoc(self, ipDict, opDict):
		yamlOPFile   = ipDict["yamlOPFile"]
		xlsOPFileObj = ipDict["xlsOPFileObj"] 
		padStr       = ipDict["padStr"]
		MwareKeyAss  = ipDict["MwareKeyAss"]
		MwareDatAss  = ipDict["MwareDatAss"]
		dataVal      = ipDict["dataVal"]
		#if ipDict.has_key("bdataVal"):
		if "bdataVal" in ipDict:
			bdataVal     = ipDict["bdataVal"]
		else:
			bdataVal     = None
		childCount   = ipDict["childCount"]
		MDKDelimiter = ipDict["MDKDelimiter"]
		UDKDelimiter = ipDict["UDKDelimiter"]
		driverObj    = ipDict["DriverObj"]
		SyntaxList   = ipDict["SyntaxList"]
		xlsRow       = xlsOPFileObj.xlsRow
		xlsCol       = 1
		
		leafNodeName = driverObj.ProcessTSHGet(suiteName="WB", functionName="getData", parameterName="leafNodeName")
		baseNodeName = driverObj.ProcessTSHGet(suiteName="WB", functionName="getData", parameterName="baseNodeName")
		
		ipDict["baseNodeName"] = baseNodeName
		ipDict["leafNodeName"] = leafNodeName
		ipDict["attrStr"]      = "AttributeName"
		AttributeNameBaseCol, AttributeNameVerCol = self.GetMDBaseAndVerRowInd(ipDict, opDict)
		
		ipDict["baseCol"]      = AttributeNameBaseCol
		ipDict["verCol"]       = AttributeNameVerCol
		AttributeNameVal = self.GetMDVal(ipDict, opDict)
				
		nodeVct = ["FusionUI", "FusionUI", "SyntaxId"]

		ipDict["nodeVct"]      = nodeVct
		SyntaxIdBaseCol = self.GetMDRowIndWithFullVct(ipDict, opDict)
		
		ipDict["baseCol"]      = SyntaxIdBaseCol
		ipDict["verCol"]       = -1
		SyntaxId = self.GetMDVal(ipDict, opDict)
				
		if (None == dataVal):
			dataVal = ""
		#print(str(SyntaxId) + ":" + str(dataVal))

		if (SyntaxId is not None):
			xRec = self.LookupSyntaxRec(SyntaxList, SyntaxId)
			if (xRec is not None):
				action = xRec.GetAction()
				resourceType = xRec.GetResourceType()
				
				print(padStr + str(action) + " " + str(resourceType) + " " + str(AttributeNameVal) + "= " + str(dataVal))
				xlsOPFileObj.WSCellWrite(xlsRow, xlsCol, str(action))
				xlsOPFileObj.WSCellWrite(xlsRow, xlsCol+1, str(resourceType))
				xlsOPFileObj.WSCellWrite(xlsRow, xlsCol+2, str(AttributeNameVal))
				xlsOPFileObj.WSCellWrite(xlsRow, xlsCol+3, "=")
				xlsOPFileObj.WSCellWrite(xlsRow, xlsCol+4, str(dataVal))
				xlsOPFileObj.xlsRow = xlsRow + 1
				if (action is not None):
					#opStr += xRec.GetAction() + " "
					pass
				if (resourceType is not None):
					#opStr += xRec.GetResourceType() + " "
					pass
			else:
				print("SyntaxId not specified")

#------------------------------------------------------------------------------------------------------------------------------------
#This abstraction is thought of, for the purpose of
#Interpreting the metadatakeys

	def	GetNamespaces(self):
		pass
	
	def	GetTables(self):
		pass
	
	def	GetAttributes(self):
		pass
	
	def	GetAttributeVersions(self):
		pass
	
#tshProcess = TSHProcess()
#tshProcess.TSHSubProcessRun()
#sys.path.append('/home/alex/learn/python/src/PYSH/TMD')
tshShell = TSHShell()
tshShell.main()

