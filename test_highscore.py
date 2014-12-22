import unittest
import shelve
import os
import shutil
import highscore

tmp = r"v:\hmwk"
orig = ""
name = "highscore.shlf"

class TestHighScore(unittest.TestCase):
    
    def setUp(self):
        """Generate temp shelf"""
        # switch to a new folder
        self.orig = os.getcwd()
        try:
            os.chdir(tmp)
        except:
            os.mkdir(tmp)
            os.chdir(tmp)
        # create the shelf        
        shelf = shelve.open(name)
        shelf.close()

    def test_highscore_store(self):        
        """Test storing initial scores"""
        self.assertEqual(-100, highscore.set_newscore('flynn', -100))
        self.assertEqual(0, highscore.set_newscore('alan', 0))
        self.assertLess(0, highscore.set_newscore('ed', 100))
        self.assertEqual(1000, highscore.set_newscore('laura', 1000))
        
    def test_highscore_set(self):
        """Test setting a new high score for a player"""
        self.assertEqual(50, highscore.set_newscore('Kirby', 50))
        self.assertEqual(150, highscore.set_newscore('Kirby', 150))
        self.assertEqual(150, highscore.set_newscore('Kirby', 40))
        self.assertEqual(150, highscore.set_newscore('Kirby', 95))
        self.assertTrue(highscore.set_newscore('Kirby', 180) == 180, 'Kirby should have 180 as a top score') 

    def tearDown(self):
        """Remove temp shelf"""
        # remove the tmp fodler (which gets rid of the shelf)
        shutil.rmtree(tmp, True)
        
if __name__ == "__main__":
    unittest.main()

