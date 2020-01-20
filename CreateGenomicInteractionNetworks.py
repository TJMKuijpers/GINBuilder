import pandas as pd
from APIforDiseaseGeneNet import GetInformationFromDiseaseGeneNet
from APIforHumanProteinAtlas import GetInformationFromHumanProteinAtlas
from APIForCTD import GetInformationFromCtd
from GetCpgToGeneConnections import GetCpgToGeneConnections
import networkx as nx
from APIforOmniPathDB import GetInformationFromOmniPathDB

class CreateGenomicInteractionNetwork:

    def __index__(self):
        self.class_of_network = 'GenomicInteractionNetwork'
        self.genes = None
        self.cpg_sites = None
        self.cpg_gene_interactions = None
        self.genomic_interaction_network = pd.DataFrame()
        self.cpg_gene_network = None
        self.genes_with_their_disease = None
        self.compound_gene_interactions_report = None
        self.network_data_frame = None
        self.gene_gene_molecular_interactions = None

    def set_genes_as_nodes(self,genes_for_network):
        self.genes = genes_for_network

    def set_cpg_sites_as_nodes(self,cpg_sites_for_network):
        self.cpg_sites = cpg_sites_for_network

    def set_compound_as_nodes(self,compounds_for_network):
        self.compound = compounds_for_network

    def get_compound_gene_interactions(self,genes_to_subset,input_type_compound,input_terms_compound,report_only_parameter,format_of_report):
        connection_to_ctd = GetInformationFromCtd('CTD')
        connection_to_ctd.set_url_for_request()
        connection_to_ctd.set_input_type(input_type=input_type_compound)
        connection_to_ctd.set_input_terms_for_ctd(input_terms=input_terms_compound)
        connection_to_ctd.set_report_parameters(report_parameter=report_only_parameter, format_to_report=format_of_report)
        connection_to_ctd.get_information_from_database()
        connection_to_ctd.filter_response_on_organism(organism_to_select='Homo sapiens')
        connection_to_ctd.format_json_to_dataframe()
        connection_to_ctd.set_gene_set(genes_to_subset)
        connection_to_ctd.filter_only_interesting_genes()
        self.compound_gene_interactions_report =connection_to_ctd.compound_set_for_genes

    def find_disease_associated_with_genes(self):
        connection_to_disgenenet = GetInformationFromDiseaseGeneNet()
        connection_to_disgenenet.get_gene_information(gene_of_interest = self.genes)
        connection_to_disgenenet.format_information_to_gene_and_disease_only()
        self.genes_with_their_disease = connection_to_disgenenet.disease_association_gene

    def find_genes_associated_with_disease(self):
        connect_to_disgenenet = GetInformationFromDiseaseGeneNet()
        connect_to_disgenenet.disease_information(disease_of_interest='C0002395')

    def get_gene_gene_interactions(self):
        gene_gene_interacts = GetInformationFromOmniPathDB()
        gene_gene_interacts.check_data_base_connection()
        gene_gene_interacts.set_search_for_interactions()
        gene_gene_interacts.set_type_of_gene_symbol()
        gene_gene_interacts.set_the_format('json')
        gene_gene_interacts.set_genes_to_search(self.genes)
        gene_gene_interacts.retrieve_molecular_interaction_network()
        gene_gene_interacts.convert_json_to_data_frame()
        self.gene_gene_molecular_interactions = gene_gene_interacts.results_df

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

    def set_column_names_on_data_frame(self,data_frame,column_names_to_set):
        data_frame.columns=column_names_to_set
        return data_frame

    def built_the_network(self):
        column_name_pattern=['Interactor A','Interactor B','Type']
        cpg_gene_data_frame=self.set_column_names_on_data_frame(self.cpg_gene_network,column_names_to_set=column_name_pattern)
        gene_compound_data_frame=self.set_column_names_on_data_frame(self.compound_gene_interactions_report,column_names_to_set=column_name_pattern)
        disease_gene_data_frame=self.set_column_names_on_data_frame(self.genes_with_their_disease,column_names_to_set=column_name_pattern)
        network_data_frame=pd.concat([cpg_gene_data_frame,disease_gene_data_frame,gene_compound_data_frame],axis=0)
        self.network_data_frame = network_data_frame

    def visualize_the_network(self):
        Graph=nx.from_pandas_edgelist(df=self.network_data_frame,source='Interactor A',target='Interactor B', edge_attr='Type')
        pos = nx.spring_layout(Graph)
        nx.draw(Graph)


test=CreateGenomicInteractionNetwork()
test.set_genes_as_nodes(genes_for_network=['ABCB5','VDAC3','RBL2','BRCA1','PGR'])
test.find_disease_associated_with_genes()
test.get_cpg_gene_interactions()
test.format_cpg_gene_interactions()
test.get_compound_gene_interactions(genes_to_subset=test.genes,input_type_compound='chem',input_terms_compound='C410127',report_only_parameter='genes_curated',format_of_report='json')
test.get_gene_gene_interactions()
test.built_the_network()
test.visualize_the_network()