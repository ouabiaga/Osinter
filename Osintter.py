import requests
import colorama
import scanner
import search
colorama.init(autoreset=True)
def banner():
    print(f"""\033[32m  \033[3m \033[1m                          
     _____     _     _           
    |     |___|_|___| |_ ___ ___ 
    |  |  |_ -| |   |  _| -_|  _|
    |_____|___|_|_|_|_| |___|_|  
                                    """)
    print("writed by _serpten_")
def process():
    print("""
    [1] Find Social Media 
    [2] Search ip
    [3] Search phone
    [4] Search whois
    [5] search dns by ip
    [6] search reverse ip look
    """)
if __name__=="__main__":
    banner()
    process()
    i=int(input("Give Process number: "))
    if i==1:
        scanner.check_username()
    elif i==2:
       search.search_ip()
    elif i==3:
        search.search_phone_public()
    elif i==4:
        search.search_whois()
    elif i==5:
        search.search_dns()
    elif i==6:
        search.search_reverseiplook()