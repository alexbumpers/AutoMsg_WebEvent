"""
Demonstrates sending email via a Python script and the smptlib module. This is in use for the WebEventScrape project, but
this specific file is not part of the project.
"""


# Import smtplib for the actual sending and encryption function
import smtplib

# Import the email modules
from email.mime.text import MIMEText

#-----create and encrypt connection, then login to server-----
#creates SMTP connection w/ gmail port and server
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()  #encrypts smtp connection via TLS mode
server.login("username", "password") #logs in to gmail server


#-----defines message and sends it-----
msg = "Good morning!"
#sends msg to email
server.sendmail("emailsender", "emailrecipient", msg)
#terminates smtp session and closes the connection
server.quit()
