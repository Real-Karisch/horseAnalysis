import numpy as np
import pandas as pd

def flagNew(df, flagColName, cols):
    dfCopy = df[cols].copy()
    dfCopy = pd.concat([pd.DataFrame([dfCopy.iloc[-1, :].copy()]), dfCopy])
    dfCopy = dfCopy.iloc[:-1, :]
    dfCopy.index = df.index

    df[flagColName] = pd.Series([False] * df.shape[0])
    for col in cols:
        df.loc[df[col] != dfCopy[col], flagColName] = True

    return df

def iterateFlagNew(df, flagColName, iterateColName):
    df[iterateColName] = pd.Series([0] * df.shape[0])
    indices = df[flagColName].copy()
    for i in range(1, 25):
        df.loc[indices & (df[iterateColName] == 0), iterateColName] = i
        indices = pd.concat([pd.Series(False), indices])
        indices = indices[:-1]
        indices.index = df.index

    df.drop(columns=[flagColName], inplace=True)
    
    return df