import os
import glob

def get_extensions():
    # local dict
    files = {}
    
    # grab all files in current folder
    for f in glob.glob("*.*"):
        ext = os.path.splitext(f)[1][1:]
        # convert extensions to lowercase so PNG is counted as png
        files[ext.lower()] = files.get(ext.lower(), 0) + 1
    
    return files
    
if __name__ == "__main__":
    extensions = get_extensions()
    for e in extensions.keys():
        print(e + ":" + str(extensions[e]))
    
