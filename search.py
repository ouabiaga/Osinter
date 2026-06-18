import requests
import json
import colorama

colorama.init(autoreset=True)

def search_ip():
    try:
        ip = input("Give me target IP address: ")
        api = f"http://ip-api.com/json/{ip}"
        response = requests.get(api)
        data = response.json()
        print(colorama.Fore.GREEN + json.dumps(data, indent=2))
    except Exception:
        print(colorama.Fore.RED + "Entered valid IP address")

def search_phone_public():
    try:
        phone = input("Phone number (start with +): ")
        url = f"https://phone-validation-api.vercel.app/api/validate/{phone}"
        response = requests.get(url)
        data = response.json()
        print(colorama.Fore.GREEN + json.dumps(data, indent=2))
    except Exception:
        print(colorama.Fore.RED + "Entered valid phone number")

def search_whois():
    try:
        domain = input("Enter the domain: ")
        api = f"https://api.hackertarget.com/whois/?q={domain}"
        response = requests.get(api)
        print(colorama.Fore.GREEN + response.text)  
    except Exception:
        print(colorama.Fore.RED + "Entered valid domain")

def search_dns():
    try:
        domain = input("Enter the domain: ")
        api = f"https://api.hackertarget.com/dnslookup/?q={domain}"
        response = requests.get(api)
        print(colorama.Fore.GREEN + response.text) 
    except Exception:
        print(colorama.Fore.RED + "Entered valid domain")

def search_reverseiplook():
    try:
        ip = input("Enter the IP: ")
        api = f"https://api.hackertarget.com/reverseiplookup/?q={ip}"
        response = requests.get(api)
        print(colorama.Fore.GREEN + response.text) 
    except Exception:
        print(colorama.Fore.RED + "Entered valid IP")
