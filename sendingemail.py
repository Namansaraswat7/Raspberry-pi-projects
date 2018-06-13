import smtplib
 
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login("namansaraswat7@gmail.com", "namansar@1")
 
msg = "hello naman ,this mais send to you  using python!"
server.sendmail("namansaraswat7@gmail.com", "naman.15bec1090@abes.ac.in",msg)
server.quit()
