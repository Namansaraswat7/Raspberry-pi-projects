import smtplib
 
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login("yr email id", "yr password")
 
msg = "hello user ,this mail send to you  using python!"
server.sendmail("sender email id", "receiver email id",msg)
server.quit()
