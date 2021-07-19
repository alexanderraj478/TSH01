class TSHStrFmt:
    def __init__(self):
        pass
    
    def StrFmt01(self, val):
        print ("%02d" % (val, ))
    
    def StrFmt02(self, val):
        print("{:02d}".format(val))

    def StrFmt03(self, val):
        print(f"{val:02d}")

    def StrFmt04(self, prec, val):
        print(str(val).zfill(prec))
        
    def StrFmt05(self, val):
        prec = 3
        print('{num:03d}'.format(num=val))
        print('{num:3d}'.format(num=val))
        print(format(val, '02d'))
        print('{:02}'.format(val))
        print(f'{val:02}')
        print(str(val).rjust(prec, '0'))
        print("{:0>2}".format(val))
        print("{0:0>2}".format(val))
        print("{0:0>{1}}".format(val, prec + 1))


        val = (prec - len(str(val))) * "0" + str(val)
        print(val)

        print('00'[len(str(val)):] + str(val))


if (__name__ == "__main__"):
    tshStrFmt = TSHStrFmt()
    tshStrFmt.StrFmt01(6)
    tshStrFmt.StrFmt02(6)
    tshStrFmt.StrFmt03(6)
    tshStrFmt.StrFmt04(6, 6)
    tshStrFmt.StrFmt05(6)
    pass