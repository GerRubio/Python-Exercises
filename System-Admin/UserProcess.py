# Show all the process running for this user.

import psutil, getpass, os

user_name = getpass.getuser()
process_dict = {proc.pid:proc.name() for proc in psutil.process_iter() if proc.username() == user_name}

print(process_dict)