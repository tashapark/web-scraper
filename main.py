import requests
from bs4 import BeautifulSoup
# beautifulsoup로 가져온 html 코드 내에서 필요한 . 거 찾을 수 있음.

url = "https://weworkremotely.com/categories/remote-full-stack-programming-jobs"

# 스크래핑 할 페이지를 잘 들여다 보고, 필요없어서 지울 부분이나 가지고 올 것을 확인해야 함.
response = requests.get(url)

print(response.content)

soup = BeautifulSoup(
    response.content,
    "html.parser",
)
#  class_ 는 클래스와 헷갈리지 않도록.
# 파이썬은 리스트를 컷할 수 있는데, [0:5] 인덱스 0부터 5 앞까지. so, [1:-1]은 2번째 꺼부터 맨 마지막 꺼 바로 앞까지. => 양끝을 제외한다는 의미임.
jobs = soup.find("section", class_="jobs").find_all("li")[1:-1]

# soup안에 것은 전부 다 find로 가지고 올 수 있음. 그래서 job 안에서 도 find 매소드 사용 가능.
# .text를 하면 html이 아니라 값(txt)가 나타남.
# find는 처음 거 한 개만, 리스트는 find_all

#  list의 길이를 알고 있으면, 리스트를 unpack 가능.
#  letters = ['a', 'b', 'c'] 일 때, 각각을 부르게 할 때 변수를 일일히 인덱스에 따라서 지정하지 않고.
#  a,b,c = letters라고 하면, a 부르면, 'a' 출력됨. 매우.. 쉬워짐.
# 핵심은 변수명이 아니라, 개수임.. 개수가 맞아야 함.

all_jobs = []

for job in jobs:
  title = job.find("span", class_="title").text
  # .company가 3개가 있어서 처음부터 이름을 주고 시작.
  # 만약에 목록에서,, 없는 리스트가 있으면, 에러가 뜸.
  # none으로 나오게 바꿔줘야 함... 안 되고 에러 뜸.. 결국 try-except 사용..
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
  # none이 있으면 none이 출력되게 만드는 것. 혹시 빈 곳이 있을 까봐.
  # url = None
  # if url:
  #   url = url["href"]
  url = job.find("a")["href"]

  job_data = {
      "title": title,
      "company": company,
      "position": position,
      "region": region,
  }
  all_jobs.append(job_data)

print(all_jobs)
