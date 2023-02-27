import time

import requests
token = 'y0_AgAAAABObGHQAAc7EgAAAADcacoMD6m9s7mwSbS93KPjur9ma5Dp_Tw'
header = {
    "Authorization": "Bearer " + token,
}
from datetime import datetime, timedelta
publisher_id = "603e385707d127033fa40efa"
compains_ids = []
compains_ids.append('63ee335365c1814a35458525')
reportUrls = {'1': 'https://promopages.yandex.ru/api/promo/v1/reports/campaigns-daily-stats',
              '2': 'https://promopages.yandex.ru/api/promo/v1/reports/campaigns-publications-daily-stats',
              '3': 'https://promopages.yandex.ru/api/promo/v1/reports/campaigns-previews-daily-stats'}
data = {
    "publisherId": publisher_id,
    "campaignIds": [compains_ids[0]],
    "mskDateFrom": (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d'),
    "mskDateTo": (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')}
# res = requests.post(reportUrls['3'], json=data, headers=header)
# reportId = res
# time.sleep(10)
# print(reportId.json()['reportId'])
res = requests.get(
    'https://promopages.yandex.ru/api/promo/v1/reports/{}?format=json'.format('63f33e4f99def05ccd672a74'),
    headers=header)
print('Отчёт')
print(res.content)