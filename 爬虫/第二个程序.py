import requests

query = input("输入一个你喜欢的明星")

url = f'https://www.baidu.com/s?ie=UTF-8&wd={query}'

dic = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36"
}
resp = requests.get(url, headers=dic)
print(resp)
print(resp.text)
