import time

import requests
import pandas as pd
import json
from datetime import datetime, timedelta

from numpy import array

testurl = 'https://promopages.yandex.ru/api/promo/v1/campaigns'
reportUrls = {'1':'https://promopages.yandex.ru/api/promo/v1/reports/campaigns-daily-stats', '2':'https://promopages.yandex.ru/api/promo/v1/reports/campaigns-publications-daily-stats', '3':'https://promopages.yandex.ru/api/promo/v1/reports/campaigns-previews-daily-stats'}
# Парметры к отчётам выше - https://yandex.ru/dev/promopages/doc/reference/post-reports.html
# token = 'y0_AgAAAABRVTuPAAklsAAAAADcZQMA09hVfL-lTW-AH3QDamAFT1uODdc' #Токен от приложения в кабинете Павел Койков
token = 'y0_AgAAAABQYAIQAAkmLAAAAADcZaERkd_aKyc_QFamkpCbL4v-KEBgipc' #Дзен где только один канал EasyCode
header = {
    "Authorization": "Bearer " + token,
}
days = 30
def get_compains(header):
    data = {
        "publisherId": publisher_id,
        "pageLimit": 200,
    }
    k = requests.get(testurl, data, headers=header)
    campaigns = k.json()['campaigns']
    return campaigns

compains_ids = []
publisher_id = "606c2c41d47eba36e1f5cc2c"
token = 'y0_AgAAAABQYAIQAAkmLAAAAADcZaERkd_aKyc_QFamkpCbL4v-KEBgipc'

compaims = get_compains(header)
for i in range(len(compaims)):
    compains_ids.append(compaims[i]['id'])
    time.sleep(2)
    data = {
        "publisherId": publisher_id,
        "campaignIds": [compains_ids[i]],
        "mskDateFrom": (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d'),
        "mskDateTo": (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')}
    res = requests.post(reportUrls['2'], json=data, headers=header)
    reportId = res
    time.sleep(10)
    print(reportId.json()['reportId'])
    res = requests.get('https://promopages.yandex.ru/api/promo/v1/reports/{}?format=json'.format(reportId.json()['reportId']), headers=header)
    print(res.content)
