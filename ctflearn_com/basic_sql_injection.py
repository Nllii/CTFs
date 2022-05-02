import requests

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Origin': 'https://web.ctflearn.com',
    # 'Content-Length': '10',
    'Accept-Language': 'en-us',
    'Host': 'web.ctflearn.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15',
    'Referer': 'https://web.ctflearn.com/web4/',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
}

data = {
    'input': 'Luke',
}

response = requests.post('https://web.ctflearn.com/web4/', headers=headers, data=data)
print(response.text)