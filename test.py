from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import time

def scroll_down(page):
    """스크롤을 끝까지 내려서 모든 데이터를 로딩하는 함수"""
    prev_height = -1
    while True:
        # 현재 scrollHeight 확인
        curr_height = page.evaluate("document.body.scrollHeight")

        # 페이지 끝까지 스크롤
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(2)  # 데이터 로딩 대기

        # 새로운 데이터가 없으면 스크롤 중지
        if curr_height == prev_height:
            break
        prev_height = curr_height

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # 페이지 이동
    page.goto("https://www.wanted.co.kr/search?query=flutter&tab=position")

    # 스크롤을 끝까지 내려서 모든 데이터를 로딩
    scroll_down(page)

    # ✅ 렌더링된 최종 HTML 가져오기
    content = page.evaluate("document.documentElement.outerHTML")

    browser.close()

# BeautifulSoup으로 파싱
soup = BeautifulSoup(content, "html.parser")

# ✅ HTML 구조를 분석하여 채용 공고 리스트 가져오기
jobs_list = soup.find_all("div", class_="JobCard_container__REty8")

print(f"총 {len(jobs_list)}개의 채용 공고를 가져왔습니다.")

# 각 채용 공고의 제목과 회사명 출력
for job in jobs_list:
    title = job.find("strong").text.strip() if job.find("strong") else "제목 없음"
    company = job.find("span", class_="JobCard_companyName__vZMqJ").text.strip() if job.find("span", class_="JobCard_companyName__vZMqJ") else "회사 없음"
    print(title, "-", company)
