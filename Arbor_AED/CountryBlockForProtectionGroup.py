import requests, urllib3,json
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class Country():

    def __init__(self, url,url_get, token):
        self.url = url
        self.url_get = url_get
        self.token = token

    def get_inf(self,pgid,headers):
        param_pg = f"pgid={pgid}"
        url_get = self.url_get + param_pg
        r = requests.get(url_get, headers=headers, verify=False)
        result=r.text
        result = json.loads(result)
        k = len(result["blacklisted-countries"])
        for i in range(0, k):
            a = result["blacklisted-countries"][i]["country"]
            print(a)

    def add_blackCountry(self):
        pgid = str(input("Protection Group id: "))
        country = str(input("Country (Country:ES || Country:ES,AU,...) : ")).upper()
        protection_group = f"&pgid={pgid}"
        url = self.url + str(country) + protection_group
        token = self.token.strip(" ")
        headers = {"X-Arbux-APIToken": f"{token}"}
        r = requests.post(url, headers=headers, verify=False)
        print("Added")
        self.get_inf(pgid, headers)

    def delet_blackCountry(self):
        pgid = str(input("Protection Group id: "))
        country = str(input("Country (Country:ES || Country:ES,AU,...) : ")).upper()
        protection_group = f"&pgid={pgid}"
        url = self.url + str(country) + protection_group
        token = self.token.strip(" ")
        headers = {"X-Arbux-APIToken": f"{token}"}
        r = requests.delete(url, headers=headers, verify=False)
        print("Deleted!!")
        self.get_inf(pgid, headers)




print("""
            ##########################################
            #          ********//*\\*******          #
            #          **ARBOR AED 6.4.X **          #
            #          ********************          #
            ##########################################
Choose protection Group id. example: 'view/?id=82', id=82
For Country code plase visit to 'https://en.wikipedia.org/wiki/Country_codes:_T' address, under the 'ISO 3166-1 alpha-2 '
ES:spain,AU:australia,AD:andorra
""")

arbor = str(input("arbor ip:"))
url = f"https://{arbor}/api/aps/v1/protection-groups/blacklisted-countries/?country="
url_get=f"https://{arbor}/api/aps/v1/protection-groups/blacklisted-countries/?"
token = str(input("AborToken : "))
c = Country(url,url_get, token)
while True:
    try:

        a = input("Ad(a) ,Delete(d) or Exit(e) Country   (a/d/e): ")
        if a.lower() == "a":
            c.add_blackCountry()
        elif a.lower() == "d":
            c.delet_blackCountry()
        elif a.lower() == "e":
            break
        else:
            print("Just choose ad(a) , delete(d) or exit(e)")
    except:
        print("Opss!!")
        break