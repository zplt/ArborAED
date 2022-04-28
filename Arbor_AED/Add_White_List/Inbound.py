import requests, urllib3, json

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://ARBOR_IP/api/aed/v2/protection-groups/whitelisted-hosts/"

List = []
# whitliste ip List
with open("ıpList","r") as file:
    List=file.readlines()
    file.close()

session = requests.session()
# Add Arbor Token to headers
headers = {'X-Arbux-APIToken': '///ARBORTOKEN///', 'Content-type': 'application/json'}


for i in List:
    i=str(i).strip("\n")
    data = {"hostAddress": f"{i}", "annotation": "UpitemTest"}
    print(data)
    r=requests.post(url, headers=headers,data=json.dumps(data), verify=False )
    print(r.text)


