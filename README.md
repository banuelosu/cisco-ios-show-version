# cisco-ios-show-version

### Prerequisites
```
python3
pip3 install netmiko
pip3 install getpass
```

### Python Modules Used
 - sys
 - os
 - getpass
 - netmiko
 
### How to run
```
python3 main.py <path-to-file>
```
The script will loop through the devices within the file and run 'show version'. The results will be printed to screen.

Notes:
```
if Command "python setup.py egg_info" failed with error code 1
pip3 install --upgrade setuptools

if fatal error: openssl/opensslv.h
sudo apt-get install python-pip python-dev libffi-dev libssl-dev libxml2-dev libxslt1-dev libjpeg8-dev zlib1g-dev
```
