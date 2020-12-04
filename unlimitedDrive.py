import requests, sys


print("Insert your Google Email Address")
email = input()
if not '@gmail' in email:	sys.exit(0)
url = "https://gd.zxd.workers.dev/drive"
data = {
  "teamDriveName": "Unlimited Drive",
  "teamDriveThemeId": "random",
  "emailAddress": email
}
headers = {"Accept": "*/*","Accept-Encoding": "gzip, deflate, br","Accept-Language": "it-it","Connection": "keep-alive","Content-Length": "103","Content-Type": "application/json","Host": "gd.zxd.workers.dev","Origin": "https://gd.zxd.workers.dev","Referer": "https://gd.zxd.workers.dev/","User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Mobile/15E148 Safari/604.1","X-Requested-With": "XMLHttpRequest",}

response = requests.post(url = url, headers = headers, json = data)
print(response.status_code)
print(response.content)