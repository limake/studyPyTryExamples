#-------------------------------------------------------------------------
# Name:        usingsmtp
# Purpose:
#
# Author:      Administrator
#
# Created:     31/01/2015
# Copyright:   (c) Administrator 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------

from email.mime.text import MIMEText
msg = MIMEText('hello,send by Python...', 'plain', 'utf-8')

from_addr = 'aaaaaaaaaa@aaaaaa'
password = "aaaaaaaaaaaaaaaaa"
smtp_server = 'aaaaaaaaaaaaa'
to_addr = 'aaaaaaaaaaaaaaaaaaaaaaa'


import smtplib
server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
