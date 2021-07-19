import os
import sys
import os.path 
from pathlib import Path
from contextlib import redirect_stdout
#from PSHMD import PSHMD
#from PSHFunc import PSHFunc
#from PSHPar import PSHPar
class TSHFile:
    def __init__(self):
        self.fileFullPath    = ""
        self.fileRelPath     = ""
        self.filePath        = ""
        self.fileName        = ""
        self.baseFileName    = ""
        self.fileNameExt     = ""

        self.mode    = ""
        self.fileHdl = None
        self.isFile  = False
        self.isDir   = False
        PSHInst0 = None

    def GetFileInfo(self, filePath):
        self.fileRelPath = filePath
        self.baseFileName = Path(filePath).stem
        self.fileName=os.path.basename(filePath)
        self.baseFileName, self.fileNameExt = os.path.splitext(self.fileName)
        self.baseFileName = os.path.splitext(self.fileName)[0]
        self.fileNameExt = os.path.splitext(self.fileName)[1]
        self.fileFullPath = self.TSHabspath()
    
    def GetFileHdl(self):
        return self.fileHdl
        
    @property
    def PSHInst0(self):
        return self.__PSHInst0
    
    @PSHInst0.setter
    def PSHInst0(self, PSHInst0):
        self.__PSHInst0 = PSHInst0
                
    @property
    def filePath(self):
        return self.__filePath
    
    @filePath.setter
    def filePath(self, filePath):
        self.__filePath = filePath
        self.GetFileInfo(filePath)
        
    @property
    def mode(self):
        return self.__mode
    
    @mode.setter
    def mode(self, mode):
        self.__mode = mode
            
    def open(self, *args):
        if (self.fileFullPath != ""):
            self.fileHdl = open(self.fileFullPath, self.mode)
        
    def close(self):
        self.fileHdl.close
        #del self.fh

    def ViewFile(self):
        #print(self.name)
        #print(self.mode)    
        #self.fh = open(self.name, self.mode)
        buf = self.fileHdl.read()
        print (buf)

    def write(self, opStr):
        self.fileHdl.write(opStr)
        
    @classmethod    
    def IsFile(self):
        config = Path('..\\scripts\\startup.scr')
        if (config.is_file()):
            # Store configuration file values
            #print("In if")
            pass
        else:
            #print("In else")
            # Keep presets
            pass
        try:
            absolute_path = config.resolve()
            print(absolute_path)
            # Store configuration file values
        except FileNotFoundError:
            print("In except")
            
            # Keep presets
    
    # Brute force with a try-except block
        try: 
            fileHdl = open('..\\scripts\\startup.scr', 'r') 
        except FileNotFoundError: 
            pass
      
    # Leverage the OS package
        exists = os.path.isfile('..\\scripts\\startup.scr')
    # Wrap the path in an object for enhanced functionality
        config = Path('..\\scripts\\startup.scr') 
        if config.is_file(): 
            pass

    def redirect_stdinOutErr(self):
        with open('yourfile.txt', 'w') as f:
            with redirect_stdout(f):
                print("This is python redirect")
                redirect_stdout(sys.stdout)
        
#    def __init__(self, PSHMD):
#        self.PSHInst0 = PSHMD
        
    def TSHPathExists(self):
        return os.path.exists(self.filePath)

    
    def TSHisfile(self):
        return os.path.isfile(self.filePath)

    def TSHisdir(self):
        return os.path.isdir(self.filePath)
    
    def TSHabspath(self):
        return os.path.abspath(self.filePath)
        
    def TSHabspath02(self):
        x = Path(self.filePath)
        y = x.resolve()
        return str(y)

if __name__ == "__main__":
    tshFile = TSHFile()
    tshFile.filePath = "/path/to/some/file.txt"
    pass
       
#if __name__ == "__main__":

#PSHMod0.dynamic_importer("PSHFile", "PSHFile")


#PSHMod0 = PSHMod()
#PSHMod0.FindAndLoadModule("PSHFile", "PSHFile", PSHInst0)

#PSHInst0.AddSuite("File")
#PSHInst0.AddSuite("Database")
#PSHInst0.ShowSuites()

#tPSHSuite = PSHInst0.GetSuite("File")
#tPSHSuite.AddFunc("ViewFile")
#tPSHSuite.ShowFuncs()

#tPSHFunc = PSHInst0.GetSuite("File").GetFunc("ViewFile")
#tPSHFunc.AddPar("fileName")
#tPSHFunc.ShowPars()
#quit()

#To import a specific Python file at 'runtime' with a known name:
#import os
#import sys
#scriptpath = "../Test/MyModule.py"
# Add the directory containing your module to the Python path (wants absolute paths)
#sys.path.append(os.path.abspath(scriptpath))
# Do the import
#import MyModule


#moduleName = input('Enter module name:')
#importlib.import_module(moduleName)
#execfile("PSHFile.py")
#exec("C:\\araj\\python\\PSHFile.py")

#module = __import__("PSHFile")
#my_class = getattr(module, "PSHFile")
#print (my_class)
#instance = PSHFile()


#TSHFile for file specific calls
#TSHDir for directory specific calls
#TSHPath for ex if it applies for both files and directories

        
#    def Initialize(self, path):
#        self.path = path
        
#pathlibPath.exists()

#vtshFile = TSHFile("/home/alex/learn/python/data/xls/yaml05.xlsm")
#vtshFile.file = "xxxx"
#print(vtshFile.__dict__)
#print(vtshFile.file)
#print(vtshFile.TSHisdir())
#print(vtshFile.TSHisfile())
