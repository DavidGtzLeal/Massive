import smtplib, socket
import os
import pandas as pd
from title import title
import platforms
import myhelp

def main():
    esc = False
    usr = None

    title()

    def exit():
        esc = True


    while esc == False:
        usr = input()
        if usr == "sendGoogle":
            platforms.mass_send_google()
        elif usr == "exit":
            esc = True
            break
        elif usr == "sendOutlook":
            platforms.mass_send_outlook()
        elif usr == "help":
            myhelp.ask_help()
        else:
            print("Use command help to get some instructions on the use of this software")


if __name__ == "__main__":
    main()