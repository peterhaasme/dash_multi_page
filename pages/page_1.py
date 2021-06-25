### Import Packages ###
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

### Import Dash Instance ###
from app import app

### Page 1 Layout and Callback ###
layout = html.Div(
    children=[
        html.H1(
            children='Page 1',
        ),
        dcc.Dropdown(
            id='page-1-dropdown',
            options=[{'label': i, 'value': i} for i in ['LA', 'NYC', 'MTL']],
            value='LA',
        ),
        html.Div(
            id='page-1-content',
        ),
        html.Br(),
        dcc.Link(
            children='Go to Page 2',
            href='/page-2',
        ),
        html.Br(),
        dcc.Link('Go back to home', href='/'),
    ]
)

@app.callback(
    Output(
        component_id='page-1-content',
        component_property='children',
    ),
    [Input(
        component_id='page-1-dropdown',
        component_property='value',
    )]
)
def page_1_dropdown(value):
    return 'You have selected "{}"'.format(value)
