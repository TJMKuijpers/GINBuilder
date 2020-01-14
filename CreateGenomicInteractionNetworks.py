import pandas as pd
from APIforDiseaseGeneNet import GetInformationFromDiseaseGeneNet
from APIforHumanProteinAtlas import GetInformationFromHumanProteinAtlas
from APIForCTD import GetInformationFromCtd
from GetCpgToGeneConnections import GetCpgToGeneConnections

class CreateGenomicInteractionNetwork:

    def __index__(self):
        self.class_of_network = 'GenomicInteractionNetwork'
        self.genes = None
        self.cpg_sites = None
        self.cpg_gene_interactions = None
        self.genomic_interaction_network = pd.DataFrame()
        self.cpg_gene_network = None
        self.genes_with_their_disease = None

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
        connection_to_disgenenet.get_gene_information(gene_of_interest = self.genes)
        connection_to_disgenenet.format_information_to_gene_and_disease_only()
        self.genes_with_their_disease = connection_to_disgenenet.response_gene

    def find_genes_associated_with_disease(self):
        connect_to_disgenenet = GetInformationFromDiseaseGeneNet()
        connect_to_disgenenet.disease_information(disease_of_interest='C0002395')

    def get_gene_gene_interactions(self):
        print('undefined function')

    def get_cpg_gene_interactions(self):
        retrieve_cpg_genes = GetCpgToGeneConnections()
        path_to_database = 'E:\Project Envirogenomarkers\Data\Data for analysis\EGM_cpg_annotation.txt'
        retrieve_cpg_genes.load_cpg_database(path_to_database=path_to_database, separator='\t')
        retrieve_cpg_genes.extract_cpg_associated_with_gene(column_name_gene='UCSC_REFGENE_NAME',gene_of_interest=self.genes)
        self.cpg_gene_interactions = retrieve_cpg_genes.cpgs_connected_to_genes

    def format_gene_gene_interactions(self):
        print('undefined function')

    def format_cpg_gene_interactions(self):
        cpg_gene_network=self.cpg_gene_interactions.loc[:,['TargetID','UCSC_REFGENE_NAME','UCSC_REFGENE_GROUP']]
        self.cpg_gene_network=cpg_gene_network

test=CreateGenomicInteractionNetwork()
test.set_genes_as_nodes(genes_for_network=['ABCB5','VDAC3','RBL2'])
test.find_disease_associated_with_genes()
test.get_cpg_gene_interactions()
test.format_cpg_gene_interactions()