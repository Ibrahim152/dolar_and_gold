import requests
from bs4 import BeautifulSoup
import ssl
import time


try:
    website = requests.get("https://sp-today.com/en/currency/us_dollar")
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    sorce = website.content
    soup = BeautifulSoup(sorce, "lxml")
    name = soup.find_all("span", {"class": "name"})
    value = soup.find_all("span", {"class": "value"})

    print(f"{name[0].text.upper()} : {value[0].text} SYP")
    print(f"{name[1].text.upper()} : {value[1].text} SYP")
    print(f"{name[2].text.upper()} : {value[2].text} SYP")
    print(f"{name[3].text.upper()} : {value[3].text} SYP")
    print(f"{name[4].text.upper()} : {value[4].text} SYP\n")
except:
    print('no connection')
    exit()

while True:
    try:
        print('''
chose a task please:
1)_USD TO SYP CONVERT
2)_SYP TO USD CONVERT
3)_my gold cost calculation
4)_how much gold i can buy??
''')
        task = input('')
        if int(task) == 1:
            US = float(input("how much USD you have?\n"))
            print(f"{US*int(value[0].text)} SYP")
        elif int(task) == 2:
            SYP = float(input("how much SYP you have?\n"))
            print(f"{SYP/int(value[0].text)} USD")
        elif int(task) == 3:
            ty = int(input("your gold is \n1)_18 karat\n2)_21 karat\n"))
            gold = float(input("how much gold you have per GRAM?\n"))
            if ty == 1:
                am = gold*float(value[3].text.replace(",", "."))*1000
                print(f"{am} SYP")
            if ty == 2:
                m = gold*float(value[4].text.replace(",", "."))*1000
                print(f"{m} SYP")
                time.sleep(10)
        elif int(task) == 4:
            S = float(input("how many SYP do you have?\n"))
            m = value[3].text.replace(",", ".")
            v = value[4].text.replace(",", ".")
            print(f"you can buy {S/(float(m)*1000)} g of 18 karat gold")
            print(f'you can buy{S/(float(v)*1000)} g of 21 karat gold')
        time.sleep(2)
    except:
        print('invalid')
        time.sleep(2)
