import unittest
import os
import workdir
import shutil

# set of files to use
files = ["a.foo", "b.txt", "c.foo", "d.gif", "e.png", "f.foo", "g.png", "h.doc", "i.html", "j.PNG", "myfile"]
tmp = r"v:\hmwk"
orig = ""

class TestWorkDir(unittest.TestCase):
    
    def setUp(self):
        """Generate files to be used in testing"""
        # capture current dir, then switch to tmp one
        self.orig = os.getcwd()
        try:
            os.chdir(tmp)
        except:
            os.mkdir(tmp)
            os.chdir(tmp)
        # create test files
        for f in files:
            x = open(f, "w")
            x.close()
        

    def test_workdir_extensions(self):
        """Verify correct file counts are returned"""
        extcount = {"foo":3, "txt":1, "gif":1, "png":3, "doc":1, "html":1}
        self.assertEqual(workdir.get_extensions(), extcount, "Failed - Wrong file extension count returned")
    
    def tearDown(self):
        """Remove temp folder"""
        # return to previous dir
        os.chdir(self.orig)
        # remove the tmp dir
        shutil.rmtree(tmp, True)

if __name__ == "__main__":
    unittest.main()

 
