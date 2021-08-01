import requests


print ("Grabbing Proxies...")

url = 'https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=7000&country=US&anonymity=elite&ssl=no'
r = requests.get(url)
results = r.text

with open ("proxy.txt", "w") as file:
    file.write(results)