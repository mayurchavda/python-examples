import smtplib

print(1)
server = smtplib.SMTP('smtp.gmail.com' , 587)
print(2)
server.starttls()
print(3)
server.login("mady00567", "")
print(4)
msg = "YOUR MESSAGE!"
server.sendmail("Mayurkumar.Chavda@radisys.com", "mayurchavda87@gmail.com", msg)
print(5)
server.quit()
print(6)
print("Mail Sent.")