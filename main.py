import requests
from bs4 import BeautifulSoup
# beautifulsoup로 가져온 html 코드 내에서 필요한 . 거 찾을 수 있음.

# pagination

all_jobs = []


def scrape_page(url):
  print(f"Scrapping {url}...")
  response = requests.get(url)
  soup = BeautifulSoup(
      response.content,
      "html.parser",
  )
  jobs = soup.find("section", class_="jobs").find_all("li")[1:-1]

  for job in jobs:
    title = job.find("span", class_="title").text
    try:
      company = job.find("span", class_="company").text
    except AttributeError:
      company = None

    try:
      position = job.find("span", class_="position").text
    except AttributeError:
      position = None

    try:
      region = job.find("span", class_="region").text
    except AttributeError:
      region = None

    url = job.find("div", class_="tooltip--flag-logo").find_next("a")
    url = url.get("href") if url else None

    job_data = {
        "title": title,
        "company": company,
        "position": position,
        "region": region,
        "url": f"https://weworkremotely.com{url}",
    }
    all_jobs.append(job_data)


def get_pages(url):
  response = requests.get(url)
  soup = BeautifulSoup(response.content, "html.parser")
  return len(
      soup.find("div", class_="pagination").find_all("span", class_="page"))


total_pages = get_pages(
    "https://weworkremotely.com/remote-full-time-jobs?page=1")

# 몇 번 루프 돌릴지 제어가능
#  index에 0이 없으니깐 제외하도록 x+1로
for x in range(total_pages):
  url = f"https://weworkremotely.com/remote-full-time-jobs?page={x+1}"
  scrape_page(url)

print(len(all_jobs))




# -------------우회로 추가하는 법

keywords = ["flutter", "python", "golang"]

#  우회법은 웹사이트마다 다를 수 있으나...
# 검사 --> 네트워크 --> 처음 거 --> request header --> user-agent 값을 가져와서 아래처럼 만들어야 함. user라고 속이는 것임..ㅎ
r = requests.get(
    "https://remoteok.com/",
    headers={
        "User-Agent":
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
    })

# r = requests.get("https://remoteok.com/")
# 이러면 block 당한 거 확인 됨.
# print(r.status_code)
#  따라서 위처럼 우회하게 해야 함.

print(r.status_code)
from playwright.sync_api import sync_playwright
# 코드에 대기 시간을 줌. 
import time
from bs4 import BeautifulSoup

p = sync_playwright().start()

# headless는 작동하지만 안보이는 것이라서, 열린 페이지가 보이게 하려면, 
# headless=False를 넣어주면 됨. 
browser = p.chromium.launch(headless=False)

page = browser.new_page()

page.goto("https://www.wanted.co.kr/jobsfeed")

# 7초간 멈추면서 작동하는 것을 볼 수 있음. 
time.sleep(5)

# selector 쓰고 처음 class 명 가지고 오면 됨. 
page.click("button.Aside_searchButton__Xhqq3")

time.sleep(5)
 
#  class 명은 개발자가 바꿀 수도 있기 때문에 placeholder를 사용하는 것이 더 안전한 선택일 수도 있음. 
page.get_by_placeholder("검색어를 입력해 주세요.").fill("flutter")

time.sleep(5)

page.keyboard.down("Enter")

time.sleep(5)

# anchor의 a#id 이렇게 찾아주면 됨
page.click("a#search_tab_position")

for x in range(5):
    time.sleep(5)
    # end 키 없으면 걍 control + 화살표 위나 아래 누루면 스크롤이 내려감.
    page.keyboard.down("End")

content = print(page.content())

# playwrit를 멈춤
p.stop()


soup = BeautifulSoup(content, "html.parser")



# page.screenshot(path="screenshot.png")


# def plus(a, b):
#     return a + b

# # 1, 2는 positional argument 위에서 해당 위치에 들어가니깐. 
# #  만약에 plus(b=1, a= 2)로 바꾸면 keyword argument가 됨. 위치랑 상관없으니깐. 
# #  즉 순서를 외우지 않아도 됨. keyword를 먼저 사용하면 나중에 positional 사용 못함. 
# #  but, 처음을 positional로 시작하면, 뒤에 keyword 가능 plus(1, b=2) 
# #  그리고 처음만 positional이면 거의 처음 argument 빼고는 선택사항인 경우가 많음. 
# #  인자가 많을 때 주로 사용함. 
# plus(1, 2)
