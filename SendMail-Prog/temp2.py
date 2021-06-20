import smtplib
import pdb

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_mail(subject="Firmware Upgrade Notification", mymsg="Upgrade for server with IP 192.168.0.5 success"):
    fromaddr = "Octopus_Notification@radisys.com"
    toaddr = "naga.manjunath@radisys.com, Laxmi.Sogani@radisys.com, Chaithanya.Vuppara@radisys.com"
    pass1 = '********'
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = subject

    #body = "Upgrade for server with IP 192.168.0.5 success"
    msg.attach(MIMEText(mymsg, 'plain'))

    server = smtplib.SMTP('172.24.100.144', 25)
    server.starttls()
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()


send_mail("Test Mail",""Firmware upgrad by mayur", "Test mail")
