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
