import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(
    children=[
        # represents the URL bar, doesn't render anything
        dcc.Location(
            id='url',
            refresh=False,
        ),
        dcc.Link(
            children='Navigate to "/"',
            href='/',
        ),
        html.Br(),
        dcc.Link(
            children='Navigate to "/page-2"',
            href='/page-2',
        ),
        # content will be rendered in this element
        html.Div(id='page-content')
    ]
)

@app.callback(
    Output(
        component_id='page-content',
        component_property='children',
        ),
    [Input(
        component_id='url',
        component_property='pathname',
        )]
)
def display_page(pathname):
    return html.Div([
        html.H3('You are on page {}'.format(pathname))
    ])
