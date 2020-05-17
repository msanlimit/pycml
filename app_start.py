import os
from subprocess import Popen as new

def app_run(ports,label,crt,putty):

 if crt == True:
   #secureCRT
   crt_app = '"C:\\Program Files\\VanDyke Software\\SecureCRT\\SecureCRT.exe"'
   args_lab = " /N "
   args = " /T /TELNET 127.0.0.1 "
   labe = 0

   for port in ports:
      thr = new((crt_app + args_lab + label[labe] + args + str(port)),shell=False)
      labe = labe + 1
 elif putty == True:
  #putty
   putty_app = '"C:\\Program Files\\PuTTY\\putty.exe"'
   args = " telnet://127.0.0.1:"
   lab = " -loghost "
   labe = 0
   for port in ports:
     thr = new((putty_app + args + str(port) + lab + label[labe]),shell=False)
     labe = labe + 1