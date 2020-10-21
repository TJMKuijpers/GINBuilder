import pandas as pd


class GetCpgToGeneConnections:

    def __init__(self):
        self.database_type = 'Affymetrix'
        self.cpg_database = None
        self.cpgs_connected_to_genes = None

    def load_cpg_database(self,path_to_database,separator=',',index_column=0):
        cpg_database = pd.read_csv(path_to_database,sep=separator,index_col=index_column)
        self.cpg_database = cpg_database

    def extract_cpg_associated_with_gene(self,column_name_gene = None, gene_of_interest = None):
        print(gene_of_interest)
        cpgs_connected_to_genes = self.cpg_database.loc[self.cpg_database[column_name_gene].isin(gene_of_interest)]
        self.cpgs_connected_to_genes = cpgs_connected_to_genes

    def add_node_for_gene(self,list_with_genes=None):
        cpg_sites=[]
        interaction_type=[]
        for x in list_with_genes:
            cpg_sites.append("CpG "+str(x))
            interaction_type.append("Gene-CpG")
        Gene_CPG_df=pd.DataFrame({"Genes":list_with_genes,"CpG":cpg_sites,"Type":interaction_type})
        self.cpgs_connected_to_genes=Gene_CPG_df
