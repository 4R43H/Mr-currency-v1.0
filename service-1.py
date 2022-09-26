"""
This My mini project for follow up the price of BTC with sms
coder --> Eliot Elderson (EE)
Email --> N0000000!
Created in --> 13 SEP 2022
Update in --> 13 SEP 2022
support time --> forever :)
Please Email:((((( --> coderpy@yahoo.com 
"""

"""
In This section we import needs to run program!

"""

import sys
import requests as req
from bs4 import BeautifulSoup as bs
import os

"""
In here I define functions and this is main function and all of program will run in this funtion.
"""
def pro():
    """
    In This section I define my banner for program !
    """
    try:
        os.system("clear")
        print("Welcom to X service")
        print("you can follow up the price of bitcoin from this service")
        print("This service working with sms and send me the message.")
        print("Tnx for using the Mr-Currency and X-service ...")

        
        """
        In this section we define inputs and I get values of them from user.
        """
        inp = input("if you want to follow up enter your phone number(only iran WHIT 0): ")
        name = input("Enter your name: ")
        my_good_price = int(input("Enter your price to follow up the bitcoin price: "))


        """
        This main function and I define it for requests to website and get the information from website.
        """
        def main():
            while True:
                r = req.get("https://www.coindesk.com/price/bitcoin")

                if r.status_code == 200:
                    global res
                    soup = bs(r.text, 'html.parser')
                    val1 = soup.find("span", class_="typography__StyledTypography-owin6q-0 jvRAOp")
                    res = val1.text.replace(",", "")
                    inform_to_user()

        """
        I define this section for inform to user. if price of bitcoin was smaller than my good price, This section inform to me
        and the main usage of program it's inform_to_user function!
        """
        def inform_to_user():
            while True:
                api_key = "6E4572424D6A327852304631497966516E455749556D334C796E716C7646734147326452425463514975553D"
                url = "https://api.kavenegar.com/v1/{}/sms/send.json".format(api_key)
                payload = {"receptor":inp, "message":"Hi {} ... price is good!".format(name)}
                t = req.post(url, data=payload)
                check()
        """
        This function check the price for requests and sms to me!
        """
        def check():
            while True:
                if float(res) <= float(my_good_price):
                    inform_to_user()
        """
        I call my function to start the program
        """           
        main()
        """
        if user enter CTRL-C program return this text and exit.
        """
    except KeyboardInterrupt:
        print("\nBad input!")
        sys.exit()

"""
This is final run.
"""
if __name__ == "__main__":
    pro()
