Terminal connect app

Script allows you to easily connect to your external terminal app.

You need to install python https://www.python.org/ and pyyaml https://pypi.org/project/PyYAML/ (best is to use pip - https://pypi.org/project/pip/)

This script was tested on Windows10, Ubuntu and Mac OS.

You need to download breakout app depend on your OS:

https://SERVER_IP/breakout/breakout-linux-x86_amd64

https://SERVER_IP/breakout/breakout-macos-x86_amd64

https://SERVER_IP/breakout/breakout-windows-x86_amd64.exe

You need to set your personal information before exec script. Open pycml.py for editing and set info according your account, server etc.:

username = "username"

password = "password"

controller = "https://192.168.1.1"

listen_address = "127.0.0.1"

Then run scipt with:

python3 pycml.py or python pycml.py depend on your python version

Version check: python --version

#Terminal app start:

For windows only, now terminal for all ports can be started automatically. By default Terminal start is disabled, strings need to be set:

terminal_start = False

crt = True

putty = False

terminal_start - will allow terminal app to start.

crt - if True, will start SecureCRT app.

putty - if True, will start Putty app.

If your SecureCRT/Putty app install dir. is not default, you need to change dir at app_start.py:

For SecureCrt:

crt_app = '"C:\Program Files\VanDyke Software\SecureCRT\SecureCRT.exe"'

For Putty:

putty_app = '"C:\Program Files\PuTTY\putty.exe"'