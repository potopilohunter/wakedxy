# Installation du module python-nmap
# pip install python-nmap

import nmap
import os

sc = nmap.PortScanner()

print("""
__  _  _______  |  | __ ____   __| _/__  ______.__.
\ \/ \/ /\__  \ |  |/ // __ \ / __ |\  \/  <   |  |
 \     /  / __ \|    <\  ___// /_/ | >    < \___  |
  \/\_/  ____  /__|_ \\___  >____ |/__/\_ \/ ____|
              \/     \/    \/     \/      \/\/     /
""")


def main():
    choice = input("1- Network scanner\n2- Vulnerabilities detection\n3- Exploit\n\nPlease enter a number: ")
    
    if choice == '1':
        nmap_scan()
        
    elif choice == '2':
        vuln()
        
    elif choice == '3':
        os.system('msfconsole')
        
    else:
        print('Please choose a number between 1 and 3')

        
def nmap_scan():
    print("******************** Welcome to the Network scanner ********************")
    print("**********************************************************************")
    ip = input("\nPlease enter the IP address: ")
    sc.scan(ip, '1-1024')
    print(sc.scaninfo())
    print(sc[ip]['tcp'].keys())
    
    
def vuln():
    print("******************** Welcome to the Vulnerabilities scanner ********************")
    print("**********************************************************************")
    ip = input("\nPlease enter the IP address: ")
    os.system('nmap -sv --script=vulscan.nse ' + ip)


if __name__ == "__main__":
    main()
