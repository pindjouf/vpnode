#!/usr/bin/env python3
import random, os

new = input("Give a name your new .conf: ")

try:
    with open("/etc/wireguard/wg0.conf", 'r') as base_conf:
        with open(f"/etc/wireguard/{new}.conf", 'w') as new_conf:
            for line in base_conf:
                if line[:7] == "Address":
                    string = line # "Grep" address line
                    ip = list(string[10:])
                    ip[9:10] = str(random.randint(1, 255))
                    new_ip = ''.join(ip)
                    new_conf.write(f"Address = {new_ip}")
                else:
                    new_conf.write(line)

except PermissionError:
    print("[Permission Denied] Gotta use sudo my man...")

finally:
    os.system("clear")
    print(f"/etc/wireguard/{new}.conf\nHas been created!")
