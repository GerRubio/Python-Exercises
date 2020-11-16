# Get the whole IPv4 from all interfaces AF_INET. 

import psutil

# Normal loop.
for iface_addrs in psutil.net_if_addrs().values():
    for addr in iface_addrs:
        if str(addr.family) == 2: # 2 = AddressFamily.AF_INET
            print(addr.address)

# Understanding list.
[addr.address for iface_addrs in psutil.net_if_addrs().values() for addr in filter(lambda x : x.family == 2, iface_addrs)]