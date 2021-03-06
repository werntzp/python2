"""
Module: testJokeMail
Read in and parse email messages to verify Joke Of The Day emails are being created.

NOTE: This test drops any messages in the message table
and should leave it empty. DANGER: this test will delete any existing message table.
"""

import mysql.connector as msc
from database import login_info
import jokemail
import jokesettings
import unittest
import datetime
from email.utils import parsedate_tz, mktime_tz
import time

conn = msc.Connect(**login_info)
curs = conn.cursor()

class testCreateJokeMail(unittest.TestCase):

    def setUp(self):
        """
        Method: setUp
        Purpose: Drop any existing messages 
        """          
        curs.execute("delete from message")
        
    def tearDown(self):
        """
        Method: tearDown
        Purpose: Drop any existing messages 
        """          
        curs.execute("delete from message")         
        
    def test_create_joke(self):
        """
        Method: test_create_joke
        Purpose: Create joke emails for recipients based on DAYCOUNT variable
        """ 
               
        # loop through day count, creating messages
        txt = "This is the message"
        start = time.time()
        jokemail.queue_emails(jokesettings.RECIPIENTS, jokesettings.STARTTIME, jokesettings.DAYCOUNT, txt)
        end = time.time()
        interval = end - start
        print("Time to complete: ", interval)
        
        # how many messages should we expect to see? 
        d = dict(jokesettings.RECIPIENTS)
        num_msgs = jokesettings.DAYCOUNT * len(d)

        # get the count from the db table
        curs.execute("select count(*) from message")        
        db_count = int(curs.fetchone()[0])
        self.assertEqual(num_msgs, db_count, "Number of expected messages in table not correct!")

if __name__  == "__main__":
    unittest.main()

 
