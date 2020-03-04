import requests
import json

class GetInformationFromReactome:

    def __init__(self):
        self.database='Reactome'
        self.url_data_base_version='https://reactome.org/ContentService/data/database/version'
        self.response_data_base_version

    def get_data_base_version(self):
        resp = requests.get(self.url_data_base_version)
        if resp.status_code != 200:
            raise ApiErrpr('GET url'.format(resp.status_code))
        self.resp_status_code=resp.status_code
        self.response_data_base_version=resp



Reactome=GetInformationFromReactome()
Reactome.get_data_base_version()
print('Data base version is %d' % Reactome.response_data_base_version.text())
