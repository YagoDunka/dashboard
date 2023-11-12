import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State

# Iniciar Aplicação 
app = dash.Dash(__name__)

# Estrutura da aplicação
app.layout = html.Div(children=[
    html.H2(children='Atualiza valor do texto!'),
    html.Br(),
    'Entrada: ', dcc.Input(id='entrada', value='Valor inicial'),
    html.Button(id='botao', n_clicks=0, children='Aciona callback'),
    html.Br(),
    html.H4(id='saida', children='')
])

# Callbacks
@app.callback(
    Output(component_id='saida', component_property='children'),
    [Input(component_id='botao', component_property='n_clicks')],
    [State(component_id='entrada', component_property='value')]
)

def funcao(clicks, a):
    if clicks is None:
        raise dash.exceptions.PreventUpdate
    clicks = int(clicks)
    if clicks > 0:
        b = f'Texto inserido: {a}'
        return b
    else:
        raise dash.exceptions.PreventUpdate

# Executar aplicação
if __name__ == '__main__':
    app.run_server(debug=True)
