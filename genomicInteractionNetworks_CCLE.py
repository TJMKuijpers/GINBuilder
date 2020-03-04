<<<<<<< HEAD
import pandas as pd
from CreateGenomicInteractionNetworks import CreateGenomicInteractionNetwork
from FilterGeneGeneInteractions import FilterGeneGeneInteractions
from mapTranscriptionFactors import mapTranscriptionFactors

path_to_gene_symbols="E:/CCLE manusscript/Data/Cluster results/Results used for paper/Network cluster 7  lymphoid neoplasms/Cytoscape network/GeneSymbolsForInteractionNetworkCluster7.txt"
gene_symbols=pd.read_csv(path_to_gene_symbols,sep='\t')
gene_symbols= gene_symbols.rename(columns={'Gene':'genes'})
gene_symbols=list(gene_symbols.genes)
cluster7_interaction_network=CreateGenomicInteractionNetwork()
cluster7_interaction_network.set_genes_as_nodes(genes_for_network=gene_symbols)
cluster7_interaction_network.get_cpg_gene_interactions(option='FromGeneList',genelist=['PTPN14','TMEM51','TMEM51-AS1','RASAL2','CNN3','ARHGAP29','CRIM1-DT','ITGA9-AS1','MFAP3L','MRAS','RASAL2-AS1','SEPT10','SOWHAC','ZNF697','FAT1','LOC100506885','NFIB','PPIC','TMC7','ZNF205','CD276','CYFIP1','LRRC49','TJP1'])
#cluster7_interaction_network.find_disease_associated_with_genes()
cluster7_interaction_network.get_gene_gene_interactions()

filtered_gene_gene_interactions = FilterGeneGeneInteractions()
filtered_gene_gene_interactions.set_gene_gene_information(cluster7_interaction_network.gene_gene_molecular_interactions)
filtered_gene_gene_interactions.set_nodes_to_include(cluster7_interaction_network.genes)
filtered_gene_gene_interactions.extract_nodes_from_network_df()

tf_interactions=mapTranscriptionFactors()
tf_interactions.read_transcription_library(path_to_tf='E:/GIT repos/NetworkSearchDatabase/transcription_catalogue.txt',separator='\t',encoding_arg='unicode_escape')
=======
import pandas as pd
from CreateGenomicInteractionNetworks import CreateGenomicInteractionNetwork
from FilterGeneGeneInteractions import FilterGeneGeneInteractions
from mapTranscriptionFactors import mapTranscriptionFactors

path_to_gene_symbols="E:/CCLE manusscript/Data/Cluster results/Results used for paper/Network cluster 7  lymphoid neoplasms/Cytoscape network/GeneSymbolsForInteractionNetworkCluster7.txt"
gene_symbols=pd.read_csv(path_to_gene_symbols,sep='\t')
gene_symbols= gene_symbols.rename(columns={'Gene':'genes'})
gene_symbols=list(gene_symbols.genes)
cluster7_interaction_network=CreateGenomicInteractionNetwork()
cluster7_interaction_network.set_genes_as_nodes(genes_for_network=gene_symbols)
cluster7_interaction_network.get_cpg_gene_interactions(option='FromGeneList',genelist=['PTPN14','TMEM51','TMEM51-AS1','RASAL2','CNN3','ARHGAP29','CRIM1-DT','ITGA9-AS1','MFAP3L','MRAS','RASAL2-AS1','SEPT10','SOWHAC','ZNF697','FAT1','LOC100506885','NFIB','PPIC','TMC7','ZNF205','CD276','CYFIP1','LRRC49','TJP1'])
#cluster7_interaction_network.find_disease_associated_with_genes()
cluster7_interaction_network.get_gene_gene_interactions()

filtered_gene_gene_interactions = FilterGeneGeneInteractions()
filtered_gene_gene_interactions.set_gene_gene_information(cluster7_interaction_network.gene_gene_molecular_interactions)
filtered_gene_gene_interactions.set_nodes_to_include(cluster7_interaction_network.genes)
filtered_gene_gene_interactions.extract_nodes_from_network_df()

tf_interactions=mapTranscriptionFactors()
tf_interactions.read_transcription_library(path_to_tf='E:/GIT repos/NetworkSearchDatabase/transcription_catalogue.txt',separator='\t',encoding_arg='unicode_escape')
>>>>>>> 4486222e1b75cf3d25bbf2025520078af836ac48
tf_interactions.get_tf_interactions_with_genes(gene_symbols)