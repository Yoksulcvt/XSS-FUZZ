import requests
import argparse
import pyfiglet
import os
from colorama import Fore, init

init(autoreset=False)

parser = argparse.ArgumentParser(description="XSS-FUZZ verdiğiniz url ")

parser.add_argument("-t","--target", type=str, help="Hedef url")
parser.add_argument("-p","--payload-list", help="Payload listesini buraya verebilirsiniz ")

args = parser.parse_args()

def banner():
    os.system("clear")
    banner = pyfiglet.figlet_format("XSS-FUZZ" ,font='slant')
    print(Fore.BLUE+banner)
    print(Fore.BLUE + "github.com/Yoksulcvt\n")


hedef_url = args.target
payloadlist = args.payload_list

def xssfuzz(hedef_url):
    banner()
    if hedef_url == None:
        return print(Fore.RED + "lütfen hedefi giriniz | --target http://example.com")
    elif payloadlist == None:
        return print(Fore.RED + "lütfen xss payloadlarını giriniz | --payload-list payload.txt")
    
    if hedef_url.startswith(("http://" ,"https://")):
        hedef_url = hedef_url
    else:
        hedef_url = "https://"+hedef_url
    
    try:  

        with open(payloadlist, "r" ,encoding='utf-8')as f:
            payloads = [satır.strip() for satır in f if satır.strip]
        if not "XSS" in hedef_url:
            return print(Fore.RED +"Lütfen Fuzz uyguluyacağınız Parametreye 'XSS' yazarak seçiniz")  
        for payload in payloads:
                    
            url = hedef_url.replace("XSS", payload) 
            r = requests.get(url=url, timeout=10)
            if payload in r.text:
                print(Fore.GREEN + f"ZAFİYET ÇALIŞTI: {url}")
                break
            else:
                print(Fore.RED +f"zafiyet çalışmadı: {url}")
    except Exception as e:
            print(Fore.RED + "Hata: ", e)


if __name__ == "__main__":
    xssfuzz(hedef_url)