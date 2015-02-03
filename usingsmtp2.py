# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        usingsmtp2
# Purpose:
#
# Author:      Administrator
#
# Created:     31/01/2015
# Copyright:   (c) Administrator 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------


from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr,formataddr
import smtplib

def _format_addr(s):
    name,addr=parseaddr(s)
    return formataddr((\
        Header(name,'utf-8').encode(),\
        addr.encode('utf-8') if isinstance(addr,unicode) else addr))

from_addr ='aaaaaaaaaaaa'
password = "aaaaaaaaaaaaaa"
smtp_server ='aaaaaaaaaaaaaa'
to_addr ='aaaaaaaaaaaaaa'

msg = MIMEMultipart()
msg['From']= _format_addr(u'Python爱好者 <%s' % from_addr)
msg['To']=_format_addr(u'管理员 <%s>' %to_addr)
msg['Subject'] = Header(u'来自SMTP的问候...','utf-8').encode()


server = smtplib.SMTP(smtp_sach,25)
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()