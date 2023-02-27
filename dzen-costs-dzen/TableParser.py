import pandas as pd

from config import create_publications_url, create_previews_url, create_campaigns_url

def previews_iterator(data, ignore_archived_campaigns=True, ignore_deleted_previews=True):
    for page in data:
        for campaign in page:
            campaign_id = campaign['id']
            campaign_title = campaign['title']
            if 'isArchived' in campaign.keys():
                campaign_is_archived = bool(campaign['isArchived'])
            else:
                campaign_is_archived = False
            if ignore_archived_campaigns:
                if not campaign_is_archived:
                    campaign_active = True
                else:
                    campaign_active = False
            else:
                campaign_active = True
            if campaign_active:
                for publication in campaign['publications']:
                    publication_id = publication['id']
                    for preview in publication['previews']:
                        preview_id = preview['id']
                        preview_title = preview['title']
                        if 'isDeleted' in preview.keys():
                            preview_is_deleted = bool(preview['isDeleted'])
                        else:
                            preview_is_deleted = False
                        if ignore_deleted_previews:
                            if preview_is_deleted:
                                preview_active = False
                            else:
                                preview_active = True
                        else:
                            preview_active = True

                        if preview_active:
                            yield campaign_id, campaign_title, publication_id, preview_id, preview_title


def campaigns_iterator(data, ignore_archived_campaigns=True):
    for page in data:
        for campaign in page:
            campaign_id = campaign['id']
            campaign_title = campaign['title']
            if 'isArchived' in campaign.keys():
                campaign_is_archived = bool(campaign['isArchived'])
            else:
                campaign_is_archived = False
            if ignore_archived_campaigns:
                if not campaign_is_archived:
                    campaign_active = True
                else:
                    campaign_active = False
            else:
                campaign_active = True
            if campaign_active:
                yield campaign_id, campaign_title


def publications_iterator(data, ignore_archived_campaigns=True):
    for page in data:
        for campaign in page:
            campaign_id = campaign['id']
            campaign_title = campaign['title']
            if 'isArchived' in campaign.keys():
                campaign_is_archived = bool(campaign['isArchived'])
            else:
                campaign_is_archived = False
            if ignore_archived_campaigns:
                if not campaign_is_archived:
                    campaign_active = True
                else:
                    campaign_active = False
            else:
                campaign_active = True
            if campaign_active:
                for publication in campaign['publications']:
                    publication_id = publication['id']
                    if len(publication['previews']):
                        publication_title = publication['previews'][-1]['title']
                    else:
                        publication_title = 'Публикация без обложек'
                    yield campaign_id, campaign_title, publication_id, publication_title


def get_campaigns_ids(data, ignore_archived_campaigns=True):
    for page in data:
        for campaign in page:
            campaign_id = campaign['id']
            campaign_title = campaign['title']
            if 'isArchived' in campaign.keys():
                campaign_is_archived = bool(campaign['isArchived'])
            else:
                campaign_is_archived = False
            if ignore_archived_campaigns:
                if not campaign_is_archived:
                    campaign_active = True
                else:
                    campaign_active = False
            else:
                campaign_active = True
            if campaign_active:
                yield campaign_id


class Matcher():
    def __init__(self):
        self.arr = {}

    def get_element(self, key):
        if key in self.arr.keys():
            value = self.arr[key]
            del self.arr[key]
            return True, value
        else:
            return False, None

    def add_element(self, key, value):
        if key in self.arr:
            # print(f'key: {key} Old value: {self.arr[key]} New value: {value}')
            self.arr[key] += value
        self.arr[key] = value


def batcher(iterator, batch_size=200):
    current_campaigns = []
    for campaign in iterator:
        current_campaigns.append(campaign)
        if len(current_campaigns) == batch_size:
            yield current_campaigns
            current_campaigns = []
    if len(current_campaigns) != 0:
        yield current_campaigns


def create_campaigns_report(arr, parse):
    for batch in batcher(get_campaigns_ids(arr, False)):
        report_id = parse.create_report_by_campaigns_ids(create_campaigns_url, batch)
        report = parse.download_report_by_reportId(report_id)
        matcher = Matcher()

        for campaign_id, campaign_title in campaigns_iterator(arr, False):
            access, campaign_budget = matcher.get_element(campaign_id)
            while not access:
                if len(report) != 0:
                    campaign_id_, campaign_budget_ = report[0]['campaignId'], report[0]['budget']
                    matcher.add_element(campaign_id_, campaign_budget_)
                    del report[0]
                    access, campaign_budget = matcher.get_element(campaign_id)
                else:
                    access = False
                    break
            if access:
                yield campaign_id, campaign_title, campaign_budget


def create_previews_report(arr, parse):
    for batch in batcher(get_campaigns_ids(arr, False)):
        report_id = parse.create_report_by_campaigns_ids(create_previews_url, batch)
        report = parse.download_report_by_reportId(report_id)
        matcher = Matcher()

        for campaign_id, campaign_title, publication_id, preview_id, preview_title in previews_iterator(arr, False):
            access, preview_budget = matcher.get_element(campaign_id + '_' + publication_id + '_' + preview_id)
            while not access:
                if len(report) != 0:
                    campaign_id_, publication_id_, preview_id_, preview_budget_ = report[0]['campaignId'], report[0][
                        'publicationId'], report[0]['previewId'], report[0]['budget']
                    matcher.add_element(campaign_id_ + '_' + publication_id_ + '_' + preview_id_, preview_budget_)
                    del report[0]
                    access, preview_budget = matcher.get_element(campaign_id + '_' + publication_id + '_' + preview_id)
                else:
                    access = False
                    break
            if access:
                yield campaign_id, campaign_title, publication_id, preview_id, preview_title, preview_budget


def create_publications_report(arr, parse):
    for batch in batcher(get_campaigns_ids(arr, False)):
        report_id = parse.create_report_by_campaigns_ids(create_publications_url, batch)
        report = parse.download_report_by_reportId(report_id)
        matcher = Matcher()

        for campaign_id, campaign_title, publication_id, publication_title in publications_iterator(arr, False):
            access, publication_budget = matcher.get_element(campaign_id + '_' + publication_id)
            while not access:
                if len(report) != 0:

                    campaign_id_, publication_id_, publication_budget_ = report[0]['campaignId'], report[0][
                        'publicationId'], report[0]['budget']
                    matcher.add_element(campaign_id_ + '_' + publication_id_, publication_budget_)
                    del report[0]
                    access, publication_budget = matcher.get_element(campaign_id + '_' + publication_id)
                else:
                    access = False
                    break
            if access:
                yield campaign_id, campaign_title, publication_id, publication_title, publication_budget


def iterator_to_dataframe(iterator):
    arr = []
    for line in iterator:
        arr.append(line)
    return pd.DataFrame(arr)