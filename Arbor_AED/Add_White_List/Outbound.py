import requests,urllib3,json
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url="https://ARBOR_IP/api/aed/v2/otf/whitelisted-hosts/"

List=[]
# whitliste ip List
with open("ıpList","r") as file:
    List=file.readlines()
    file.close()

session = requests.session()
# Add Arbor Token to headersm
headers = {'X-Arbux-APIToken':'cIvoVXWSBIptHuH3DXmgo8imCLmqyu2KPhSUvg8N', 'Content-type': 'application/json'}


for i in List:
    i=str(i).strip("\n")
    data = {"hostAddress": f"{i}", "annotation": "UpitemTest"}
    print(data)
    r=requests.post(url, headers=headers,data=json.dumps(data), verify=False )
    print(r.text)
