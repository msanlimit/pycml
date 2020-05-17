import yaml
import os
import platform
import app_start
from subprocess import Popen as new

#user data
username = "username"
password = "password"
controller = "https://192.168.1.1"
listen_address = "127.0.0.1"
verify_tls = False
enabled = True

terminal_start = False
crt = True
putty = False




#package name set
os_win = "Windows"
os_linux = "Linux"
os_mac = "Darwin"
win_pack = "breakout-windows-x86_amd64.exe"
lin_pack = "./breakout-linux-x86_amd64"
mac_pack = "./breakout-macos-x86_amd64"






# run key
config = "config"
init = "init"
run = "run"


cur_os = platform.system()
pkg_name = ""

if cur_os == os_linux:
  pkg_name = lin_pack
elif cur_os == os_win:
  pkg_name =  win_pack
elif cur_os == os_mac:
  pkg_name = mac_pack
print(pkg_name)
 #config.yaml created
os.system(pkg_name + " " + config)


#config.yaml tweak
with open("config.yaml") as file:
    list_conf = yaml.safe_load(file)


list_conf["controller"] = controller
list_conf["listen_address"] = listen_address
list_conf["password"] = password
list_conf["username"] = username
list_conf["verify_tls"] = verify_tls

with open("config.yaml", "w") as f:
    yaml.dump(list_conf, f)


#labs.yaml created
os.system(pkg_name + " " + init)

#labs.yaml tweak
lab_id = []
lab_ports = []
label = []
port_num = 0
with open("labs.yaml") as file:
    list_labs = yaml.safe_load(file)

for list in list_labs:
	lab_id.append(list)
	

for lab in lab_id:
 list_labs[lab]['enabled'] = enabled
 for node in list_labs[lab]['nodes']:
	 label.append(list_labs[lab]['nodes'][node]['label'])
	 if list_labs[lab]['nodes'][node]['devices'][0]['listen_port'] > port_num:
	     port_num = (list_labs[lab]['nodes'][node]['devices'][0]['listen_port'])
	     lab_ports.append(port_num)
	 else:
		 port_num = port_num + 2
		 list_labs[lab]['nodes'][node]['devices'][0]['listen_port'] = port_num
		 lab_ports.append(port_num)
		 list_labs[lab]['nodes'][node]['devices'][1]['listen_port'] = port_num + 1



with open("labs.yaml", "w") as f:
    yaml.dump(list_labs, f)



#run
#os.system(pkg_name + " " + run)
p1 = new(pkg_name + " " + run, shell=False)
if terminal_start == True:
 p2 = new(app_start.app_run(lab_ports,label,crt,putty),shell=False)



	