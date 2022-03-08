import socket
import subprocess
import platform
import sys
import os
from datetime import *
from colorama import *



target = sys.argv[1]
target_ip = socket.gethostbyname(target)

tstart = datetime.now()



def start_1():
    subprocess.call("cls", shell=True)
    print("")
    print("")
    print(Fore.GREEN + "         ________  ________  ________  _________  _______   ________     ")
    print("        |\   __  \|\   __  \|\   __  \|\___   ___\\  ___ \ |\   __  \    ")
    print("        \ \  \|\  \ \  \|\  \ \  \|\  \|___ \  \_\ \   __/|\ \  \|\  \   ")
    print("         \ \   ____\ \  \\\  \ \   _  _\   \ \  \ \ \  \_|/_\ \   _  _\  ")
    print("          \ \  \___|\ \  \\\  \ \  \\  \|   \ \  \ \ \  \_|\ \ \  \\  \| ")
    print("           \ \__\    \ \_______\ \__\\ _\    \ \__\ \ \_______\ \__\\ _\ ")
    print("            \|__|     \|_______|\|__|\|__|    \|__|  \|_______|\|__|\|__|" + Style.RESET_ALL)
    print("")
    print("")
    print("")

    print(Fore.GREEN + Back.MAGENTA + " System Info: " + Style.RESET_ALL)
    print("")
    print("")

    print(Back.BLUE + " OS: " + Style.RESET_ALL + " " + Back.YELLOW + Fore.BLUE + " " + platform.system() + " " + Style.RESET_ALL)
    print("")
    print(Back.BLUE + " RELEASE: " + Style.RESET_ALL + " " + Back.YELLOW + Fore.BLUE + " " + platform.release() + " " + Style.RESET_ALL)
    print("")
    print(Back.BLUE + " NAME: " + Style.RESET_ALL + " " + Back.YELLOW + Fore.BLUE + " " + os.name + " " + Style.RESET_ALL)
    print("")
    print("")



def versions():
    print("")
    print("PORTS: ")
    print("")
    print("21: FTP")
    print("22: SSH")
    print("23: TELNET")
    print("25: SMTP")
    print("80: HTTP")
    print("443: HTTPS")
    print("")



def start_scanning():
    print(Back.GREEN + Fore.BLACK + " OPEN PORTS: " + Style.RESET_ALL)
    print("")

    try:
        for p in range(1, 80):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            res = sock.connect_ex((target_ip, p))
            if res == 0:
                print("  " + Back.MAGENTA + str(p) + Style.RESET_ALL + Fore.GREEN + " OPEN" + Style.RESET_ALL)
            sock.close()

    except Exception:
        print(Back.RED + Fore.YELLOW + " ERROR!!! " + Style.RESET_ALL)
        sys.exit()

    tend = datetime.now()
    diff = tend - tstart

    print("")
    print("")

    print(Back.GREEN + Fore.BLACK + " Scan completed in: " + str(diff) + " " + Style.RESET_ALL)


start_1()
versions()
start_scanning()
