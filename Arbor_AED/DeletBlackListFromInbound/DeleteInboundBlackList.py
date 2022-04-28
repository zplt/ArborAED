import requests,urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
ip=input("Arbor_Ip: ").strip(" ")
token=str(input("Arbor_Token: ")).strip(" ")


url=f"https://{ip}/api/aed/v2/protection-groups/blacklisted-hosts"
param="/?hostAddress="
list=[]

with open("DeletList","r") as file:
    list=file.readlines()
    file.close()

headers = {'X-Arbux-APIToken':f'{token}'}

for i in list:
    i=str(i).strip("\n")
    full_path=(url+param+ f"{i}")
    r=requests.delete(full_path, headers=headers, verify=False )
    print(r.status_code)
    print(r.text)

