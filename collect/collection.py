from pymongo import MongoClient
import requests
from datetime import datetime
from bs4 import BeautifulSoup

# 몽고DB 접속
mongo = MongoClient("localhost", 20000)


# aid 만드는 함수
def num_to_aid(num, size=10):
    num_str = str(num)
    return num_str.zfill(size)


# naver_craw 함수
def naver_craw(num):
    result = {"title": "", "company": "국민일보", "createdAt": datetime.now()}

    response = requests.get(
        f"https://entertain.naver.com/read?oid=005&aid={num_to_aid(num)}")

    html = response.text
    html_bs = BeautifulSoup(html, "html.parser")

    title = html_bs.select(".end_tit")[0].get_text().strip()

    result["title"] = title
    return result


# save 함수
def mongo_save(mongo, datas, db_name=None, collection_name=None):
    result = mongo[db_name][collection_name].insert_many(datas).inserted_ids
    return result
