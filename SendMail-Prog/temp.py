'''import smtplib
gmailaddress = eval((input("what is your gmail address? ")))
gmailpassword = input("what is the password for that email address? ")
mailto = input("what email address do you want to send your message to? ")
msg = input("What is your message? ")
mailServer = smtplib.SMTP('smtp.gmail.com' , 587)
mailServer.starttls()
mailServer.login(gmailaddress , gmailpassword)
mailServer.sendmail(gmailaddress, mailto , msg)
print(" \n Sent!")
mailServer.quit()
'''

'''
import smtplib
import pdb

from string import Template

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
pdb.set_trace()
MY_ADDRESS = 'mady00567@gmail.com'
PASSWORD = ''

s = smtplib.SMTP(host='smtp.gmail.com', port=587)
s.starttls()
s.login(MY_ADDRESS, PASSWORD)

msg = MIMEMultipart()  # create a message

# add in the actual person name to the message template
#message = message_template.substitute(PERSON_NAME=name.title())
message = "Hi Mayur, How are you?"
# Prints out the message body for our sake
print(message)

# setup the parameters of the message
msg['From'] = MY_ADDRESS
msg['To'] = "mayurchavda87@gmail.com"
msg['Subject'] = "This is TEST"

# add in the message body
msg.attach(MIMEText(message, 'plain'))

# send the message via the server set up earlier.
s.send_message(msg)
print(msg)
del msg
'''

from email.mime.text import MIMEText
import smtplib
msg=MIMEText('hi, send by python.....','plain','utf-8')
from_addr='mady00567@gmail.com'
password='***************'
to_addr='user@gmail.com'
s=smtplib.SMTP_SSL('smtp.gmail.com')
s.login(from_addr,password)
s.sendmail(from_addr, [to_addr], msg.as_string())
