import requests
import json
import pandas as pd

class GetInformationFromGeneMania:

    def __init__(self):
        self.database='DiseaseGeneNet'
        self.url='http://genemania.org/link?o=3702&g=PHYB%7CELF3%7CCOP1%7CSPA1%7CFUS9'
        self.resp_status_code = None
        self.response = None


    def check_data_base_connection(self):
        resp = requests.get(self.url)
        if resp.status_code != 200:
            raise ApiErrpr('GET url'.format(resp.status_code))
        self.resp_status_code = resp.status_code
        self.response=resp

test=GetInformationFromGeneMania()
test.check_data_base_connection()