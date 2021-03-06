import unittest
import generate_email
from email.mime.multipart import MIMEMultipart

class TestGenerateEmail(unittest.TestCase):
    
    def test_email_noattachments(self):
        files = []
        msg = generate_email.new_message("dude@abides.com", "Rug cleaning costs.", files)
        self.assertEqual(msg["To"], "dude@abides.com", "Address did not match!")   
    
    
    def test_email_attachments(self):
        # set of files to use
        files = [r"v:\workspace\HandlingEmail_Homework\src\logo.png", 
                r"v:\workspace\HandlingEmail_Homework\src\calendar.xls"]
        
        msg = generate_email.new_message("dude@abides.com", "See attachments", files)     
        self.assertEqual(len(list(msg.walk())), 4, "Message does not contain four parts!")

if __name__ == "__main__":
    unittest.main()

 
