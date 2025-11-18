import pandas as pd
import plotly.offline as py
import plotly.graph_objs as go

#py.init_notebook_mode(connected=False)

df = pd.read_csv(r'C:\Users\vincy\Google Drive\Alura\7 Days of Code\Ciencia de Dados\despesa_ceaps_2.csv')
print(df.head())

print('Esse dataset contém {} linhas'.format(df.shape[0]))

trace = go.Scatter(x = df['ANO'],
                   y = df['VALOR_REEMBOLSADO'],
                   mode = 'markers')

data = [trace]

py.plot(data)