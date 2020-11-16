# Create a file with some information from the PC to a JSON file.

import psutil, json

cpu_cores = psutil.cpu_count()
total_memory = psutil.virtual_memory().total
available_memory = psutil.virtual_memory().available
addresses = [addr.address for iface_addrs in psutil.net_if_addrs().values() for addr in filter(lambda x: x.family == 2, iface_addrs)]

# Dict with all information.
full_info = {'CPU Cores' : cpu_cores, 'Total Memory' : total_memory, 'Available Memory' : available_memory, 'Addresses' : addresses}

# Create JSON file.
with open('pc_info.json', 'w') as json_file:
  json.dump(full_info, json_file)