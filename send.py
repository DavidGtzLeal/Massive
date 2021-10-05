
import smtplib, socket
import os
import pandas as pd
from title import bcolors
import myparser

def send(platform):

    if platform == "Google":
        plt = "smtp.gmail.com"
    elif platform == "Outlook":
        plt = "smtp.office365.com"

    
    mail = input("Mail: ")
    passw = input("Password: ")
    exc = pd.read_excel("list.xlsx")
    destiny = None
    subject = input("Mail subject: ")

    for i in exc.index:
        with open('message.txt', encoding="latin-1") as f:
            lines = f.read()
        
        lines = myparser.parser(lines, exc["A1"][i], exc["A2"][i], exc["A3"][i])
        with smtplib.SMTP(plt, 587) as smtp:
            destiny = exc["Mail"][i]
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()

            try:
                smtp.login(mail, passw)
                

                msg = f'Subject: {subject}\n\n{lines}'
                smtp.sendmail(mail, destiny, msg)
                print(bcolors().OKGREEN +"Message sended correctly" + bcolors.ENDC)
            except socket.error as e:
                print(bcolors().FAIL +"Could not connect" + bcolors.ENDC)


    print(bcolors().OKGREEN +"ALL MESSAGES SENDED CORRECTLY" + bcolors.ENDC)


