import requests,urllib3,random,GetCollection
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from datetime import datetime
time=datetime.now()

class StixObject:

    def __init__(self,ip,id,user,passwd):
        self.ip=ip
        self.id=id
        self.user=user
        self.passwd=passwd
        self.url=f"https://{self.ip}/taxii/root/collections/{self.id}/objects/"


    def AdBlackList(self,values):
        session=requests.session()
        session.auth=(f"{self.user}",f"{self.passwd}")
        aut=session.post(self.url,verify=False)
        headers={'Content-type': 'application/vnd.oasis.stix+json; version=2.0'}
        for i in values:
            randomA = random.randint(0, 1000)
            randomB = random.randint(0, 1000)
            json = {
                "id": "bundle--14d13cfb-cf39-4d5" + str(randomB) + "d-926e-a0b2892c6b" + str(randomA) + "a",
                "objects": [
                    {
                        "id": "indicator--754ed1e6-e1fa-49f" + str(randomA) + "-92c4-4710bb7ac3d" + str(randomB),
                        "labels": [
                            "bidirectional"
                        ],
                        "name": "Malicious Url",
                        "pattern": "[url:value = 'http://{}']".format(i),
                        "type": "indicator",
                        "valid_from": str(time)
                    }
                ],
                "spec_version": "2.0",
                "type": "bundle"
            }
            response = session.post(self.url, headers=headers, json=json, verify=False)
        session.close()
        print("Url(s) added")


    def GetBlackList(self):
        with open("Url", "r") as file:
            Lines = file.readlines()
            file.close()
        self.AdBlackList(Lines)

while True:
    try:
        Get_Collection
        ip=Get_Collection.ip
        id=Get_Collection.id
        user=Get_Collection.user
        passwd=Get_Collection.passwd
        s=StixObject(ip,id,user,passwd)
        s.GetBlackList()
        break
    except:
        print("hata")
        break