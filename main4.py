# code.tutsplus.com
# import necessary packages
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib, mymodule
# create message object instance
msg = MIMEMultipart()
message = "Thank you"
# setup the parameters of the message
password = mymodule.my_password
msg['From'] = "dervoed.brest@gmail.com"
msg['To'] = "dervoed.brest@tut.by"
msg['Subject'] = "Subscription"
# add in the message body
msg.attach(MIMEText(message, 'plain'))
# create server
server = smtplib.SMTP('smtp.gmail.com: 587')
server.starttls()
# Login Credentials for sending the mail
server.login(msg['From'], password)
# send the message via the server.
server.sendmail(msg['From'], msg['To'], msg.as_string())
server.quit()