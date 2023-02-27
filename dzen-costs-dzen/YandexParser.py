from config import *
import requests
from datetime import datetime, timedelta
import time


class Parser():
    def __init__(self, token, pubId):
        self.token = token
        self.pubId = pubId

    def get_campaigns_info(self, next_page):
        data = {
            "publisherId": self.pubId,
            "pageLimit": 200
        }
        if next_page:
            data["pageLastId"] = next_page
        headers = {
            'Authorization': f'Bearer {self.token}'
        }
        r = requests.get(info_url, data, headers=headers)

        campaigns = r.json()['campaigns']
        if 'pageLastId' in r.json().keys():
            next_page = r.json()['pageLastId']
        if 'hasNextPage' in r.json().keys():
            access = r.json()['hasNextPage']
        else:
            access = False

        return campaigns, next_page, access

    def create_report_by_campaigns_ids(self, url, campaigns_ids):
        data = {
            "publisherId": self.pubId,
            "campaignIds": campaigns_ids,
            "mskDateFrom": (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d'),
            "mskDateTo": (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')

        }
        headers = {
            'Authorization': f'Bearer {self.token}'
        }
        r = requests.post(url, json=data, headers=headers)
        while 'reportId' not in r.json().keys():
            time.sleep(5)
            print('Wait reportId')
            r = requests.post(url, json=data, headers=headers)
            print(r.json())
        return r.json()['reportId']

    def download_report_by_reportId(self, report_id):
        url = report_url.format(report_id)
        headers = {
            'Authorization': f'Bearer {self.token}'
        }
        while True:
            try:
                # print('Waiting report...')
                time.sleep(5)
                report = requests.get(url, headers=headers).json()
                # if 'detail' in report:
                #    print(report['detail'])
                report = report['statistics']
                break
            except KeyError:
                continue
            except Exception as s:
                print(s)
                exit()
        return report

    def easymo_publication_request(self, campaign_title, publication_id, publication_title, budget):
        text = (publication_title + '_' + publication_id)[:100]
        token = '3iwm2kamjan293r62nbasiqmUMNSau3msass83nsd93msihwn322nsdjd'
        data = {
            'access_token': token,
            'date': (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d'),
            'filter': {
                'utm_source': 'zen',
                'utm_campaign': campaign_title,
                'utm_content': text
            },
            'searchLike': {
                'utm_content': True
            },
            'costs': str(float(budget) * 1.05)
        }
        print(data)
        response = requests.post('http://easy-mo.ru/external/api/marketing/costs', json=data)
        print(response.json())
        return 1 if response.status_code == 200 else 0
