# SirThirrygolooo - 2023 - Rip discord et leurs brillantes idées de con (ou opéra jsp qui a chié dans la colle la)

import requests
import time,datetime
import os
import colorama
import random

url = "https://api.discord.gx.games/v1/direct-fulfillment"
correct_url = "https://discord.com/billing/partner-promotions/1180231712274387115/"
logs_file = "logs.txt"
links_file = "liens.txt"
proxies_file = "http_proxies.txt"

# payload = {"partnerUserId": "2989a05be1d8d3a9ae6e6eeb1048079b64fa7e659992719908e5be4d5478a519"}
headers = {
    "authority": "api.discord.gx.games",
    "accept": "*/*",
    "accept-language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
    "content-type": "application/json",
    "origin": "https://www.opera.com",
    "referer": "https://www.opera.com/",
    "sec-ch-ua": '"Opera GX";v="105", "Chromium";v="119", "Not?A_Brand";v="24"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0"
}

# response = requests.request("POST", url, json=payload, headers=headers)

# possible de faire varier entièrement
def update_parnerUserId():
    def_chaine = "2989a05be1d8d3a9ae6e6eeb1048079b64fa7e659992719908e5be4d"
    char = "abcdefghijklmnopqrstuvwxyz"
    number = "0123456789"
    payload = {"partnerUserId": def_chaine+random.choice(number)+random.choice(number)+random.choice(number)+random.choice(number)+random.choice(char)+random.choice(number)+random.choice(number)+random.choice(number)}

    return payload

def printRed(text):
    print(colorama.Fore.RED + text + colorama.Fore.RESET)

def printGreen(text):
    print(colorama.Fore.GREEN + text + colorama.Fore.RESET)

def set_proxies():
    file = open(f"{proxies_file}", "r")
    proxies = file.readlines()
    file.close()

    return proxies

def set_proxy():
    proxies = set_proxies()
    proxy = proxies[0].replace("\n", "")
    return proxy

def remove_proxy():
    proxies = set_proxies()
    proxies.pop(0)
    file = open(f"{proxies_file}", "w")
    for proxy in proxies:
        file.write(proxy)
    file.close()

def make_request_with_proxy():
    timestamp = datetime.datetime.now().strftime("%H:%M:%S")
    payload = update_parnerUserId()
    proxy = set_proxy()
    proxies = {
        "http": proxy,
        "https": proxy
    }
    try:
        response = requests.request("POST", url, json=payload, headers=headers, proxies=proxies)
        if response.status_code == 429:
            printRed(f"[{timestamp}] - Erreur 429 : Too many requests ! Let's change proxy !")
            remove_proxy()
            return make_request_with_proxy()
        else:
            return response
    except:
        remove_proxy()
        return make_request_with_proxy()

def make_request_print_response():
    payload = update_parnerUserId()
    response = requests.request("POST", url, json=payload, headers=headers)
    print(response.json())
    print(response.status_code)
    lien = cemoi_le_lien(response)
    print(lien)

def write_in_file(response,file):
    file = open(f"{file}", "a")
    file.write(cemoi_le_lien(response) + "\n")
    file.close()

def cemoi_le_lien(response):
    token = response.json()["token"]
    link = correct_url + token
    return link

def counter():
    file = open(f"{links_file}", "r")
    lines = file.readlines()
    file.close()
    return len(lines)

def start():
    os.system('cls')
    while True:
        os.system('cls')
        print("Script démarré !")
        print("-"*64)
        print("Nombre de liens récupérés : " + str(counter()))
        print("Proxies restants : " + str(len(set_proxies())))
        print("Prochain proxy : " + set_proxy())
        print("-"*64)
        print("Appuyez sur CTRL+C pour arrêter le script")
        response = make_request_with_proxy()
        if response.status_code == 200:
            timestamp = datetime.datetime.now().strftime("%H:%M:%S")
            printGreen(f"[{timestamp}] - Success !")
            write_in_file(response, f"{links_file}")
        else:
            write_in_file(response, f"{logs_file}")
        time.sleep(3)
    menu()

def stop():
    exit()


def menu():
    os.system('cls')
    print("""
███████╗██╗      █████╗ ███████╗██╗      █████╗     ██╗  ██╗    
██╔════╝██║     ██╔══██╗██╔════╝██║     ██╔══██╗    ╚██╗██╔╝    
█████╗  ██║     ███████║█████╗  ██║     ███████║     ╚███╔╝     
██╔══╝  ██║     ██╔══██║██╔══╝  ██║     ██╔══██║     ██╔██╗     
██║     ███████╗██║  ██║██║     ███████╗██║  ██║    ██╔╝ ██╗    
╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝    ╚═╝  ╚═╝    
                                                                
███╗   ██╗██╗████████╗██████╗  ██████╗                          
████╗  ██║██║╚══██╔══╝██╔══██╗██╔═══██╗                         
██╔██╗ ██║██║   ██║   ██████╔╝██║   ██║                         
██║╚██╗██║██║   ██║   ██╔══██╗██║   ██║                         
██║ ╚████║██║   ██║   ██║  ██║╚██████╔╝                         
╚═╝  ╚═══╝╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝                          """)
    print("\n"+"#"*64+"\n")
    print("1 - Démarrer le script")
    print("2 - Voir le nombre de liens récupérés")
    print("3 - Supprimer les liens")
    print("4 - Quitter")
    choice = input("Votre choix : ")
    if choice == "1":
        start()
    elif choice == "2":
        print("Nombre de liens récupérés : " + str(counter()))
        menu()
    elif choice == "3":
        os.remove("liens.txt")
        menu()
    elif choice == "4":
        os.system('cls')
        exit()
    else:
        print("Veuillez entrer un choix valide !")
        menu()

def main():
    os.system('title Flafla x Discord')
    menu()

if __name__ == "__main__":
    main()