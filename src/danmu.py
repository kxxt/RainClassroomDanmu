import requests
from settings import danmu_api_url, site_url, UserAgent
import json


def get_csrf_token_from_cookies(cookie: str):
    start = cookie.find('csrftoken=')
    return cookie[start+len('csrftoken='):cookie[start:].find(';')]


def cookie_to_dict(cookies: str) -> dict:
    lines = cookies.split('; ')
    return {x.split('=')[0]: x.split('=')[1] for x in lines}


def send(cookies: str, lesson_id: str, presentation_id: str, msg: str, **kwargs) -> dict:

    csrf_token = get_csrf_token_from_cookies(cookies)
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7,en-GB;q=0.6,zh-TW;q=0.5',
        'Content-Type': 'application/json;charset=UTF-8',
        'Origin': site_url,
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'x-csrftoken': csrf_token
    }
    if 'ppt' in kwargs:
        headers['Referer'] = site_url + \
            f'/lesson/fullscreen/{lesson_id}/ppt/{kwargs["ppt"]}',
    data = {
        'lessonID': lesson_id,
        'presentationID': presentation_id,
        'message': msg
    }
    _cookies = cookie_to_dict(cookies)
    response = requests.post(
        danmu_api_url, cookies=_cookies, data=json.dumps(data))
    return response.json()
