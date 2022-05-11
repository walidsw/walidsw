#walid waccub swadhin
import smtplib
from time import sleep
import sys
from getpass import getpass

from os import name, system

def clear():
    if name =='nt':
        system('cls')
    else:
        system('clear')
print(f'\n\n')
print ("\t      _________    __        __        HERO        ________    __                                                ")
print ("\t[walid|########|  |##\      /##|      /####\      |########|  |##|              By walid swadhin                 ")
print ("\t[walid|##|____    |###\ __ /###|     /##/\##\        |##|     |##|            by blue_sky team BD                ")
print ("\t[walid|########|  |##| |##| |##|    /########\       |##|     |##|         ____   __  _  _ ____   __  ___        ")
print ("\t[walid|##|_____   |##|      |##|   /##/    \##\    __|##|__   |##|_______   |__| |  | |\/|  |__| |__  |__|       ")
print ("\t[walid|########|  |##|      |##|  /##/      \##\  |########|  |##########| _|__| |__| |  | _|__| |__  |  \       ")

print('\n\n')       
print('choose your email provider: ')

print('[1] gmail')
print('[2] outlook/hotmail')
print('[3] custom')

provider = int(input('\n>>'))

if provider == 1:
    smtp_server = 'smtp.gmail.com'
elif provider == 2:
    smtp_server = "smtp.office365.com"
elif provider == 3:
    smtp_server = input('enter custom smtp server:') 
else:
    print('invalid choice')
    sys.exit() 
print('\n')  
email = input("SENDER'S EMAIL: ")
password = getpass("sender's password: ")

server = smtplib.SMTP(smtp_server,587)
server.ehlo()
server.starttls()

try:
    server.login(email,password)
    print('\n\tlogin successfull\n\n')
    
except:
    print('login failed')
    sys.exit()

a=True
while a:
    rec = input('enter receiver email adress: ')
  
    #name = input('enter a name:')

    subject = input('email subject: ')

    body = input('enter mail message: ')

    print('\n\n----------------------------------------')
    msg = f'from:{email}\n\nTo:{rec}\n\nsubject:{subject}\n\n{body}'
    n = int(input('BOMBING EMAIL NUMBER(how many mail want to send) :'))
    print(f'\n\n')
    print(msg)
    print('\n\n----------------------------------------')
    print(f'\n\n')


    for i in range(n):
        server.sendmail(email,rec,body)
        print('email sent:',i+1)
    
    print(f'{n} emails have been sent\n\n')
    
    print('want to send email anywhere else,\n\n if yes type: 1 \n else type: 2\n')
    
    k = int(input('>>'))
    if k==1:
        a=True
    elif k==2:
        a=False
    else:
        a=False

