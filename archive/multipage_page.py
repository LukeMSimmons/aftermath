import dash; from dash import html, dcc, callback, Input, Output 

# Register to app.py
title = 'Aftermath Dashboards' 
dash.register_page(__name__, title=title) 

layout = html.Div([

    html.H1('Aftermath Dashboards')])
