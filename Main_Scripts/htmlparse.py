"""
This is the main document for this project. It searches a given
url (in the html_doc variable) for mailto: and then sends a
pre-composed email regarding next day's events.
Functionality right now is limited and URLs must be
manually given, but ultimately this script should
check for next day's events on a daily basis and send
and appropriate email, likely using some sort of
datettime-based algorithm.
"""


import urllib
import re
import datetime
from bs4 import BeautifulSoup

#variable to open URL to be parse
html_doc = urllib.urlopen("link goes here")
#parses URL
soup = BeautifulSoup(html_doc, 'html.parser')

#find links in html_doc, specified to find mailto
for elem in soup.find_all('a',href=re.compile('mailto:')):
	print elem['href'].split("mailto:", 1)[1]
	#prints specific email (i.e., the person's email address)
	print elem['href']




# Import smtplib for the actual sending and encryption function
import smtplib
# Import the email modules
from email.mime.text import MIMEText

#create and encrypt connection, then login to server
#creates SMTP connection w/ gmail port and server
server = smtplib.SMTP('smtp.gmail.com', 587)
#encrypts smtp connection via TLS mode
server.starttls()
#logs in to gmail server
server.login("gmailusername", "gmailpassword")


#defines message and sends it
msg = """" Greetings,\n \n We at the IT Helpdesk have noticed that you have an
upcoming meeting/event in Burke 210. That room is already equipped with a
television connected to Skype and capable of connecting to your own laptop,
should you bring it\n \n If you require any additional IT equipment or needs,
please contact us by 3 pm today so that we can prepare to have it ready for
you.\n \n If you have any questions or concerns, please feel free to contact
us at 251.380.2276 or helpdesk@shc.edu.\n \n Regards,\n \n ____\n \n IT Help
Desk\n \n Spring Hill College\n \n 251-380-2276\n \n helpdesk@shc.edu\n\nThis
email contains information from Spring Hill College, and is intended solely
for the use of the named recipient or recipients. It may contain confidential
or privileged information, including but not limited to FERPA-protected
information. If you are not a named recipient on the email, please delete
this message because any unauthorized review, copying, or use of this
message is prohibited. """

#sends msg to email
server.sendmail("emailsender", "emailrecipient", msg)
#terminates smtp session and closes the connection
server.quit()















## -------------------- UNUSED ------------------------- ##

#html_doc = "webevent.html" <---- alternative to urllib.open -->
#opens html file from PC
#soup = BeautifulSoup(open(html_doc), 'html.parser')
#opens htmldoc FILE, parses it


#print soup.find_all('a', href=re.compile('mailto:'))

#for link in soup.find_all('a'):
    #print(link.get('href'))

#soup.find_all()
