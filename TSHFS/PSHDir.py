import os
#import sys
#from TSHGlobal import *

class PSHDir:

    def PSHcwd(self):
        print(os.getcwd())
        pass
    
    def PSHrealpath(self):
        print(os.path.realpath(__file__))
        pass
    
    def PSHdirname(self):
        print(os.path.dirname(os.path.realpath(__file__)))
        pass
