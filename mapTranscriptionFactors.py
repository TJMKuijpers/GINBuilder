<<<<<<< HEAD
import pandas as pd

class mapTranscriptionFactors:

    def __init__(self):
        self.type='transcription regulation'
        self.tf_library = None
        self.tf_interactions = None

    def read_transcription_library(self,path_to_tf,separator,encoding_arg):
        tf_library=pd.read_csv(path_to_tf,sep=separator,encoding=encoding_arg)
        self.tf_library=tf_library

    def get_tf_interactions_with_genes(self,genes):
        tf_step_source_subset=self.tf_library.loc[self.tf_library.TF.isin(genes),:]
        print(tf_step_source_subset)
        tf_step_target_subset=tf_step_source_subset.loc[tf_step_source_subset.target_gene.isin(genes),:]
        self.tf_interactions=tf_step_target_subset
=======
import pandas as pd

class mapTranscriptionFactors:

    def __init__(self):
        self.type='transcription regulation'
        self.tf_library = None
        self.tf_interactions = None

    def read_transcription_library(self,path_to_tf,separator,encoding_arg):
        tf_library=pd.read_csv(path_to_tf,sep=separator,encoding=encoding_arg)
        self.tf_library=tf_library

    def get_tf_interactions_with_genes(self,genes):
        tf_step_source_subset=self.tf_library.loc[self.tf_library.TF.isin(genes),:]
        print(tf_step_source_subset)
        tf_step_target_subset=tf_step_source_subset.loc[tf_step_source_subset.target_gene.isin(genes),:]
        self.tf_interactions=tf_step_target_subset
>>>>>>> 4486222e1b75cf3d25bbf2025520078af836ac48
