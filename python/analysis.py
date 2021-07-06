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

horsedtype = {
    'track': 'string',
    'date': 'string',
    'race': 'int',
    'horseProgram': 'string',
    'horseName': 'string',
    'lastRaceDay': 'float', #check
    'lastRaceMonth': 'string',
    'lastRaceYear': 'float',
    'lastRaceTrack': 'string',
    'jockey': 'string',
    'weight': 'int',
    'ME': 'string',
    'placePP': 'float',
    'placeSeg1': 'float',
    'placeSeg2': 'float',
    'placeSeg3': 'float',
    'placeSeg4': 'float',
    'placeSeg5': 'float',
    'placeSeg6': 'float',
    'odds': 'float',
    'comments': 'string',
    'lastRaceNum': 'float',
    'lastRacePlace': 'float',
    'lengthsSeg1': 'float',
    'lengthsSeg2': 'float',
    'lengthsSeg3': 'float',
    'lengthsSeg4': 'float',
    'lengthsSeg5': 'float',
    'lengthsSeg6': 'float',
    'rlLengthsSeg1': 'float',
    'rlLengthsSeg2': 'float',
    'rlLengthsSeg3': 'float',
    'rlLengthsSeg4': 'float',
    'rlLengthsSeg5': 'float',
    'rlLengthsSeg6': 'float',
    'rlPlaceSeg1': 'float',
    'rlPlaceSeg2': 'float',
    'rlPlaceSeg3': 'float',
    'rlPlaceSeg4': 'float',
    'rlPlaceSeg5': 'float',
    'rlPlaceSeg6': 'float',
    'trainer': 'string',
    'owner': 'string',
}
racedtype = {
    'track': 'string',
    'date': 'string',
    'race': 'int',
    'stakes': 'string',
    'distanceStr': 'string',
    'distance': 'float',
    'surface': 'string',
    'weather': 'string',
    'conditions': 'string',
    'startTime': 'string',
    'startNote': 'string',
    'segment1': 'string',
    'segment2': 'string',
    'segment3': 'string',
    'segment4': 'string',
    'segment5': 'string',
    'segments': 'int',
    'fracTime1': 'float',
    'fracTime2': 'float',
    'fracTime3': 'float',
    'fracTime4': 'float',
    'fracTime5': 'float',
    'finalTime': 'float',
    'runup': 'int',
    'wpsPool': 'float',
    'firstPlaceWin': 'float',
    'firstPlacePlace': 'float',
    'firstPlaceShow': 'float',
    'secondPlacePlace': 'float',
    'secondPlaceShow': 'float',
    'thirdPlaceShow': 'float',
    'exactaBuyin': 'string',
    'exactaFinish': 'string',
    'exactaPayout': 'float',
    'exactaPool': 'float',
    'trifectaBuyin': 'string',
    'trifectaFinish': 'string',
    'trifectaPayout': 'float',
    'trifectaPool': 'float',
}