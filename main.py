from requests import get

# tuple이나 list를 만들 때 복수형을 사용함. 
websites = (
    "google.com",
    "https://twitter.com",
    "airbnb.com",
    "facebook.com",
    "https://tictok.com"
)

results = {}

# for in에서는 for website(item) in websites: 이런 식으로 사용함. 

# but, 원하는 대로 사용하면 됨. 
for website in websites: 
    # startswith는 불리안을 주는 것. 
    # if website.startswith("https://"):
    #     print("good to go")
    # else: 
    #     print("we have to fix it.")
    # not 붙여서 고쳐야 하는 것에 집중하는 방법 
    # if website.startswith("https://") == False: 로 쓸 수도 있음. 
    if not website.startswith("https://"):
        website = f"https://{website}"
    # response를 return 해줌 
    # response는 웹사이트의 응답임
    response = get(website)
    # status_code 만 보이게 글 없이
    if response.status_code < 199:
        # 결과 값은 : 로 나옮. \
        results[website] = "Informational"
        # print(f"{website} is OK")
    elif response.status_code < 299:
        results[website] = "Success"
    elif response.status_code < 399:
        results[website] = 'Redirection'
    elif response.status_code < 499:
        results[website] = 'Client Error'
    else:
        results[website] = 'Server Error'


print(results)
# PyPi 스탠다드 라이브러리에 없는 것을 여기서 찾으면 됨. 
# requests는 python 코드에서 웹사이트로 리퀘스트 보내는 걸 할 수 있게 해줌. 웹 사이트 이동을 말함. 
        