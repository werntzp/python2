from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText    
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
import mimetypes
import os

def new_message(address, body, args):
    # create new message
    msg = MIMEMultipart()
    msg["To"] = address
    p = MIMEText(body, "plain")
    msg.attach(p)
    
    if len(args) > 0:
        for a in args:
            # open the file
            f = open(a, "rb")

            # try to guess type and build appropriate object
            t = mimetypes.guess_type(a)
            if t[0].find("image") > -1:
                x = MIMEImage(f.read())
            elif t[0].find("application") > -1:
                x = MIMEApplication(f.read())
            
            f.close()
            
            # add header info
            x.add_header("Content-Disposition", "attachment", filename=os.path.basename(a))
            
            # attach to the message
            msg.attach(x)
    
    # return the message
    #print(msg.as_string())
    return msg
    
         
