#The code below creates a random key
#requires requests library (pip install requests)
import requests
RandomKeyApiUrl = 'https://raw.githubusercontent.com/kronikles000/SimpleRandomKeyGenerator1/refs/heads/main/RandomKeyAPI.py' #dont change this
RandomKeyApiCode = requests.get(RandomKeyApiUrl, timeout=10).text

createdkey = '0'
keylength = 20 #20 by default, set it to whatever

#print(RandomKeyApiCode)
namespace = {'keylength': keylength}

exec(RandomKeyApiCode, namespace)

createdkey = namespace['createdkey']

print(f'{createdkey}')
print('1')