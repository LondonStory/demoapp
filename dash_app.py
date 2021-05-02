import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input
import plotly.express as px
import pandas as pd
import numpy as np

# Working with Data Frame
dff = pd.read_csv("https://raw.githubusercontent.com/javedhassans/demoapp/main/workingsheet.csv")

# Creating dash app

app = dash.Dash(__name__)
# server = app.server

app.layout = html.Div([
    html.H1('Funding on Dutch Elections',
            style={'textAlign': 'center', 'margin-bottom': '5px', 'color': 'white'}),
    html.H5('Amount spent by parties', style={'textAlign': 'center', 'margin-bottom': '10px', 'color': 'white'}
            ),

    html.Div([

        html.Div([
            html.H6(children='Total Parties',
                    style={'text-align': 'center',
                           'color': 'white'}),
            html.P(f"{dff['Party'].nunique():,.0f}",
                   style={'text-align': 'center', 'color': 'orange',
                          'fontSize': 40})

        ], className='card_container four columns'),

        html.Div([
            html.H6(children='Total Number of Adds',
                    style={'text-align': 'center',
                           'color': 'white'}),
            html.P(f"{dff['Number of Ads in Library'].sum():,.0f}",
                   style={'text-align': 'center', 'color': 'orange',
                          'fontSize': 40})

        ], className='card_container four columns'),

        html.Div([
            html.H6(children='Total Amount in Euros',
                    style={'text-align': 'center',
                           'color': 'white'}),
            html.P(f"{dff['Amount Spent (EUR)'].sum():,.0f}",
                   style={'text-align': 'center', 'color': 'orange',
                          'fontSize': 40})

        ], className='card_container four columns'),

    ], className='row flex display'),

    html.Div([
        html.Div([
            html.P('Select Party:', className='fix_label', style={'color': 'white'}),
            dcc.Dropdown(id='w_parties',
                         multi=False,
                         searchable=True,
                         value='',
                         placeholder='Select Party',
                         options=[{'label':c, 'value':c}
                                  for c in (dff['Party'].unique())], className='dcc_compon')

        ], className='create_container three columns')

    ], className='row flex-display')

])

# id='mainContainer', style={'display': 'flex', 'flex-direction': 'column', 'margin-bottom': '25px'}

if __name__ == '__main__':
    app.run_server(debug=True)
