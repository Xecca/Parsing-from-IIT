import requests
from bs4 import BeautifulSoup as BS
from keys import *  # Login and password are stored here

s = requests.Session()

# get logintoken
auth_html = s.get("https://eu.iit.csu.ru/login/index.php")
auth_bs = BS(auth_html.content, "html.parser")
loginToken = auth_bs.select("input[name=logintoken]")[0]['value']

# print(loginToken)

# do login
payload = {
    "anchor": '',
    "logintoken": loginToken,
    "username": login,      #from file keys.py
    "password": password,   #from file keys.py
    "rememberusername": 1
}

answ = s.post("https://eu.iit.csu.ru/login/index.php", data = payload)
answ_bs = BS(answ.content, "html.parser")

print( "Уррра! Я вошел в: {}\n ".format(
    answ_bs.select(".page-header-headings")[0].text.strip()
) )

# get my grade from grade book
grade_html = s.get("https://eu.iit.csu.ru/grade/report/overview/index.php")
grade_bs = BS(grade_html.content, "html.parser")

courses = {}    # save parsed data here

# string = ("#grade-report-overview-5907_r{}".format(index))
studentName = grade_bs.select("#page-header > div > div > div > div.d-sm-flex.align-items-center > div.mr-auto > div > div.page-header-headings > h1")[0].text.strip()

print("Имя студента: {}\n".format(
    studentName
))

index = 0

for course in grade_bs.select("tbody > tr"):
    string = ('#grade-report-overview-5907_r{}_c0'.format(index))
    courseTitle = (course.select(str(string + ' > a')))[0].text
    courseGrade = (course.select('tr > .c1'))[0].text
    print(courseTitle + '\t' + courseGrade)
    courses[courseTitle] = courseGrade
    index += 1
    print(" ------------------------------------------------------- ")

# print(courses)