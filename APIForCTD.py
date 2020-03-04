import requests
import json
import pandas as pd


class GetInformationFromCtd:

    def __init__(self,database):
        self.database = database
        self.url = None
        self.resp_status_code = None
        self.parameters_for_query = None
        self.response = None
        self.report = None
        self.input_type = None
        self.input_terms = None
        self.url_to_retrieve = None
        self.format_to_report = None
        self.report_parameter = None
        self.filtered_output_json = None
        self.compound_association_gene = None
        self.compound_set_for_genes = None
        self.gene_set = None

    def set_url_for_request(self):
        if self.database == 'CTD':
            self.url = 'http://ctdbase.org/tools/batchQuery.go'
        resp = requests.get(self.url)
        if resp.status_code != 200:
            raise ApiErrpr('GET url'.format(resp.status_code))
        self.resp_status_code=resp.status_code

    def set_input_type(self,input_type=None):
        self.input_type=input_type

    def set_input_terms_for_ctd(self,input_terms=None):
        self.input_terms=input_terms

    def set_report_parameters(self,report_parameter,format_to_report):
        self.report_parameter = report_parameter
        self.format_to_report = format_to_report

    def get_information_from_database(self):
        self.url_to_retrieve = self.url + '?inputType=' + self.input_type + '&inputTerms=' + self.input_terms + '&report='+self.report_parameter+'&format='+self.format_to_report
        response=requests.get(self.url_to_retrieve)
        if response.status_code == 200:
            print('request is successful')
        self.response = response

    def filter_response_on_organism(self,organism_to_select):
        get_response_report=self.response.json()
        get_response_with_organism=[x for x in get_response_report if 'Organism' in x.keys()]
        response_report_filtered=[i for i in get_response_with_organism if i['Organism'] == organism_to_select]
        self.filtered_output_json=response_report_filtered


    def format_json_to_dataframe(self):
        keys_of_interest = ('ChemicalName','GeneSymbol')
        dictionary_from_json = self.filtered_output_json
        dataframe_compound_gene = pd.DataFrame.from_dict(dictionary_from_json)
        dataframe_compound_gene = dataframe_compound_gene.loc[:, keys_of_interest]
        self.compound_association_gene = dataframe_compound_gene

    def set_gene_set(self,genes_of_interest):
        self.gene_set=genes_of_interest

    def filter_only_interesting_genes(self):
        complete_compound_gene_set=self.compound_association_gene
        compound_set_for_genes=complete_compound_gene_set.loc[complete_compound_gene_set['GeneSymbol'].isin(self.gene_set)]
        type_interaction=pd.DataFrame({'Type':['Compound-Gene' for x in range(compound_set_for_genes.shape[1])]})
        compound_set_for_genes.reset_index(drop=True, inplace=True)
        type_interaction.reset_index(drop=True, inplace=True)
        compound_set_for_genes_df=pd.concat([compound_set_for_genes,type_interaction],axis=1)
        self.compound_set_for_genes=compound_set_for_genes_df