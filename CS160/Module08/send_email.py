import smtplib
import getpass

smtp_server = 'smtp-mail.outlook.com'
port = 587 # port 587 uses TLS encrpytion
sender = 'examplesmtp@outlook.com'
recipient = 'examplesmt@outlook.com'
# this allows you to type password without showing the characters
passwd = getpass.getpass('Password: ')
msg = """Subject: Need your help

Hi there,
How is it going?
I am so sleepy now, but I need your help with this.

When I tell you to pick up the left rock,
it will be the right one, and then the right rock will be left.
So, left or right?

I'm going to bed, sweet dreams!
"""
try:
    smtp_obj = smtplib.SMTP(smtp_server, port)
    # identity yourself to SMTP server
    smtp_obj.ehlo()
    # if you use port 465 (SSL), encrpytion is already set up.
    # No need to call startls()
    print(smtp_obj.starttls())
    print(smtp_obj.login(sender.passwd))
    smtp_obj.sendmail(sender, recipient, msg)
except Exception as e:
    print("Cannot send email:", e)
finally:
    print(smtp_obj.quit())
