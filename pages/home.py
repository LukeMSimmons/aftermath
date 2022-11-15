import dash; from dash import html, dcc, callback, Input, Output 
from config import buff, sig 


# Register to app.py 
title = 'Aftermath Dashboards' 
dash.register_page(__name__, title=title) 


layout = html.Div([

    html.Div([
        html.H1(title)], 
        style=dict(marginLeft=buff)), 

    html.Div([
        html.H2('Do you have lots of data, but want a dashboard instead?')], 
        style=dict(marginLeft=buff)), 



    sig])
