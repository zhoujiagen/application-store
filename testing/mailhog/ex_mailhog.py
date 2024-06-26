#-*-coding: UTF-8 -*-

# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.message import EmailMessage

if __name__=="__main__":
  textfile = 'README.md'
  # Open the plain text file whose name is in textfile for reading.
  with open(textfile) as fp:
      # Create a text/plain message
      msg = EmailMessage()
      msg.set_content(fp.read())

  # me == the sender's email address
  # you == the recipient's email address
  msg['Subject'] = f'The contents of {textfile}'
  msg['From'] = 'from@example.com'
  msg['To'] = 'to@example.com'

  # Send the message via our own SMTP server.
  s = smtplib.SMTP(host='localhost', port=1025)
  s.send_message(msg)
  s.quit()