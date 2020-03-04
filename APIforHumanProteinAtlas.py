import requests
import json

class GetInformationFromHumanProteinAtlas:

    def __init__(self):
        self.database='HumanProteinAtlas'
        self.url='http://www.proteinatlas.org/api/search_download.php'
        self.resp_status_code = None
        self.gene_of_interest = None
        self.columns_of_interest = None
        self.url_for_columns_of_interest = None
        self.url_for_format = None
        self.url_for_compression = None
        self.url_for_gene = None
        self.response_HPA_search = None
        self.gene_list = None
        self.response_HPA_multiple_genes = None
        self.url_for_gene_list = None
        self.url_to_take_gene_list = None

    def check_data_base_connection(self):
        resp = requests.get(self.url)
        if resp.status_code != 200:
            raise ApiErrpr('GET url'.format(resp.status_code))
        self.resp_status_code = resp.status_code

    def set_gene_of_interest(self,gene):
        self.gene_of_interest = gene
        self.url_for_gene='?search='+gene

    def set_columns_of_interest(self,columns_of_interest):
        self.columns_of_interest=columns_of_interest
        columns_of_interest_string=','.join(columns_of_interest)
        self.url_for_columns_of_interest='&columns='+columns_of_interest_string

    def set_format_and_compression(self,format='json',compression='no'):
        self.url_for_format='&format='+format
        self.url_for_compression='&compress='+compression

    def search_data_base_for_gene(self):
        url_to_take=self.url+self.url_for_gene+self.url_for_format+self.url_for_columns_of_interest+self.url_for_compression
        response_HPA=requests.get(url_to_take)
        self.response_HPA_search = response_HPA

    def set_gene_list_to_search(self,gene_list):
        self.gene_list=gene_list

    def search_gene_list_of_interest(self):
        genes_of_interest=','.join(map(str,self.gene_list ))
        self.url_for_gene_list='?search='+genes_of_interest
        url_to_take_gene_list=self.url+self.url_for_gene_list+self.url_for_format+self.url_for_columns_of_interest+self.url_for_compression
        response_HPA_multiple_genes=requests.get(url_to_take_gene_list)
        self.url_to_take_gene_list = url_to_take_gene_list
        self.response_HPA_multiple_genes = response_HPA_multiple_genes

GeneSearchABCB5=GetInformationFromHumanProteinAtlas()
GeneSearchABCB5.set_gene_of_interest('ENSG00000004846')
GeneSearchABCB5.set_columns_of_interest(['g','gs','rnats','rnatsm','rnaclsm','rnacas','rnacass','rnacad'])
GeneSearchABCB5.set_format_and_compression()
GeneSearchABCB5.search_data_base_for_gene()
GeneSearch_list=GetInformationFromHumanProteinAtlas()
GeneSearch_list.set_gene_list_to_search(['ENSG00000169710','ENSG00000004846','ENSG00000141510','ENSG00000164362'])
GeneSearch_list.set_format_and_compression()
GeneSearch_list.set_columns_of_interest(['g','gs','rnats','rnatsm','rnaclsm','rnacas','rnacass','rnacad'])
GeneSearch_list.search_gene_list_of_interest()
