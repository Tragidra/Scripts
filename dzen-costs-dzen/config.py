create_publications_url = 'https://promopages.yandex.ru/api/promo/v1/reports/campaigns-publications-daily-stats'
create_previews_url = 'https://promopages.yandex.ru/api/promo/v1/reports/campaigns-previews-daily-stats'
create_campaigns_url = 'https://promopages.yandex.ru/api/promo/v1/reports/campaigns-daily-stats'

info_url = 'https://promopages.yandex.ru/api/promo/v1/campaigns'
report_url = 'https://promopages.yandex.ru/api/promo/v1/reports/{}?format=json'

publisher_ids = ['603e385707d127033fa40efa']
tokens = [
          'y0_AgAAAABXj1ydAAhkPgAAAADOJbHLrQtk8RWxTyONcIDJmuXdKyduEJM']  # y0_AgAAAABXj1ydAAhkPwAAAADOO_OCBIG7lnltQoCatOObzwj7hOIlgxk

data = list(zip(publisher_ids, tokens))
headers = {
    'Authorization': 'Bearer {}'
}

__all__ = ['create_publications_url',
           'create_previews_url',
           'create_campaigns_url',
           'info_url',
           'report_url',
           'data',
           'headers']
