"""
Module: jokemail

Contains logic to create emails and store them in MySQL.
"""
from database import login_info
import mysql.connector as msc
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime
import time

conn = msc.Connect(**login_info)
curs = conn.cursor()

def queue_emails(recipients, start_date, num_days, txt):
    """
    Method: queue_emails
    Purpose: general multiple emails to recipients, starting one a date and continuing for a specified number  
    """
    
    # loop through and call other method to generate a bunch of emails
    dte = datetime.datetime.strptime(start_date, "%d/%m/%y %H:%M")
    for i in range(num_days):
        create_joke_email(recipients, dte, txt)
        dte += datetime.timedelta(days=i)            
    

def create_joke_email(recipients, dte, txt):
    """
    Method: create_joke_email
    Purpose: general one email to the recipients on specified date with incoming text 
    """

    # create email
    msg = MIMEMultipart()
    msg["Subject"] = "Joke of the Day!"
    msg["From"] = "website@example.com"
    msg["Date"] = dte
    body = MIMEText(txt)
    msg.attach(body)
    
    # loop through the recipients and add to mail message
    d = dict(recipients)
    for k in d: 
        # get email addr
        msg["To"] =  d[k]
        # store that message in the database
        sql = "insert into message (msgDate, msgSenderName, msgSenderAddress, msgText) \
             values ('{0}', '{1}', '{2}', '{3}')".format(msg["Date"], k, msg["To"], txt)     
        curs.execute(sql)
 
