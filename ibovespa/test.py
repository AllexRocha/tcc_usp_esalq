


def concatenar_parcial(df,ano):
    meses = df.columns[1:]
    dataframes = []
    for mes in meses:
        df_aux = df[mes]
        df_aux = df_aux.iloc[:-2]
        if mes in ['Abr', 'Jun', 'Set', 'Nov']:
            df_aux = df_aux.iloc[:-1]
        elif mes == 'Fev':
            if ano in [2012,2016,2020,2024]:
                df_aux = df_aux.iloc[:-2]
            else:
                df_aux = df_aux.iloc[:-3]

                
        if df_aux.isnull().all():
            break
        dataframes.append(df_aux)

    df_resultante = pd.concat(dataframes, ignore_index=True)
    return df_resultante

import pandas as pd
anos = 14
dataframe = []
for ano in range(2010,2010+anos+1):
    caminho_arquivo = f'{ano}.csv'

    df = pd.read_csv(caminho_arquivo, sep=';', decimal='.', header=1,encoding='latin-1')
    dataframe.append(concatenar_parcial(df,ano))
df_resultante = pd.concat(dataframe, ignore_index=True)


date_range = pd.date_range(start='2010-01-01', periods=len(df_resultante), freq='D')
df_resultante.index = date_range
df_resultante = df_resultante.iloc[:-30]

df = pd.DataFrame({'Último': df_resultante})
df['Último'] = df['Último'].str.replace(',', '')
df.dropna(subset=['Último'], inplace=True)
df['Último'] = df['Último'].astype(float)
df['Data'] = df.index