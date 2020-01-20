import requests
import json
import pandas as pd

class GetInformationFromOmniPathDB:

    def __init__(self):
        self.database='DiseaseGeneNet'
        self.url='http://omnipathdb.org/'
        self.resp_status_code = None
        self.response = None
        self.genes_to_search = None
        self.search_results = None
        self.format = None
        self.results_df = None

    def check_data_base_connection(self):
        resp = requests.get(self.url)
        if resp.status_code != 200:
            raise ApiErrpr('GET url'.format(resp.status_code))
        self.resp_status_code = resp.status_code
        self.response=resp

    def set_the_data_base(self):
        print('undefined function')

    def set_search_for_interactions(self):
        self.url='http://omnipathdb.org/interactions/'

    def set_type_of_gene_symbol(self):
        self.gene_symbol='?genesymbols=1'

    def set_genes_to_search(self,genelist):
        genes_in_url=','.join(genelist)
        self.genes_to_search='&partners='+genes_in_url

    def set_the_format(self,format):
        self.format ='&format='+format

    def retrieve_molecular_interaction_network(self):
        url_for_omnipath = self.url+self.gene_symbol+self.genes_to_search+self.format
        print(url_for_omnipath)
        results_of_search = requests.get(url_for_omnipath)
        print(results_of_search)
        self.search_results = results_of_search

    def convert_json_to_data_frame(self):
        results_df_style = pd.DataFrame.from_dict(self.search_results.json())
        self.results_df = results_df_style

