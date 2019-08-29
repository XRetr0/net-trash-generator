import requests
import random

dict = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
gen_num = int(input("Generation length (recommended length 6 symbols): "))
domain = str(input("Domain: "))
while 1:
    url = 'http://'
    for x in range(0,gen_num):
        url = url + random.choice(dict)
        
    url = url + domain
    print("generated url: "+url)
    try:
        req = requests.get(url)
        print("connection done")
        
        with open('result.txt', 'a') as file:
            file.write(url +'\n')
    except:
        print("connection error")
