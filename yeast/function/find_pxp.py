import pandas as pd
import re

# return if PxP sequence exist
def is_include_pxp(sequence):
    pattern = '[AVLIPFC]..[AVLIPFC]PP.P[AVLIPFCT].[AVLIPFC]'
    result = re.search(pattern, sequence)
    if result:
        return True
    else:
        return False

# return processed df
def find_pxp(df):

    drop_list = []

    for row in df.itertuples():
        sequence = row.sequence
        
        if not is_include_pxp(sequence):
            drop_list.append(row.Index)

    df = df.drop(drop_list)
    return df
