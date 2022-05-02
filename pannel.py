# This Tool Was Made By @5nz#2606 For Educational Purposes Only! 🙂


from pystyle import *
import base64
import fade
import os
from os import system
import sys

sys.stdout.write('\x1b[8;{rows};{cols}t'.format(rows=15, cols=90))

os.system('cls' if os.name == "nt" else 'clear')
system(f'title NZ TOOL DISCORD: @5nz#2606 ^| THIS TOOL WAS MADE FOR EDUCATIONAL PURPOSES ONLY')
nz = """
 ███▄    █ ▒███████▒   ▄▄▄█████▓ ▒█████   ▒█████   ██▓    
 ██ ▀█   █ ▒ ▒ ▒ ▄▀░   ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    
▓██  ▀█ ██▒░ ▒ ▄▀▒░    ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    
▓██▒  ▐▌██▒  ▄▀▒   ░   ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░    
▒██░   ▓██░▒███████▒     ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒
░ ▒░   ▒ ▒ ░▒▒ ▓░▒░▒     ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░
░ ░░   ░ ▒░░░▒ ▒ ░ ▒       ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░
   ░   ░ ░ ░ ░ ░ ░ ░     ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   
         ░   ░ ░                    ░ ░      ░ ░      ░  ░
           ░  
"""

nz2 = fade.brazil(nz)
print(nz2)
Write.Print(
        "                       * This Tool Was Made By 5nz For Educational Purposes ONLY *\n",
        Colors.green_to_yellow, interval=0.01)

uid = Write.Input(" Enter Discord ID>  ", Colors.cyan_to_blue, interval=0.1, hide_cursor=True)
results = base64.b64encode(str(uid).encode()).decode()
Write.Print({results},Colors.red_to_blue)