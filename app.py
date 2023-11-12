import dash
from dash import dcc, html
import plotly.express as px
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import pandas as pd
import preprocessamento
import graficos

# Inicialização da aplicação

app = dash.Dash(__name__, 
                external_stylesheets=[dbc.themes.CYBORG])

#Layout do dashboard

app.layout = dbc.Container([

    dbc.Row([ #Primeira linha
        dbc.Col([
            html.H1('Dashboard Monitoramento de Chuvas',
                    className= 'text-center text-primary'),
            html.Br()
        ])
    ]),

    dbc.Row([ #Segunda linha
        dbc.Col([
            dcc.Graph(figure=graficos.figura1)
        ])
    ]),

    dbc.Row([ #Terceira linha
        dbc.Col([ #Primeira coluna
              dcc.Dropdown(id='menu', value=['Glória','Velha Central', 'Itoupavazinha','Vorstadt'],
                           multi=True, options=[{'label':x, 'value':x} for x in graficos.pluvio_estacoes.columns]),
              dcc.Graph(id='grafico')
        ], width=6),
        dbc.Col([ #Segunda coluna
            dcc.Graph(figure=graficos.figura3)
        ], width={'size': 6})
    ], class_name='g-0'),

    dbc.Row([ #Quarta linha
        dbc.Col([
            dcc.Graph(figure=graficos.figura3)
        ])
    ])
])

# Callbacks
@app.callback(
    Output('grafico', 'figure'),
    Input('menu', 'value')
)

def funcao(acoes):
    data_fig = px.line(graficos.pluvio_estacoes[acoes])
    fig = (data_fig)
    fig.update_layout(title='Índice Pluviométrico por Estação',
                        yaxis_title='',
                        xaxis_title='',
                        template='plotly_dark',
                        showlegend=False)
    return fig


# Execução do aplicação
if __name__ == '__main__':
    app.run_server(debug=True)