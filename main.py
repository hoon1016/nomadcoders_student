from indeed import extract_indeed_pages,extract_indeed_jobs

last_indeed_page = extract_indeed_pages()

extract_indeed_jobs(last_indeed_page)



#순서요약
#1) 모듈설치
#2) 가져올 페이지의 url요청 (get .text)
#3) 원하는 html 파트 가져오기 (Beautiful Soup)
#4) pagination 찾기
#5-1) pagination 안의 모든 앵커 찾기
#5-2) loop를 이용해 각 페이지의 "span" 모두 찾기
#6) 불러올 페이지 넘버 지정해주기

#1. Import Packages (모듈설치)
#-영상에서 쓰인 모듈 :
#ㄴRequest (사이트 정보 가져오기 (text))
#ㄴBeautiful Soup (html 내 필요한 부분 추출하기 (html))

#2. 가져올 페이지의 url요청 (request.get)
#-페이지.text 가져왕

#3. 원하는 html 파트 가져오기 (Beautiful Soup)
#-위 .text에서 HTML 불러왕 (html.parser)

#4. HTML 내에서 내가 원하는 정보의 pagination(페이지 네비게이터)을 찾기(indeed_soup.find)
#ㄴ"div" 를 찾아서 "pagination" 클래스 불러와줭

#5-1. pagination 안의 모든 앵커('a href' 형태로 되어있는 링크들) 찾아주기
#ㄴpagination.find_all('a'))

#5-2. 페이지 링크마다 있는 태그를 각각 모두 불러와줘야 하므로 loop(for-in) 사용
#ㄴfor link in links: pages.append(link.find("span"))


#6. 어디서부터 어디까지 불러올건지 페이지 넘버 지정해주기
#ㄴpages = pages[0:-1]
