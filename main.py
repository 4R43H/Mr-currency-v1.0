# /bin/python3
"""
This My mini project for bezzar of crypto currencys
coder --> Eliot Elderson (EE)
Email --> N0000000!
Created in --> 29 Agu 2022
Update in --> 31 Agu 2022
support time --> forever :)
Please Email:((((( --> coderpy@yahoo.com 

"""

#packages to import
import requests as req
from bs4 import BeautifulSoup as bs
import sys
from colorama import Fore as color
import os


# variables
bold = '\033[1m'
endbold = '\033[0m'


cr_list = [
    'bitcoin',
    'ethereum',
    'dogecoin',
    'shiba-inu',
    'xrp',
    'binance-coin',
    'cardano',
    'solana',
    'stellar',
    'chainlink',
    'uniswap',
    'decentraland',
    'filecoin',
    'apecoin',
    'hedera',
    'eos',
    'tezos',
    'the-sandbox',
    'aave',
    'axie-infinity',
    'elrond',
    'theta',
    'chiliz',
    'ecash',
    'neo',
    'synthetix',
    'polygon',
    'avalanche',
    'tron',
    'litecoin',
    'cosmos',
    'monero',
    'quant',
    'algorand',
    'flow',
    'vechain']

#clear the screen
os.system("clear")


# functions
def ban():
    #banner!
    print(bold+color.MAGENTA+'''                                                                 
  _ __ ___  _ __ ______ ___ _   _ _ __ _ __ ___ _ __   ___ _   _ 
 | '_ ` _ \| '__|______/ __| | | | '__| '__/ _ \ '_ \ / __| | | |
 | | | | | | |        | (__| |_| | |  | | |  __/ | | | (__| |_| |
 |_| |_| |_|_|         \___|\__,_|_|  |_|  \___|_| |_|\___|\__, |
                                                            __/ |
                                                           |___/ 
    '''+endbold)

    print("Welcome to Mr currncy app!")
    print("You can type list to see list!")
    print("You can type exit to exit of this app!")
    print("You can type help to see help list!")
    print("You can see supported crypto currencys with see command!")
    print("service-1 to use service-1")
    print("----------------------------------")


def cons():
    try:
        ban()
        for x in cr_list:
            print(color.CYAN+x+endbold)

        while True:
            arz_avalie = input("Enter your crypto currency! : ")
            if arz_avalie == "list":
                print(cr_list)

            if arz_avalie == "exit":
                print("")
                print(color.GREEN+"have good time!"+endbold)
                print(color.GREEN+"good bye!"+endbold)
                sys.exit()

            if arz_avalie == "help":
                ban()

            if arz_avalie == "service-1":
                print("you can go to service-1.py file and run it and use it!")

            if arz_avalie == "see":
                print(cr_list)

            if arz_avalie == "clear":
                os.system("clear")

            if arz_avalie in cr_list:
                r = req.get("https://www.coindesk.com/price/"+arz_avalie+"/")

                if r.status_code == 200:
                    soup = bs(r.text, 'html.parser')
                    val1 = soup.find("span", class_="typography__StyledTypography-owin6q-0 jvRAOp")
                    print(str(val1.text)+"$")

                elif r.status_code == 404:
                    print("Oops! Not found.")

                elif arz_avalie not in cr_list:
                    print("Sorry\n We are not supported this crypto currency!")

    except KeyboardInterrupt:
        print("\nWhy do this! :/")
        sys.exit()


if __name__ == "__main__":
    cons()
