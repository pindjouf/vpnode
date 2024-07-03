#!/usr/bin/env python3

with open("/home/pindjouf/mediaman.conf", 'r') as base_conf:
    for line in base_conf:
        if line.startswith("Address"):
            string = line.strip()
            full_ip = string.split()[2] # awk the 3rd column
            cidr_index = full_ip.find('/')

            ip = full_ip[:cidr_index]
            cidr = full_ip[cidr_index:]

            ip_parts = ip.split(".")
            last_octet = int(ip_parts[3])

            if last_octet <= 254 and last_octet > 1:
                last_octet += 1
                ip_parts[3] = str(last_octet)
                new_ip = ".".join(ip_parts)
                print(new_ip)
