# Run on a newly built kali machine to quickly download
# and install the following tools:
# Empire
# CrackMapExec
# Sublist3r
# Gobuster
# Terminator
# Bloodhound
# Idle

import subprocess
import os

print("Downloading Empire.")
subprocess.call(["git", "clone", "https://github.com/EmpireProject/Empire.git"])
print("Done.")

print("Installing Empire.")
subprocess.call(["pip", "install", "-r" "Empire/setup/requirements.txt"])
subprocess.call(["./Empire/setup/install.sh"])
print("Done.")

print("Downloading CrackMapExec.")
subprocess.call(["git", "clone", "--recursive", "https://github.com/byt3bl33d3r/CrackMapExec.git"])
print("Done.")

print("Installing CrackMapExec")
os.chdir('CrackMapExec/')
subprocess.call(["./setup.py", "install"])

print("Running cme first time setup")
subprocess.call(["cme"])

print("Downloading sublist3r.")
subprocess.call(["git", "clone", "https://github.com/aboul3la/Sublist3r.git"])
print("Done.")

print("Installing sublist3r.")
subprocess.call(["pip", "install", "-r" "Sublist3r/requirements.txt"])
print("Done.")

print("Downloading gobuster.")
subprocess.call(["apt-get", "install", "gobuster", "-y"])
print("Done.")

print("Downloading terminator.")
subprocess.call(["apt-get", "install", "terminator", "-y"])
print("Done.")

print("Downloading Bloodhound.")
subprocess.call(["apt-get", "install", "bloodhound", "-y"])
print("Done.")

print("Downloading idle.")
subprocess.call(["apt-get", "install", "idle", "-y"])
print("Done.")

print("All done!")
