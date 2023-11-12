import pandas as pd
import plotly.express as px
import preprocessamento

# Ler o arquivo
pluvio = pd.read_csv('pluvio_out.csv',
                        parse_dates=[0],
                        date_format='%d/%m/%Y-%H:%M:%S')


# Ajustar as datas e dividir o daaframe
pluvio_dia = pluvio.resample('1D', on='Data').sum()

pluvio_blumenau = pluvio_dia.iloc[:, -1:]
pluvio_estacoes = pluvio_dia.iloc[:, :-1]

# Construir os gráficos
figura1 = px.line(pluvio_blumenau)
figura1.update_layout(title='Índice pluviométrico de Blumenau',
                      yaxis_title='',
                      xaxis_title='',
                      template='plotly_dark',
                      showlegend=False)

figura2 = px.line(pluvio_estacoes)
figura2.update_layout(title='Índice pluviométrico por Estação',
                      yaxis_title='',
                      xaxis_title='',
                      template='plotly_dark')

# Ler o arquivo com tweets
tweets = pd.read_csv('tweets_out.csv',
                        parse_dates=[1],
                        date_format='%Y-%m-%d %H:%M:%S')

# Limpar e corrigir as datas
tweets.drop_duplicates(subset=['id'], inplace=True, keep='last')
tweets.reset_index(inplace=True, drop=True)

tweets['data'] = tweets['data'].dt.date

tweets['texto'] = tweets['texto'].apply(preprocessamento.text_cleaning)
tags = preprocessamento.tags

# Determinar os tweets por dia e construir o gráfico
tweets_dia = tweets.groupby('data')['texto'].apply(preprocessamento.conta_palavras, tags=tags)

figura3 = px.line(pluvio_blumenau)
figura3.add_bar(x=tweets_dia.index, y=tweets_dia.values, name='Tweets por dia')
figura3.update_layout(title='Incidência de tags nos tweets por dia',
                      yaxis_title='',
                      xaxis_title='',
                      template='plotly_dark')
figura3.update_legends(title='')

