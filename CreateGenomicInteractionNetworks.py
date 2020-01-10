import pandas as pd
from APIforDiseaseGeneNet import GetInformationFromDiseaseGeneNet
from APIforHumanProteinAtlas import GetInformationFromHumanProteinAtlas
from APIForCTD import GetInformationFromCtd

class CreateGenomicInteractionNetwork:

    def __index__(self):
        self.class = 'GenomicInteractionNetwork'
        self.genes = None
        self.cpg_sites = None

    def set_genes_as_nodes(self,genes_for_network):
        self.genes = genes_for_network

    def set_cpg_sites_as_nodes(self,cpg_sites_for_network):
        self.cpg_sites = cpg_sites_for_network

    def set_compound_as_nodes(self,compounds_for_network):
        self.compound = compounds_for_network

    def get_compound_gene_interactions(self,input_type_compound,input_terms_compound,report_only_parameter,format_of_report):
        connection_to_ctd = GetInformationFromCtd('CTD')
        connection_to_ctd.set_url_for_request()
        connection_to_ctd.set_input_type(input_type=input_type_compound)
        connection_to_ctd.set_input_terms_for_ctd(input_terms=input_terms_compound)
        connection_to_ctd.set_report_parameters(report_parameter=report_only_parameter, format_to_report=format_of_report)
        print('CTD status code', CTD.resp_status_code)
        connection_to_ctd.get_information_from_database()
        connection_to_ctd.filter_response_on_organism(organism_to_select='Homo sapiens')

    def find_disease_associated_with_genes(self):
        connection_to_disgenenet = GetInformationFromDiseaseGeneNet()
        connection_to_disgenenet.get_gene_information(gene_of_interest='FASN')


    def find_genes_associated_with_disease(self):
        connect_to_disgenenet = GetInformationFromDiseaseGeneNet()
        connect_to_disgenenet.disease_information(disease_of_interest='C0002395')

    def get_gene_gene_interactions(self):

    def get_cpg_gene_interactions(self):
