import dash
from dash import dcc, html
import plotly.express as px
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import pandas as pd
import yfinance as yf

# Leitura e ajuste dos dados

# acoes_b3 = ['PETR4.SA', #petrobras
#             'VALE3.SA', #vale
#             'ITUB4.SA', #itau
#             'BBDC4.SA', #bradesco
#             'ABEV3.SA', #ambev
#             'B3SA3.SA', #b3
#             'MRFG3.SA', #marfrig
#             'WEGE3.SA', #weg
#             'SUZB3.SA', #suzano
#             'VIVT3.SA', #vivo
#             '^BVSP'] #ibovespa
# df = yf.download(acoes_b3, period='1y')
# df.index.name = None
# df.to_csv('b3.csv')

data = pd.read_csv('b3.csv', index_col=0)

# Construção dos gráficos
data2 = data['VALE3.SA']
fig2 = px.line(data2)
fig2.update_layout(title='VALE3.SA 10+',
                   yaxis_title='Preço (R$)',
                   xaxis_title='Data',
                   template='plotly_dark',
                   showlegend=False)

data3 = data['ITUB4.SA']
fig3 = px.line(data3)
fig3.update_layout(title='ITUB4.SA 10+',
                   yaxis_title='Preço (R$)',
                   xaxis_title='Data',
                   template='plotly_dark',
                   showlegend=False)

data4 = pd.read_csv('petro.csv', index_col=0)
candle = go.Candlestick(x=data4.index,
                        open=data4['Open'],
                        high=data4['High'],
                        low=data4['Low'],
                        close=data4['Close'])
fig4 = go.Figure(data=[candle])
fig4.update_layout(title='PETR4.SA 10+',
                    yaxis_title='Preço (R$)',
                    xaxis_title='Data',
                    template='plotly_dark')

# Inicialização da aplicação

app = dash.Dash(__name__, 
                external_stylesheets=[dbc.themes.CYBORG])

#Layout do dashboard

app.layout = dbc.Container([

    dbc.Row([ #Primeira linha
        dbc.Col([
            html.H1('Dashboard do Mercado Financeiro',
                    className= 'text-center text-primary'),
            html.Br()
        ])
    ]),

    dbc.Row([ #Segunda linha
        dbc.Col([

            dcc.Dropdown(id='menu', value=['ABEV3.SA'],
                         options={x:x for x in data.columns},
                         multi=True),
            dcc.Graph(id='grafico')
        ])
    ]),

    dbc.Row([ #Terceira linha
        dbc.Col([ #Primeira coluna
            dcc.Graph(figure=fig2)
        ], width=4),
        dbc.Col([ #Segunda coluna
            dcc.Graph(figure=fig3)
        ], width={'size': 8})
    ], class_name='g-0'),

    dbc.Row([ #Quarta linha
        dbc.Col([
            dcc.Graph(figure=fig4)
        ])
    ])
])

# Callbacks
@app.callback(
    Output('grafico', 'figure'),
    Input('menu', 'value')
)

def funcao(acoes):
    data_fig = data[acoes]
    fig = px.line(data_fig)
    fig.update_layout(title='B3 10+',
                        yaxis_title='Preço (R$)',
                        xaxis_title='Data',
                        template='plotly_dark',
                        showlegend=False)  #plotly.com/python/templates/
    return fig

# Execução do aplicação
if __name__ == '__main__':
    app.run_server(debug=True)