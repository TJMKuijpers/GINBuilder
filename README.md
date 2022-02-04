# APIforInteractionNetworks

These files are used to create interaction networks between different node types including genes, CpG sites/islands, compound and diseases.
For the different nodes, different APIs can be used to extract information from online databases.

The python notebook can be used as a template to construct a genomic interactio network. Visualization of the network is possible with igraph althrough 
it is recommended to use a more advanced network visualization tool.

<h3> How to build a genomic interaction network? </h3>
First, you should import the libraries needed to create the interactions:<br>

```python
import pandas as pd
from CreateGenomicInteractionNetworks import CreateGenomicInteractionNetwork
from FilterGeneGeneInteractions import FilterGeneGeneInteractions
from mapTranscriptionFactors import mapTranscriptionFactors
```

Second, you have to import the gene symbols as input for the tool:

```python
path_to_gene_symbols=''  # write path here
gene_symbols=pd.read_csv(path_to_gene_symbols,sep=',')
```

It is important to note that the class CreateGenomicInteractionNetwork takes a list as input:

```python
gene_symbols = list(gene_symbols.genes)
```

To start, create an instance of the class object and set the genes as nodes. 

```python
interaction_network=CreateGenomicInteractionNetwork()
interaction_network.set_genes_as_nodes(genes_for_network=gene_symbols)
```

The CpG - gene interactions can be set from either a XXX or from a gene list. Basically, a gene list is a list containing the gene names for each CpG island/site. For example, the CpG island associated with the gene 'ABCA5' can be added by putting 'ABCA5' in the genelist.

```python
interaction_network.get_cpg_gene_interactions(option='FromGeneList',genelist=['PTPN14','TMEM51','TMEM51-AS1','RASAL2','CNN3','ARHGAP29','CRIM1-DT','ITGA9-AS1','MFAP3L','MRAS','RASAL2-AS1','SEPT10','SOWHAC','ZNF697','FAT1','LOC100506885','NFIB','PPIC','TMC7','ZNF205','CD276','CYFIP1','LRRC49','TJP1'])
```

Now you can add different kind of interactions: disease - gene interactions, gene - gene interactions, and transcription factor - gene interactions by using:

```python
interaction_network.find_disease_associated_with_genes()
interaction_network.get_gene_gene_interactions()
```

<h3>Software license </h3>
Software is licensed under BSD-2-clause.
