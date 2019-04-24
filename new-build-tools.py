# Run on a newly built kali machine to quickly download
# and install the following tools:
# Empire
# gobuster
# terminator
# Bloodhound

import subprocess

print("Downloading Empire.")
subprocess.call(["git", "clone", "https://github.com/EmpireProject/Empire.git"])
print("Done.")

print("Installing Empire.")
subprocess.call(["./Empire/setup/install.sh"])
print("Done.")

print("Downloading impacket.")
subprocess.call(["git", "clone", "https://github.com/SecureAuthCorp/impacket.git"])
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
