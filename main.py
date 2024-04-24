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
