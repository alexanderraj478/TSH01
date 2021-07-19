import sys
import getopt
  
class TSHgetopt:  
    def full_name(self):
        first_name = None
        last_name = None
      
        argv = sys.argv[1:]
      
        try:
            opts, args = getopt.getopt(argv, "f:l:")
        except:
            print("Error")
      
        for opt, arg in opts:
            if opt in ['-f']:
                first_name = arg
            elif opt in ['-l']:
                last_name = arg
          
      
        print( str(first_name) +" " + str(last_name))

    def full_nameWithLong(self):
        first_name = None
        last_name = None
      
        argv = sys.argv[1:]
      
        try:
            opts, args = getopt.getopt(argv, "f:l:", ["first_name=", "last_name="])
          
            #opts, args = getopt.getopt(argv, "f:l:", 
            #                           ["first_name=",
            #                            "last_name="])
        except:
            print("Error")
      
        for opt, arg in opts:
            if opt in ['-f', '--first_name']:
                first_name = arg
            elif opt in ['-l', '--last_name']:
                last_name = arg
          
      
        print( str(first_name) +" " + str(last_name))
  

if (__name__ == "__main__"):
    tshgetopt = TSHgetopt()
    tshgetopt.full_name()
    tshgetopt.full_nameWithLong()
