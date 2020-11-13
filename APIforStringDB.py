import requests
import json
import pandas as pd


class GetInformationFromStringDB:

    def __init__(self, genes=None):
        self.type_interactions = "PPI"
        self.url_to_database = "https://string-db.org/api/json/network"
        self.genes = genes
        self.response = None
        self.params = None
        self.ppi = None

    def check_data_base_connection(self):
        resp = requests.get(self.url)
        if resp.status_code != 200:
            raise ApiErrpr('GET url'.format(resp.status_code))
        self.resp_status_code = resp.status_code
        self.response = resp

    def set_parameters(self):
        self.params = {"identifiers": "%0d".join(self.genes), "species": 9606}

    def get_protein_protein_interactions(self):
        response = requests.post(self.url_to_database, self.params)
        ppi_df = pd.DataFrame.from_dict(response.json())
        ppi_df = ppi_df.loc[ppi_df.score > 0.7, :]
        ppis = ppi_df.loc[:, ['preferredName_A', 'preferredName_B']]
        self.ppi = ppis
