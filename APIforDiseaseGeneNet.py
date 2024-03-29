import requests
import json
import pandas as pd

class GetInformationFromDiseaseGeneNet:

    def __init__(self,account,password):
        self.database='DiseaseGeneNet'
        self.url='https://www.disgenet.org/api'
        self.resp_status_code = None
        self.response_gene = None
        self.disease_association_gene = None
        self.account = account
        self.password = password
        self.session = None

    def check_data_base_connection(self):
        session=requests.Session()
        try:
            response=session.post(self.url+'/auth/',data={'email':self.account,'password':self.password})
            if response.status_code == 200:
                json_response=response.json()
                self.api_key = json_response.get('token')
                self.session=session
            else:
                print(response.status_code)
                print(response.text)
        except requests.exceptions.RequestException as req_ex:
               print(req_ex)
        
    def get_gene_information(self,gene_of_interest):
        self.session.headers.update({"Authorization": "Bearer %s" % self.api_key})
        if gene_of_interest.__len__()!=1:
            seperation_pattern = '%2C'
            gene_pattern_in_url = seperation_pattern.join(gene_of_interest)
            url_to_take = self.url+'/gda/gene/'+gene_pattern_in_url
            response_gene = self.session.get(url_to_take,params={'source':'CURATED'})
            self.response_gene = response_gene
        else:
            gene_of_interest_x=gene_of_interest[0]
            url_to_take = self.url+'/gda/gene/'+gene_of_interest_x
            response_gene = self.session.get(url_to_take,params={'source':'CURATED'})
            self.response_gene = response_gene

    def disease_information(self,disease_of_interest):
        self.session.headers.update({"Authorization": "Bearer %s" % self.api_key})
        if disease_of_interest.__len__() != 1:
            diseases_for_url=['%20'.join(disease) for disease in disease_of_interest]
            seperation_pattern = '%2C'
            disease_pattern_in_url=seperation_pattern.join(diseases_for_url)
            url_to_take=self.url+'/gda/disease/'+disease_pattern_in_url
            response_disease = self.session.get(url_to_take,params={'source':'CURATED'})
        else:
            disease_for_url=['%20'.join(x.split()) for x in disease_of_interest]
            seperation_pattern = '%2C'
            disease_pattern_in_url=seperation_pattern.join(disease_for_url)
            url_to_take = self.url+'/gda/disease/'+disease_pattern_in_url
            print(url_to_take)
            response_disease = self.session.get(url_to_take,params={'source':'CURATED'})
        self.response_disease = response_disease


    def format_information_to_gene_and_disease_only(self):
        keys_of_interest = ('gene_symbol','disease_name')
        dictionary_from_json = self.response_gene.json()
        dataframe_disease_gene = pd.DataFrame.from_dict(dictionary_from_json)
        dataframe_disease_gene = dataframe_disease_gene.loc[:,keys_of_interest]
        type_interaction_disease = pd.DataFrame({'Type':['Gene-Disease' for x in range(dataframe_disease_gene.shape[0])]})
        dataframe_disease_gene.reset_index(drop=True, inplace=True)
        type_interaction_disease.reset_index(drop=True, inplace=True)
        disease_association_gene_df = pd.concat([dataframe_disease_gene,type_interaction_disease],axis=1)
        self.disease_association_gene = disease_association_gene_df
        self.session.close()