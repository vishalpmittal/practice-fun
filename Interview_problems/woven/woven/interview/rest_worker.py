import requests, json


class RESTWorker:

    def __init__(self):
        self.key = 'f7a10a51'
        self.URLBase = 'https://test.pulsra.com/api/v0/corp/onsite_interview/q1/' + self.key

    def get_all_emails_ids(self):
        r = requests.get(self.URLBase + '/all')
        return r.json()

    def get_email(self, email_id):
        r = requests.get(self.URLBase + '/' + email_id)
        return r.json()

    # def get_full_name(self, f_name):
    #     r = requests.get(self.URLBase + '/' + f_name)
    #     return '{} {}'.format(r.json()['first'], r.json()['last'])
