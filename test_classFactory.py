import unittest
from classFactory import build_row
import mysql.connector
from database import login_info

class DBTest(unittest.TestCase):
    
    def setUp(self):
        C = build_row("animal", "id name family weight")
        self.c = C([1, "Clifford", "Dog", 10000])

    def test_attributes(self):
        self.assertEqual(self.c.id, 1)
        self.assertEqual(self.c.name, "Clifford")
        self.assertEqual(self.c.family, "Dog")
        self.assertEqual(self.c.weight, 10000)

    def test_repr(self):
        self.assertEqual(repr(self.c),
                         "animal_record(1, 'Clifford', 'Dog', 10000)")

    def test_cursor_no_conditions(self):
        # get a database cursor
        db = mysql.connector.Connect(**login_info)
                
        # get all animals
        db_rows = []
        cursor = db.cursor()
        cursor.execute("select * from animal")
        for r in cursor.fetchall():
            db_rows.append(r)
        # get animals from classFactory
        my_rows = []
        for dr in self.c.retrieve(cursor):
            my_rows.append(dr)
        self.assertEqual(len(db_rows), len(my_rows), "Row counts do not match!")
        db.close()    

    def test_cursor_conditions(self):
        # get a database cursor
        db = mysql.connector.Connect(**login_info)
        cursor = db.cursor()
        # get some animals
        db_rows = []
        cursor = db.cursor()
        cursor.execute("select * from animal where weight < 50")
        for r in cursor.fetchall():
            db_rows.append(r)
        # get animals from classFactory
        my_rows = []
        for dr in self.c.retrieve(cursor, "weight < 50"):
            my_rows.append(dr)
        self.assertEqual(len(db_rows), len(my_rows), "Row counts do not match!")
        db.close()    


           
if __name__ == "__main__":
    unittest.main()

 
