import dash
import custom_basic_auth
import dash_html_components as html
import dash_core_components as dcc
import plotly

# Keep this out of source code repository - save in a file or a database
def authenticate(username, password):
    return (username == '1' and password == '2')

app = dash.Dash('auth')
auth = custom_basic_auth.CustomBasicAuth(
    app,
    authenticate
)

app.layout = html.Div([
    html.H1('Welcome to the app'),
    html.H3('You are successfully authorized'),
    dcc.Dropdown(
        id='dropdown',
        options=[{'label': i, 'value': i} for i in ['A', 'B']],
        value='A'
    ),
    dcc.Graph(id='graph')
], className="container")

@app.callback(
    dash.dependencies.Output('graph', 'figure'),
    [dash.dependencies.Input('dropdown', 'value')])
def update_graph(dropdown_value):
    return {
        'layout': {
            'title': 'Graph of {}'.format(dropdown_value),
            'margin': {
                'l': 20,
                'b': 20,
                'r': 10,
                't': 60
            }
        },
        'data': [{'x': [1, 2, 3], 'y': [4, 1, 2]}]
    }

app.scripts.config.serve_locally = True
app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

if __name__ == '__main__':
    app.run_server(debug=True)
