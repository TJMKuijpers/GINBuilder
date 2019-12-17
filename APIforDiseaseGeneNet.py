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
        url_to_take=self.url+'gene/'+gene_of_interest+'?source=CURATED'
        response_gene=requests.get(url_to_take)
        self.response_gene=response_gene

    def disease_information(self,disease_of_interest):
        url_to_take=self.url+'disease/'+disease_of_interest+'?source=CURATED'
        response_disease=requests.get(url_to_take)
        self.response_disease=response_disease

DiseaseGeneNet=GetInformationFromDiseaseGeneNet()
DiseaseGeneNet.check_data_base_connection
DiseaseGeneNet.get_gene_information(gene_of_interest='FASN')
DiseaseGeneNet.disease_information(disease_of_interest='C0002395')