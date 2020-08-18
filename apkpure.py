'''
CREATED BY MUHAMMAD HANAN ASGHAR
PYTHONIST
'''
import requests
from bs4 import BeautifulSoup
import json
def APKPURE(app):
    JSON_DATA = []
    FINAL_LST = []
    id = 1
    SOUP = BeautifulSoup(requests.get(f'https://apkpure.com/search?q={app}').content,"html.parser")
    SEARCH_DATA = SOUP.findAll("dl")
    for i in SEARCH_DATA:
        LINK = "https://apkpure.com"+i.findAll("a")[0].get('href')+"/download?from=details"
        DOWNLOAD_LINK = BeautifulSoup(requests.get(LINK).content,"html.parser").findAll("a",{"id":"download_link"})[0].get('href')
        TITLE = i.findAll("p")[0].text
        IMAGE = i.findAll('img')[0].get('src')
        JSON_DATA = {
            "id": id,
            "Title": TITLE,
            "Image": IMAGE,
            "Download": DOWNLOAD_LINK
        }
        FINAL_LST.append(JSON_DATA)
        id += 1
    return FINAL_LST
