# Run on a newly built kali machine to quickly download
# and install the following tools:
# Empire
# CrackMapExec
# Sublist3r
# Gobuster
# Terminator
# Bloodhound
# Idle
# Docker

import subprocess
import os

print("Downloading Empire.")
subprocess.call(["git", "clone", "https://github.com/EmpireProject/Empire.git"])
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

print("Docker time")
print("Adding Docker PGP key")
subprocess.call(["curl", "-fsSL", "https://download.docker.com/linux/debian/gpg", "-o", "key.txt"])
subprocess.call(["apt-key", "add", "key.txt"])
subprocess.call(["rm", "key.txt"])
print("Done.")
print("Adding Docker APT repository")
subprocess.call(["echo", "'deb", "[arch=amd64]", "https://download.docker.com/linux/debian", "buster", "stable'", ">", "/etc/apt/sources.list.d/docker.list"])
print("Done.")
print("updating..")
subprocess.call(["apt-get", "update"])
print("Done.")
print("Removing any old versions of Docker")
subprocess.call(["apt-get", "remove", "docker", "docker-engine", "docker.io"])
print("Done")
print("Installing Docker")
subprocess.call(["apt-get", "install", "docker-ce"])
print("Done")

update = input("Would you like to run updates as well? [Y/N] ")

if update == "Y":
    print("Ok, running updates.")
    subprocess.call(["apt-get", "update"])
    subprocess.call(["apt-get", "upgrade", "-y"])
    subprocess.call(["apt-get", "dist-upgrade", "-y"])
    subprocess.call(["apt", "autoremove", "-y"])

else:
    pass

print("All done!")
print("Note: Empire isn't installed. Run the install.sh script at Empire/setup/install.sh.")
