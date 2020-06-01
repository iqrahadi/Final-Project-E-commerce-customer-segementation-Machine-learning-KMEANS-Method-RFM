import pandas as pd 

#data frame awal sudah terseleksi
def data_retail():
    df = pd.read_csv('RetailEngland.csv').head(20)
    return df
def data_retail2():
    df = pd.read_csv('RetailEngland.csv').tail(20)
    return df

#data frame yang sudah dilakukan groupby level customer dengan colomn RFM
def data_retail3():
    df = pd.read_csv('cleanIqra2.csv',usecols=[1,2,3,4]).head(20)
    return df


