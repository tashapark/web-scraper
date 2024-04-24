import requests
from bs4 import BeautifulSoup
# beautifulsoup로 가져온 html 코드 내에서 필요한 . 거 찾을 수 있음.

# pagination

all_jobs = []

# 함수만들어서 아까 거 넣어줌 
def scrape_page(url):
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

    url = job.find("div", class_="tooltip--flag-logo").next_sibling["href"]

    job_data = {
        "title": title,
        "company": company,
        "position": position,
        "region": region,
        "url": f"https://weworkremotely.com{url}",
    }
    all_jobs.append(job_data)


response = requests.get(
    "https://weworkremotely.com/remote-full-time-jobs?page=1")

soup = BeautifulSoup(response.content, "html.parser")

buttons = len(
    soup.find("div", class_="pagination").find_all("span", class_="page"))

# 몇 번 루프 돌릴지 제어가능
#  index에 0이 없으니깐 제외하도록 x+1로
for x in range(buttons):
  print("request page", x + 1)
