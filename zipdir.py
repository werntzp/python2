import os
import glob
import zipfile

def zip(path, zipname):
    # switch to incoming path
    os.chdir(path)
    # create a new zip file
    zf = zipfile.ZipFile(os.path.dirname(os.path.dirname(path)) + "\\" + zipname, "w")
    # grab all files in current folder
    for x in glob.glob("*"):
        # only add files
        if os.path.isfile(x):
            zf.write(x, os.path.basename(os.getcwd()) + "\\" + os.path.basename(x))
            
    zf.close()
    return zf

if __name__ == "__main__":
    lst = zip(r"v:\workspace\Archives_Homework\src", "myzip.zip").namelist()
    for f in lst:
        print(f)
        
    
