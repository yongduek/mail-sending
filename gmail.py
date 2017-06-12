import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
 
fromaddr = "kcvs.kccv2017@gmail.com"
#toaddr = "yongduek.seo@gmail.com"
 
def sendmail2(toaddr):
    msg = MIMEMultipart()

    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Invitation to KCCV 2017"

    txtfile = 'kccv-inv.txt'
    f=open(txtfile, 'r')
    invitxt = f.read()
    #print (body)
    f.close()
    body = invitxt

    msg.attach(MIMEText(body, 'plain'))

    attach_filename = 'kccv-prog.pdf'
    attachment = open(attach_filename, "rb")

    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % attach_filename)

    msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    #print ('server=', server)
    server.starttls()
    server.login(fromaddr, "Password_of_yours")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
#


email_list_file = 'emails.txt'
fel = open (email_list_file, 'r')
email_list = fel.read().splitlines()
for email_addr in email_list:
    print ('sending to [{}]'.format(email_addr))
    sendmail2(email_addr)

exit()
