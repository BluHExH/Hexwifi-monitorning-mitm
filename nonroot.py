import os
import time
import requests
from termcolor import colored

# Telegram Config
BOT_TOKEN = "YOUR_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"

def print_banner():
    os.system("clear")
    print(colored("""
         ██╗  ██╗███████╗██╗  ██╗
         ██║  ██║██╔════╝╚██╗██╔╝
         ███████║█████╗   ╚███╔╝ 
         ██╔══██║██╔══╝   ██╔██╗ 
         ██║  ██║███████╗██╔╝ ██╗
         ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
             HEX WiFi Monitor
    """, 'cyan'))

def scan_network():
    print(colored("\n[+] Scanning network using nmap...", 'yellow'))
    os.system("nmap -sn 192.168.1.0/24 -oG result.txt")

    devices = []
    with open("result.txt", "r") as file:
        for line in file:
            if "Status: Up" in line or "Host:" in line:
                devices.append(line.strip())

    if devices:
        log_text = "\n".join(devices)
        print(colored("\n[+] Devices Found:\n", 'green') + log_text)
        save_log(log_text)
        send_telegram(log_text)
    else:
        print(colored("[!] No devices found!", 'red'))

def save_log(text):
    with open("device_log.txt", "a") as f:
        f.write(text + "\n\n")
    print(colored("[✓] Info saved to device_log.txt", 'green'))

def send_telegram(text):
    try:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        data = {
            "chat_id": CHAT_ID,
            "text": f"HEX WiFi Devices:\n{text}"
        }
        requests.post(url, data=data)
        print(colored("[✓] Info sent to Telegram!", 'green'))
    except:
        print(colored("[!] Failed to send to Telegram.", 'red'))

def main():
    print_banner()
    while True:
        print(colored("\n[1] Scan WiFi Devices", 'blue'))
        print(colored("[2] Exit", 'blue'))
        choice = input(colored("Select option: ", 'yellow'))

        if choice == "1":
            scan_network()
        elif choice == "2":
            print(colored("Exiting...", 'red'))
            break
        else:
            print(colored("Invalid choice!", 'red'))

if __name__ == "__main__":
    main()
