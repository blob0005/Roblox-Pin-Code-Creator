anyerror = False
try:
  import requests
  import colorama
except:
  anyerror = True
if anyerror == True:
  print("Missing Module(s), Press Enter To Start Repair Process (Wont Always Work)")
  input("")
  try:
    import os
    os.system("pip install requests")
    os.system("pip install colorama")
    print("Problems Should Be Fixed Now, Restart The Program")
    input("")
    exit()
  except:
    print("Error While Fixing, Sorry")
    input("")
    exit()
try:
    import os
    from os import system
    system("title " + "Roblox Pin Code Creator,   Made By blob#0005,   Github: github.com/blob0005")
except:
    pass
colorama.init(autoreset=True)
while True:
    try:
        cookie = input("Enter Cookie: ")
        r = requests.get("https://www.roblox.com/mobileapi/userinfo", cookies={".ROBLOSECURITY": cookie}).json()
        break
    except:
        print("Cookie Invalid")



pin = input("What Shall Pin Be: ")

req = requests.session()
req.cookies.set(".ROBLOSECURITY", str(cookie), domain="roblox.com")
url = "https://auth.roblox.com/v1/account/pin"
lol = req.post("https://auth.roblox.com/v1/account/pin/unlock")
token = str(lol.headers["x-csrf-token"])
headers = {
    "x-csrf-token": token
}

json = {
    "pin": int(pin)
}

re = req.post(url=url, headers=headers, json=json)

re = str(re)

if "200" in re:
    print(colorama.Fore.GREEN + "Succsesfully Created Pin")
if "200" not in re:
    print(colorama.Fore.RED + "Failed To Set Pin")


input("")
exit()
