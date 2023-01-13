import os 
from dash import html 

project_folder = os.path.dirname(os.path.abspath(__file__))

template = 'simple_white' 
font = 'Helvetica' 
buff = '14px' 

sig = html.Div([
        html.Div([
            html.H4('For more information or a quote, send an email to:')], 
            style=dict(display='inline-block')), 
        html.Div([
            html.A('hello@aftermathdashboards.com', 
                   href='mailto:hello@aftermathdashboards.com', 
                   style=dict(color='darkcyan', textDecoration='none'))], 
            style=dict(marginLeft='4px', fontSize='18px', display='inline-block')), 
        html.Br(), html.Br()], 
        style=dict(marginLeft=buff)) 
