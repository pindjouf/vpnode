# vpnode

## What it is
Simple script to add new users to my vpn "blazingly-fast".

## How it works
Takes last octet in your main config's IP Address i.e. `/etc/wireguard/wg0.conf` and replaces it with a random one.\
Then it makes a new file in that same directory with the newly generated IP and a filename of your choosing.

Speaking of which it only works if your IP is 7 digits long, it still has a long way to go before being a nice polished product.\
I will improve it in my free time.\
Feel free to contribute if you feel the need.
