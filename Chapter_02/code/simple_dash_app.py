
from dash import Dash, dcc, html

app = Dash()
app.layout = html.Div([
    dcc.Graph(figure={'data': [{'x': [1, 2, 3], 'y': [4, 1, 2]}]})
])
app.run_server(debug=True)
