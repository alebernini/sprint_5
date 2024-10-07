import pandas as pd

def dropar_na(df, coluna, limite_dados_faltantes):
    if df[coluna].isna().mean() > limite_dados_faltantes: 
        df = df.dropna_na(subset=[coluna])
    return df   

def limpar_outlier (df, coluna):
    Media = df[coluna].mean()    
    Desvio_Padrao = df[coluna].std()
    Limite_Superior = Media + 2*Desvio_Padrao
    Limite_Inferior = Media - 2*Desvio_Padrao
    df = df[(df[coluna] > Limite_Inferior) & (df[coluna] < Limite_Superior)]

    return df  
    

