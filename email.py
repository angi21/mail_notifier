import imaplib

latest_email = []
def read_email(mail_id,password,host,from_id):
    
    mail = imaplib.IMAP4_SSL(host)
    mail.login(mail_id,password)
    mail.select('INBOX')
    result, data = mail.search(None,'FROM',f'\"{from_id}\"')    
    ids = next(iter(data))
    
    emails = ids.split()
    
    latest = emails[-1]
    #print(latest)
    #res,data = mail.fetch(latest,"(RFC822)")
    #result = data[0][1].decode("utf-8")
    #with open('email.txt',mode='a') as file:
     #   file.write(raw_text)
    return latest
    pass

from getpass import getpass
import os
host = 'imap.gmail.com'
mail_id = input('  Enter ur mail id  ')
from_id = input('  Enter the id u wanna check ')
password = getpass('  Enter password  ')
codes = []
while True:
    raw_code = read_email(mail_id,password,host,from_id)
#    codes = []
    if not codes:
        codes.append(raw_code)
        print(codes)
    else:
        if codes[-1] != raw_code:
            print('new message recieved')
            codes.append(raw_code)
            with open('mail.txt',mode='a') as file:
                file.write('Hey new email received from '+from_id)
            os.system("notepad mail.txt")
            continue