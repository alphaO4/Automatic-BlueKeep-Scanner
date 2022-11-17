import requests
import shodan
import os

requests.packages.urllib3.disable_warnings()

API_KEY = os.environ.get('SHODAN_API_KEY')


SEARCH_FOR = 'vuln:"cve-2019-0708" country:DE'
f = open("urls.txt", "a")
api = shodan.Shodan(API_KEY)
result = api.search(SEARCH_FOR, limit=1000)
for service in result['matches']:
    IP = service['ip_str']
    url = "https://{}".format(IP)
    f.writelines(url+"\n")

print("[+] Found {} results.".format(result['total']))
