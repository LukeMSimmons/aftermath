import os 
from dash import html 

project_folder = os.path.dirname(os.path.abspath(__file__))

template = 'simple_white' 
font = 'Helvetica' 
buff = '14px' 

breakline = html.Div([], style=dict(marginLeft=buff, marginTop='30px', height='2px', backgroundColor='#00aa7b'))

sig = html.Div([
        html.Div([
            html.H4("If interactive visualizations like these would enhance data consumption in your organization, have us build your own dashboard and watch the insights pour right out.")], 
            style=dict(marginTop='33px')), 
        html.Div([
            html.H4('For more information or a quote, send an email to:')], 
            style=dict(display='inline-block')), 
        html.Div([
            html.A('hello@aftermathdashboards.com', 
                   href='mailto:hello@aftermathdashboards.com', 
                   style=dict(color='darkcyan', textDecoration='none'))], 
            style=dict(marginLeft='4px', display='inline-block')), 
        html.Br()], 
        style=dict(marginLeft=buff)) 
