import pandas as pd
import plotly.express as px
import preprocessamento
import plotly.graph_objects as go

# Ler o arquivo
pluvio = pd.read_csv('pluvio_out.csv',
                        parse_dates=[0],
                        date_format='%d/%m/%Y-%H:%M:%S')

# Ajustar as datas e dividir o dataframe
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


prob_dia = pd.read_csv('probabilidade.csv', index_col=0)
graf1 = go.Bar(x=prob_dia.index, 
               y=prob_dia.values.flatten(),
               name='Probabilidade dos Tweets',
               yaxis='y1',
               opacity=0.5)

graf2 = go.Scatter(x=pluvio_blumenau.index,
                   y=pluvio_blumenau.values.flatten(),
                   name='Índice Pluviométrico',
                   yaxis='y2',
                   mode='lines+markers')

layout = go.Layout(title='Probabilidade de Tweets sobre Enchente',
                   yaxis1=dict(title='Probabilidade', side = 'left'),
                   yaxis2=dict(title='Índice Pluviométrico', side = 'right', overlaying='y', showgrid=False),
                   template='plotly_dark')

figura4 = go.Figure(data=[graf1, graf2], layout=layout)