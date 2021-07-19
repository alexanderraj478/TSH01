class TSHshutil:
    def __init__(self):
        pass
    
    def TSHcopyfile(self):
        pass
    
    def TSHcopy(self):
        pass
    
    def TSHcopy2(self):
        pass
    
    #shutil.copyfile(src_file, dest_file, *, follow_symlinks=True)
    #shutil.copy(src_file, dest_file, *, follow_symlinks=True)
    #shutil.copy2(src_file, dest_file, *, follow_symlinks=True)
    #shutil.copyfileobj(src_file_object, dest_file_object[, length])
# example
file_src = 'source.txt'  
f_src = open(file_src, 'rb')

file_dest = 'destination.txt'  
f_dest = open(file_dest, 'wb')

shutil.copyfileobj(f_src, f_dest)  

