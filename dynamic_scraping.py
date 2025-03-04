# playwright을 이용하기 위해선 real browser가 필요함. 이젠 replit이 아니라 우리 컴퓨터에서 실행해야 함.
# 컴퓨터에 파이썬, VSCode 설치해놓기.
# pip: 우리 컴퓨터에 파이썬 패키지를 설치할 수 있게 해줌. 
# pip install playwright
# playwright install -> 브라우저를 설치해 줌. Chromium, Firefox, Webkit, FFMPEG 설치됐다고 뜸!

# playwright를 작동시키는 방법
# sync: 쉬운 버전
# async: 많은 브라우저를 parallel하기 작동시킴
from playwright.sync_api import sync_playwright 

p = sync_playwright().start() #instantiation and start
browser = p.chromium.launch(headless = False) #크롬 브라우저를 시작
page = browser.new_page() #브라우저에서 새로운 탭을 열어줌 (새로운 페이지)
keyword = 'python'
url = f"https://remoteok.com/remote-{keyword}-jobs"
page.goto(url)
page.screenshot(path = 'remoteok_screeneshot.png') # 스크린샷을 찍음. headless mode: default. 컴퓨터에서 브라우저를 실행시키지만 우리한테 보여주진 않음.