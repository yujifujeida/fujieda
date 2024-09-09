import pandas as pd
import numpy as np
from function import find_pxp

print(pd.__version__)

df = pd.read_excel('allgene.xlsx', index_col=None, header=1)

result_df = find_pxp.find_pxp(df)
print(result_df.info)
result_df.to_excel('result.xlsx')