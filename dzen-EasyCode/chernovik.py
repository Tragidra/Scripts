import time

import requests
import pandas as pd
import json
from datetime import datetime, timedelta

from numpy import array

testurl = 'https://promopages.yandex.ru/api/promo/v1/campaigns'
reportUrls = {'1': 'https://promopages.yandex.ru/api/promo/v1/reports/campaigns-daily-stats',
              '2': 'https://promopages.yandex.ru/api/promo/v1/reports/campaigns-publications-daily-stats',
              '3': 'https://promopages.yandex.ru/api/promo/v1/reports/campaigns-previews-daily-stats'}
# Парметры к отчётам выше - https://yandex.ru/dev/promopages/doc/reference/post-reports.html
# token = 'y0_AgAAAABRVTuPAAklsAAAAADcZQMA09hVfL-lTW-AH3QDamAFT1uODdc' #Токен от приложения в кабинете Павел Койков
days = 30
HasNextPage = True


def get_compains(header, last=None):
    global HasNextPage, kk
    if last is None:
        data = {
            "publisherId": publisher_id,
            "pageLimit": 200,
            # "startFrom": '2022-10-01T00:00:00Z'
        }
    else:
        data = {
            "publisherId": publisher_id,
            "pageLimit": 200,
            "pageLastId": last
        }
    k = requests.get(testurl, data, headers=header)
    # if kk == 1000:
    #     print(k.json())
    campaigns = k.json()['campaigns']
    try:
        HasNextPage = k.json()['hasNextPage']
    except:
        HasNextPage = False
    try:
        nextPage = k.json()['pageLastId']
    except:
        nextPage = None
    print(nextPage)
    return campaigns, nextPage


compaims = None
last = None
publisher_id = "603e385707d127033fa40efa"
token = 'y0_AgAAAABObGHQAAc7EgAAAADcacoMD6m9s7mwSbS93KPjur9ma5Dp_Tw'
header = {
    "Authorization": "Bearer " + token,
}
kk = 0


def runPartCompams(compaims):
    global kk
    countCompainsWithoutKeys = 0
    kk = kk + len(compaims)
    all_compains_ids = []
    for i in range(len(compaims)):
        if 'isArchived' in compaims[i].keys():
            if not compaims[i]['isArchived']:
                print('Попал1')
                compains_ids = []
                compains_ids.append(compaims[i]['id'])
                time.sleep(2)
                data = {
                    "publisherId": publisher_id,
                    "campaignIds": [compains_ids[i]],
                    "mskDateFrom": (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d'),
                    "mskDateTo": (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')}
                res = requests.post(reportUrls['3'], json=data, headers=header)
                reportId = res
                time.sleep(10)
                print(reportId.json()['reportId'])
                res = requests.get(
                    'https://promopages.yandex.ru/api/promo/v1/reports/{}?format=json'.format(
                        reportId.json()['reportId']),
                    headers=header)
                print('Отчёт')
                print(res.content)
        else:
                compains_ids = []
                compains_ids.append(compaims[i]['id'])
                all_compains_ids.append(compaims[i]['id'])
                time.sleep(2)
                data = {
                    "publisherId": publisher_id,
                    "campaignIds": [compains_ids[0]],
                    "mskDateFrom": (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d'),
                    "mskDateTo": (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')}
                res = requests.post(reportUrls['3'], json=data, headers=header)
                reportId = res
                time.sleep(10)
                print(reportId.json()['reportId'])
                res = requests.get('https://promopages.yandex.ru/api/promo/v1/reports/{}?format=json'.format(
                    reportId.json()['reportId']), headers=header)
                # print('Отчёт')
                # print(res.content)
                print(all_compains_ids)
        # else:
        #     print('Упал в исключение по ключам')
        #     countCompainsWithoutKeys = countCompainsWithoutKeys + len(compaims[i])
        # if countCompainsWithoutKeys != 0:
        #     print(countCompainsWithoutKeys)


while HasNextPage:
    compaims, last = get_compains(header, last)
    runPartCompams(compaims)
    if last is None:
        print(kk)
        break
    print(kk)
