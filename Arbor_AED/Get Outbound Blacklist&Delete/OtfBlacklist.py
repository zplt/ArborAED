import requests, urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class Blacklist:

    def __init__(self, ip, token, returPage):
        self.ip = ip
        self.token = token
        self.returPage = returPage
        self.List = []

    def get_blacklist(self):
        param = f"?perPage={self.returPage}"
        url = f"https://{self.ip}/api/aed/v2/otf/blacklisted-hosts/{param}"
        header = {'X-Arbux-APIToken': f'{self.token}', 'Accept': 'text/csv'}
        session = requests.session()
        r = session.get(url, headers=header, verify=False)
        result = r.text.split()
        for i in result:
            self.List.append(i.strip(","))
        return self.List

    def delet_blakclist(self):
        url = f"https://{self.ip}/api/aed/v2/otf/blacklisted-hosts/?hostAddress="
        header = {'X-Arbux-APIToken': f'{self.token}'}
        session = requests.session()
        for i in self.List:
            i = str(i).strip("\n")
            full_path = (url + f"{i}")
            r = session.delete(full_path, headers=header, verify=False)
            if str(r.status_code) == "204":
                print(f"{i} adress deleted")

while True:
    try:
        ip = str(input("ip: ")).strip(" ")
        token = str(input("Token: ")).strip(" ")
        # The number of results returned per page
        returPage = str(input("Return Page: "))
        blacklist = Blacklist(ip, token, returPage)
        List01 = blacklist.get_blacklist()
        a = input("Do you want to delete ip list from blacklist(y/n): ")
        if a.lower() == "y":
            blacklist.delet_blakclist()
        else:
            b = input("Do you want to extract ip list as a text file(y/n): ")
            if b.lower() == "y":
                with open("Extracted Ip List", "w") as file:
                    for i in List01:
                        file.write("%s\n" % i)
            else:
                break
        break
    except SyntaxError as err :
        print("Error: {}".format(err))
        break

