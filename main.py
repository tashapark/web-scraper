from playwright.sync_api import sync_playwright
# 코드에 대기 시간을 줌. 
import time
from bs4 import BeautifulSoup
import csv

p = sync_playwright().start()

# headless는 작동하지만 안보이는 것이라서, 열린 페이지가 보이게 하려면, 
# headless=False를 넣어주면 됨. 
browser = p.chromium.launch(headless=False)

page = browser.new_page()

# 아래 코드는 어떻게 진행되는 지 보여주기 위함이고, 사실은 url만 있으면 끝임 
page.goto("https://www.wanted.co.kr/search?query=flutter&tab=position")

# # 7초간 멈추면서 작동하는 것을 볼 수 있음. 
# time.sleep(5)

# # selector 쓰고 처음 class 명 가지고 오면 됨. 
# page.click("button.Aside_searchButton__Xhqq3")

# time.sleep(5)
 
# #  class 명은 개발자가 바꿀 수도 있기 때문에 placeholder를 사용하는 것이 더 안전한 선택일 수도 있음. 
# page.get_by_placeholder("검색어를 입력해 주세요.").fill("flutter")

# time.sleep(5)

# page.keyboard.down("Enter")

# time.sleep(5)

# # anchor의 a#id 이렇게 찾아주면 됨
# page.click("a#search_tab_position")

for x in range(5):
    time.sleep(5)
    # end 키 없으면 걍 control + 화살표 위나 아래 누루면 스크롤이 내려감.
    page.keyboard.down("End")

content = page.content()

# playwrit를 멈춤
p.stop()


soup = BeautifulSoup(content, "html.parser")

jobs = soup.find_all("div", class_="JobCard_container__FqChn")

jobs_db = []

for job in jobs:
    # 속성 은 전부 다 [] 안에 들어갈 수 있음.
    link = f"https://www.wanted.co.kr{job.find('a')['href']}"
    title = job.find("strong", class_="JobCard_title__ddkwM").text
    company_name = job.find("span", class_="JobCard_companyName__vZMqJ").text
    reward = job.find("span", class_="JobCard_reward__sdyHn").text
    job ={ 
        "title":title,
        "company_name":company_name,
        "reward":reward,
        "link":link
    }
    jobs_db.append(job)

# print(jobs_db)
# print(len(jobs_db))

# mode "r"이 디폴트고 읽기 전용이라서 w로 열어줌 
file = open("jobs.csv", "w")
# csv에 행을 추가하게 해줌
writer = csv.writer(file)
# writerow는 리스트만 보내고, 딕셔너리가 안됌.
# 파이썬에 밸류나 키를 가져오게 하는 함수가 이미 있음. 
# .values(), .keys()
writer.writerow([
    "Title","Company","Reward", "Link",
    ])

for job in jobs_db:
    writer.writerow(job.values())
file.close()

keywords = [
    "flutter",
    "nextjs",
    "kotlin"
]