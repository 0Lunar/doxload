#!/usr/bin/python3

import os

try:
    import requests as r
    from bs4 import BeautifulSoup as bs
    from colorama import Fore
except:
    if os.system("pip3 install requests bs4") != 0:
        os.system("pip install requests bs4")

def clean():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def banner():
    print(Fore.RED + '''    .___           .__                    .___
  __| _/_______  __|  |   _________     __| _/
 / __ |/  _ \\  \\/  /  |  /  _ \\__  \\   / __ | 
/ /_/ (  <_> >    <|  |_(  <_> ) __ \\_/ /_/ | 
\\____ |\\____/__/\\_ \\____/\\____(____  /\\____ | 
     \\/           \\/               \\/      \\/ 

            Made by LunarStone292

''' + Fore.RESET)

def download(url):
    if url.endswith("/"):
        url += "raw"
    elif url.endswith("/raw") == False:
        url += "/raw"
    req = r.get(url).text
    open("out.txt", "w").write(req)
    print(Fore.CYAN + "download completed!")

def checkURL(url):
    if url.startswith("https://doxbin"):
        name = url.split("/")
        if str(name[-1]) != "raw" and str(name[-1]) != "":
            print(Fore.CYAN + "\ndownloading " + str(name[-1]))
        else:
            print(Fore.CYAN + "\ndownloading " + str(name[-2]))
        download(url)
    else:
        print(Fore.RED + "Error, invalid URL")

def main():
    clean()
    banner()
    url = input(Fore.CYAN + "Enter the doxbin URL: ")
    checkURL(url)

if __name__ == "__main__":
    main()
