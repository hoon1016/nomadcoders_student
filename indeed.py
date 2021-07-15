import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}"

def extract_indeed_pages():
  result = requests.get(URL)
  soup = BeautifulSoup(result.text,"html.parser")
  pagination = soup.find("div", {"class":"pagination"})

  links = pagination.find_all('a')
  pages = []

  for link in links[:-1]:
      pages.append(int(link.string))
  max_page = pages[-1]
  return max_page

def extract_indeed_jobs(last_pages):
  jobs = []
  for page in range(last_pages):
    result = requests.get(f"{URL}&start={page * LIMIT}")
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("h2", {"class": "jobTitle"})
    for h2_item in results:
      all_spans = h2_item.find_all("span")
      for span_item in all_spans:
        if span_item.get("title") is not None:
          print(span_item.get("title"))
          jobs.append(span_item.get("title"))
  return jobs

#1. 모든 a 태그 검색
#soup.find_all("a")
#soup("a")

#2. string 이 있는 title 태그 모두 검색
#soup.title.find_all(string=True)
#soup.title(string=True)

#3. a 태그를 두개만 가져옴
#soup.find_all("a", limit=2)

#4. string 검색
#soup.find_all(string="Elsie") # string 이 Elsie 인 것 찾기
#soup.find_all(string=["Tillie", "Elsie", "Lacie"]) # or 검색
#soup.find_all(string=re.compile("Dormouse")) # 정규식 이용

#5. p 태그와 속성 값이 title 이 있는거
#soup.find_all("p", "title")
#예)

#6. a태그와 b태그 찾기
#soup.find_all(["a", "b"])

#7. 속성 값 가져오기
#soup.p['class']
#soup.p['id']

#8. string을 다른 string으로 교체
#tag.string.replace_with("새로운 값")

#9. 보기 좋게 출력
#soup.b.prettify()

#10. 간단한 검색
#soup.body.b # body 태그 아래의 첫번째 b 태그
#soup.a # 첫번째 a 태그

#11. 속성 값 모두 출력
#tag.attrs

#12. class 는 파이썬에서 예약어이므로 class_ 로 쓴다.
#soup.find_all("a", class_="sister")

#13. find
#find()
#find_next()
#find_all()

#14. find 할 때 확인
#if soup.find("div", title=True) is not None:
#i = soup.find("div", title=True)

#15. data-로 시작하는 속성 find
#soup.find("div", attrs={"data-value": True})

#16. 태그명 얻기
#soup.find("div").name

#17. 속성 얻기
#soup.find("div")['class'] # 만약 속성 값이 없다면 에러
#soup.find("div").get('class') # 속성 값이 없다면 None 반환

#18. 속성이 있는지 확인
#tag.has_attr('class')
#tag.has_attr('id')
#있으면 True, 없으면 False

#19. 태그 삭제
#a_tag.img.unwrap()

#20. 태그 추가
#soup.p.string.wrap(soup.new_tag("b"))
#soup.p.wrap(soup.new_tag("div")
