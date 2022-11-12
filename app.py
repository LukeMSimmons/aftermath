import dash
from dash import Dash, html

app = Dash(__name__, use_pages=True)

app.layout = html.Div([dash.page_container]) 
