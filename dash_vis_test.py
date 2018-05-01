import time
import datetime
import requests
import sqlite3
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

app = dash.Dash(__name__)
app.layout = html.Div(
    html.Div([
        html.H4('Cryptocurrency Price'),
        html.Div(id='live-update-text'),
        dcc.Graph(id='live-update-graph'),
        dcc.Interval(
            id='interval-component',
            interval=10*1000, # in milliseconds
            n_intervals=0
        )
    ])
)


@app.callback(Output('live-update-text', 'children'),
              [Input('interval-component', 'n_intervals')])
def update_metrics(n):
    conn = sqlite3.connect('crypto.db')
    c = conn.cursor()
    cur = pd.read_sql_query('SELECT price FROM current_data',conn)
    price= cur.iloc[0]['price']
    #c.execute('SELECT * FROM current_data')
    #table =  c.fetchall()
    #price = table[0][1]
    style = {'padding': '5px', 'fontSize': '32px'}
    return [
        #html.Span('time: {0:.2f}'.format(time), style=style),
        html.Span('price: {0:.2f}'.format(price), style=style),
    ]
    conn.close()

# Multiple components can update everytime interval gets fired.
@app.callback(Output('live-update-graph', 'figure'),
              [Input('interval-component', 'n_intervals')])
def update_graph_live(n):
    conn = sqlite3.connect('crypto.db')
    c = conn.cursor()
    his = pd.read_sql_query('SELECT * FROM historical_data',conn)
    data = {
        'time': his['time'],
        'price': his['price'],
    }
    conn.close()
    # Create the graph with subplots
    fig = plotly.tools.make_subplots(rows=1, cols=1, vertical_spacing=0.2)
    fig['layout']['margin'] = {
        'l': 30, 'r': 10, 'b': 30, 't': 10
    }
    fig['layout']['legend'] = {'x': 0, 'y': 1, 'xanchor': 'left'}

    fig.append_trace({
        'x': data['time'],
        'y': data['price'],
     }, 1, 1)
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)

