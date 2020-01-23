import pandas as pd


class FilterGeneGeneInteractions:

    def __init__(self):
        self.type = 'NetworkStructure'
        self.network= None
        self.intermediate_nodes_allowed = False
        self.nodes = None
        self.network_filtered = None

    def set_gene_gene_information(self,network):
        self.network = network

    def set_nodes_to_include(self,node_list):
        self.nodes = node_list

    def set_intermediate_nodes_allowed(self,intermediate=False):
        print('check')
        if intermediate:
            self.intermediate_nodes_allowed = True

    def extract_nodes_from_network_df(self):
        if self.intermediate_nodes_allowed:
            print('intermediate nodes are allowed')
        else:
            # intermediate nodes are not allowed therefore source and target should be in gene list
            filtered_network_source_nodes_filtered=self.network.loc[self.network['source_genesymbol'].isin(self.nodes),:]
            filtered_network_target_nodes_filtered=filtered_network_source_nodes_filtered.loc[filtered_network_source_nodes_filtered['target_genesymbol'].isin(self.nodes),:]
            self.network_filtered = filtered_network_target_nodes_filtered