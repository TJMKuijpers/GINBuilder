import requests
import json

class GetInformationFromDiseaseGeneNet:

    def __init__(self):
        self.database='DiseaseGeneNet'
        self.url='https://disgenet.org/api/gda/'
        self.resp_status_code = None

    def check_data_base_connection(self):
        resp = requests.get(self.url)
        if resp.status_code != 200:
            raise ApiErrpr('GET url'.format(resp.status_code))
        self.resp_status_code = resp.status_code

    def get_gene_information(self,gene_of_interest):
        if gene_of_interest.__len__()!=1:
            seperation_pattern = '%2C'
            gene_pattern_in_url = seperation_pattern.join(gene_of_interest)
            url_to_take = self.url+'gene/'+gene_pattern_in_url+'?source=CURATED'
            response_gene = requests.get(url_to_take)
            self.response_gene = response_gene
        else:
            url_to_take = self.url+'gene/'+gene_of_interest+'?source=CURATED'
            response_gene = requests.get(url_to_take)
            self.response_gene = response_gene

    def disease_information(self,disease_of_interest):
        if disease_of_interest.__len__() != 1:
            seperation_pattern = '%2C'
            disease_pattern_in_url=seperation_pattern.join(disease_of_interest)
            url_to_take=self.url+'disease/'+disease_pattern_in_url+'?source=CURATED'
            response_disease=requests.get(url_to_take)
        else:
            url_to_take=self.url+'disease/'+disease_of_interest+'?source=CURATED'
            response_disease=requests.get(url_to_take)
        self.response_disease=response_disease

