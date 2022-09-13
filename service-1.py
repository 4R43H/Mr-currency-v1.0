"""
This My mini project for follow up the price of BTC with sms
coder --> Eliot Elderson (EE)
Email --> N0000000!
Created in --> 13 SEP 2022
Update in --> 13 SEP 2022
support time --> forever :)
Please Email:((((( --> coderpy@yahoo.com 
"""
import sys
import requests as req
from bs4 import BeautifulSoup as bs
import os

def pro():
    try:
        os.system("clear")
        print("Welcom to X service")
        print("you can follow up the price of bitcoin from this service")

        inp = input("if you want to follow up enter your phone number(only iran WHIT 0): ")
        name = input("Enter your name: ")
        my_good_price = int(input("Enter your price to follow up the bitcoin price: "))

        def main():
            while True:
                r = req.get("https://www.coindesk.com/price/bitcoin")

                if r.status_code == 200:
                    global res
                    soup = bs(r.text, 'html.parser')
                    val1 = soup.find("span", class_="typography__StyledTypography-owin6q-0 jvRAOp")
                    res = val1.text.replace(",", "")
                    inform_to_user()

        def inform_to_user():
            while True:
                api_key = "6E4572424D6A327852304631497966516E455749556D334C796E716C7646734147326452425463514975553D"
                url = "https://api.kavenegar.com/v1/{}/sms/send.json".format(api_key)
                payload = {"receptor":inp, "message":"Hi {} ... price is good!".format(name)}
                t = req.post(url, data=payload)
                check()

        def check():
            while True:
                if float(res) <= float(my_good_price):
                    inform_to_user()
            
        main()

    except KeyboardInterrupt:
        print("\nBad input!")
        sys.exit()

if __name__ == "__main__":
    pro()
