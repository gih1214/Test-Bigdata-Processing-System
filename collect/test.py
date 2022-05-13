from cgitb import html
from turtle import title
from unittest import result
import requests
from datetime import datetime
from bs4 import BeautifulSoup


# aid 메서드 만들기 (숫자 -> 문자열)
def num_to_aid(num):
    num_str = str(num)
    return num_str.zfill(10)


# 메서드화 시키기
# dependency -> num_to_aid(int:num)
def naver_craw(num):
    result = {"title": "", "company": "국민일보", "createdAt": datetime.now()}

    response = requests.get(
        f"https://entertain.naver.com/read?oid=005&aid={num_to_aid(num)}")

    html = response.text
    html_bs = BeautifulSoup(html, "html.parser")

    # strip() : 양 옆의 공백을 다 제거해주는 메서드
    title = html_bs.select(".end_tit")[0].get_text().strip()
    # print(f"{company} {title} {createdAt}")

    result["title"] = title
    return result
