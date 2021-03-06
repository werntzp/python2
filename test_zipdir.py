import unittest, os, time, shutil, glob, zipfile
import zipdir

tmp = r"v:\hmwk"
zipname = "myzip.zip"
files = ["mal", "zoe", "wash", "kaylee", "simon"]
folders = ["inara", "jayne", "river"]
orig = ""

class TestZipDir(unittest.TestCase):

    def setUp(self):
        """Generate temp folder with files and sub-folders"""
        self.orig = os.getcwd()
        if not os.path.isdir(tmp):
            os.mkdir(tmp)
        os.chdir(tmp)
        # create files    
        for f in files:
            x = open(f, "w")
            x.close()
        # create folders
        for f in folders:
            os.mkdir(f)
        # sleep for a few
        time.sleep(3)    
    
    def test_zip_folder_contents(self):
        # create the expected file list
        prefix = os.path.basename(tmp)
        expected = set([prefix + "/" + f for f in files])
        # create the zip file
        zf = zipdir.zip(tmp, zipname)
        # do the assert
        self.assertEqual(set(zf.namelist()), expected, "Failed - correct file list not returned")  

    def tearDown(self):
        """Remove temp folder and archive"""
        # return to previous dir
        os.chdir(self.orig)
        # remove the tmp dir
        shutil.rmtree(tmp, True)

if __name__ == "__main__":
    unittest.main()

 
