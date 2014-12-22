"""
Demonstration of setUp and tearDown.
The tests do not actually test anything - this is a demo.
"""
import unittest
import tempfile
import shutil
import glob
import os

class FileTest(unittest.TestCase):
    
    def setUp(self):
        self.origdir = os.getcwd()
        self.dirname = tempfile.mkdtemp("testdir")
        os.chdir(self.dirname)
    
    def test_1(self):
        "Verify creation of files is possible"
        myfiles = set(["this.txt", "that.txt", "the_other.txt"])
        for filename in myfiles:
            f = open(filename, "w")
            f.write("Some text\n")
            f.close()
            self.assertTrue(f.closed)
            
        # make sure only the files created actually exist    
        osfiles = set(os.listdir(os.getcwd()))
        self.assertEqual(myfiles, osfiles, "Temp folder contains files other than the three expected")
        
    def test_2(self):
        "Verify that the current directory is empty"
        self.assertEqual(glob.glob("*"), [], "Directory not empty")

    def test_3(self):
        "Create a binary file and verify size"
        # create binary file with 1 million bytes
        binfile = os.getcwd() + "testbinfile"
        bf = open(binfile, "wb")
        bf.write(b"\0" * 1000000)
        bf.close()
        # check size with os.stat
        statinfo = os.stat(binfile)
        self.assertEquals(statinfo.st_size, 1000000, "Binary files does not equal 1000000 bytes")

    def tearDown(self):
        os.chdir(self.origdir)
        shutil.rmtree(self.dirname)
        

if __name__ == "__main__":
    unittest.main()

