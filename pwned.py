#TMFS24 05/2019
#Calls Troy Hunt's pwnedpassword API see: https://www.troyhunt.com/ive-just-launched-pwned-passwords-version-2/#cloudflareprivacyandkanonymity

from getpass import getpass
import hashlib
import requests


password = getpass("Enter Password:")

passhash = hashlib.sha1(password.encode()).hexdigest().upper()
#print(passhash[5:])
partial = passhash[:5].upper()

response = requests.get('https://api.pwnedpasswords.com/range/'+partial)

#print(response.status_code)
if response.status_code == 200:
    print('Partial Hash Found...')

    for line in response.text.splitlines():
        #print(line)
        #print(line.split(":")[0])
        if line.split(":")[0] == passhash[5:]:
            print("Password Hash: " + partial + line.split(":")[0]+" Found!")
            print(line.split(":")[1] + " occurences.")

elif response.status_code == 404:
    print('Partial Hash Not Found.')



