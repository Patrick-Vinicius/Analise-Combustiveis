#%%

import pandas as pd
# %%

# %%


tsv_file='dados.tsv'

# reading given tsv file
csv_table=pd.read_table(tsv_file,sep='\t')

# converting tsv file into csv
csv_table.to_csv('dados.csv',index=False)

# output
print("Successfully made csv file")
# %%

df = pd.read_csv("dados.csv")
df.shape
# %%
df.info()
# %%
