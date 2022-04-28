import requests,urllib3,json
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)



def get_colletion_name(url, collection_name):
    global id
    session = requests.session()
    headers = {'Content-type': 'application/vnd.oasis.stix+json; version=2.0'}
    session.auth = (f"{user}", f"{passwd}")
    aut = session.post(url, verify=False)
    r = session.get(url, headers=headers, verify=False)
    response = json.loads(r.text)

    for i in range(1, 20):
        if response["collections"][i]["title"] == collection_name:
            print("id: ", response["collections"][i]["id"])
            id=response["collections"][i]["id"]
            break
        else:
            pass

def collection(ip):
        url = f"https://{ip}/taxii/root/collections"
        collection_name = str(input("Collection Name: "))
        get_colletion_name(url, collection_name)


ip = str(input("ip : ")).strip(" ")
user=str(input("user: ")).strip(" ")
passwd=str(input("password: "))
collection(ip)