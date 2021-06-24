import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

### Dash instance ###
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(
        __name__,
        external_stylesheets=external_stylesheets,
        )

### Page container ###
page_container = html.Div(
    children=[
        # represents the URL bar, doesn't render anything
        dcc.Location(
            id='url',
            refresh=False,
        ),
        # content will be rendered in this element
        html.Div(id='page-content')
    ]
)

### Index Page Layout ###
index_layout = html.Div(
    children=[
        dcc.Link(
            children='Go to Page 1',
            href='/page-1',
        ),
        html.Br(),
        dcc.Link(
            children='Go to Page 2',
            href='/page-2',
        ),
    ]
)

### Page 1 Layout and Callback ###
page_1_layout = html.Div(
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

### Page 2 Layout and Callbacks ###
page_2_layout = html.Div(
    children=[
        html.H1(
            children='Page 2',
        ),
        dcc.RadioItems(
            id='page-2-radios',
            options=[{'label': i, 'value': i} for i in ['Orange', 'Blue', 'Red']],
            value='Orange',
        ),
        html.Div(
            id='page-2-content',
        ),
        html.Br(),
        dcc.Link(
            children='Go to Page 1',
            href='/page-1',
        ),
        html.Br(),
        dcc.Link('Go back to home', href='/')
    ]
)

@app.callback(
    Output(
        component_id='page-2-content',
        component_property='children',
    ),
    [Input(
        component_id='page-2-radios',
        component_property='value',
    )]
)
def page_2_radios(value):
    return 'You have selected "{}"'.format(value)

### Set app layout to page container ###
app.layout = page_container

### Assemble all layouts ###
app.validation_layout = html.Div(
    children = [
        page_container,
        index_layout,
        page_1_layout,
        page_2_layout,
    ]
)

### Update Page Container ###
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
    # add if index page
    if pathname == '/page-1':
        return page_1_layout
    elif pathname == '/page-2':
        return page_2_layout
    else:
        return index_layout
