# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        usingfujian
# Purpose:
#
# Author:      Administrator
#
# Created:     01/02/2015
# Copyright:   (c) Administrator 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr,formataddr
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage

def _format_addr(s):
    name,addr=parseaddr(s)
    return formataddr((\
        Header(name,'utf-8').encode(),\
        addr.encode('utf-8') if isinstance(addr,unicode) else addr))

from_addr ='lml131415@126.com'
password = "lml121314"
smtp_server ='smtp.126.com'
to_addr ='aminic@163.com'





msg = MIMEMultipart()

msg['From'] = _format_addr(u'Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr(u'管理员 <%s>' % to_addr)
msg['Subject'] = Header(u'来自SMTP的问候……', 'utf-8').encode()

msg.attach(MIMEText('<html><body><h1>Hello</h1>' +
    '<p><img src="cid:0"></p>' +
    '</body></html>', 'html', 'utf-8'))

with open('d:\\d.jpg', 'rb') as f:
    mime = MIMEBase('image', 'jpeg', filename='d.jpg')
    mime.add_header('Content-Disposition', 'attachment', filename='d.jpg')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    mime.set_payload(f.read())
    encoders.encode_base64(mime)
    msg.attach(mime)
    #############################
    #img=MIMEImage(f.read())
    #msg.attach(img)


##################################################
server = smtplib.SMTP(smtp_server,25)
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()