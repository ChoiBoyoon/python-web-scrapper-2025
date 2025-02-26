# Request Headers : 브라우저가 서버에 보내는 정보
import requests
from bs4 import BeautifulSoup
import pandas as pd

# user agent is about browser information. cookies, encoding, https, languages, etc.
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"

url = "https://remoteok.com/remote-python-jobs"

response=requests.get(url)
print(response.status_code) #429. they're blocking scraping

response = requests.get(url, headers={
    "User-Agent": user_agent
})
print(response.status_code) #200