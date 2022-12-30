import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Host": "uat-contentlibrary.midea-group.com"
}
res = requests.get("https://uat-contentlibrary.midea-group.com/libs/granite/csrf/token.json", headers=header, verify=False)

print(res.status_code)
