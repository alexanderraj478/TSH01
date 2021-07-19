import sys, getopt

class TSHCmdLine:
    def __init__(self):
        cmdLineArgs = None
        cmdLineArgTot = 0
        pass
    
    def DispCmdInvoked(self, argv):
        cmdLineArgs = argv
        print (len(cmdLineArgs))
        print (cmdLineArgs)
    
    def main(self, argv):
        inputfile = ''
        outputfile = ''
        try:
            opts, args = getopt.getopt(argv, "hi:o:", ["ifile=","ofile="])
        except getopt.GetoptError:
            print ('psh.py {cmds}')
            sys.exit(2)
        
        for opt, arg in opts:
            if opt == '-h':
                print ('test.py -i <inputfile> -o <outputfile>')
                sys.exit()
            elif opt in ("-i", "--ifile"):
                inputfile = arg
            elif opt in ("-o", "--ofile"):
                outputfile = arg
        print ('Input file is "', inputfile)
        print ('Output file is "', outputfile)

if __name__ == "__main__":
    tshCmdLine = TSHCmdLine()
    argv = ["TSHCmdLine.py", "-i alex", "-o veni"]
    tshCmdLine.main(sys.argv[1:])