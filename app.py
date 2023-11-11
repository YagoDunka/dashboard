import dash
from dash import html, dcc 
import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd
import seaborn as sns

dataset = sns.load_dataset('iris')

app = dash.Dash(__name__,
                external_stylesheets=[dbc.themes.SUPERHERO])

sepal_fig = px.scatter(dataset,
                       x='sepal_length',
                       y='sepal_width',
                       color='species',
                       title='Sépala',
                       template='plotly_dark')

petal_fig = px.scatter(dataset,
                          x='petal_length',
                          y='petal_width',
                          color='species',
                          title='Pétala',
                          template='plotly_dark')

app.layout = html.Div(children=[
    html.H1('Visualização do Dataset Iris'),
    html.Div([
        dcc.Graph(figure=sepal_fig),
        dcc.Graph(figure=petal_fig)
    ], style={'display': 'flex'})
])

if __name__ == '__main__':
    app.run_server(debug=True)