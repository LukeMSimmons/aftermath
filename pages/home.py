from config import project_folder, buff, template, font, sig 
import dash; from dash import html, dcc, callback, Input, Output 
import plotly.express as px 
import pandas as pd 

import os 

# Get DataFrames 
co_df = pd.read_pickle(f'{project_folder}/data/pkl/co_df.pkl') 
steam_df = pd.read_pickle(f'{project_folder}/data/pkl/steam_games.pkl') 

# Register to app.py 
title = 'Aftermath Dashboards' 
dash.register_page(__name__, title=title) 


layout = html.Div([

    html.Div([
        html.Div([
            html.Img(src='/assets/aftermath_logo.png')], 
            style=dict(marginLeft='8px', display='inline-block')), 
        html.Div([
            html.H1(title)], 
            style=dict(marginLeft='14px', display='inline-block'))], 
        style=dict(height='58px')), 
    
    html.Div([
        html.Div([
            html.H3('Do you have raw data, but want insights instead?')]), 
        html.Div([
            html.H3('A web app like this one might just be right for you!')])], 
        style=dict(marginLeft=buff, height='82px')), 

    html.Div([
        html.H3('You may want to analyze one numerical variable, perhaps with a histogram.')], 
        style=dict(marginLeft=buff)), 

    html.Div([
        html.Div([
            html.H4('Select a variable'), 
            dcc.Dropdown(steam_df.columns, 'Metacritic Score', id='steam_dropdown')], 
            style=dict(marginLeft=buff, width='10%', display='inline-block')), 
        html.Div([
            html.H4('Marginal Plot Type'), 
            dcc.Dropdown(['box', 'violin', 'rug', 'None'], 'box', id='steam_m_dropdown')], 
            style=dict(marginLeft=buff, width='10%', display='inline-block'))]), 

    html.Div([
        html.Div([
            dcc.Graph(id='steam_histogram')], 
            style=dict())]), 

    html.Br(), 
    html.Div([
        html.H3('You can track variables over time with a line plot.'), 
        html.H5('Protip: try double-clicking one of the sites in the legend.')], 
        style=dict(marginLeft=buff)), 

    html.Div([
        html.Div([
            html.H4('Select a State'), 
            dcc.Dropdown(co_df['State'].unique(), 'California', 
                         id='co_state_dropdown')], 
            style=dict(marginLeft=buff, width='10%', display='inline-block')), 
        html.Div([
            html.H4('Select Counties'), 
            dcc.Dropdown(value=['San Diego'], 
                         multi=True, id='co_county_dropdown')], 
            style=dict(marginLeft=buff, width='12%', display='inline-block'))]), 

    html.Div([
        html.Div([
            dcc.Graph(id='co_timeseries')], 
            style=dict())]), 

    html.Br(), html.Br(), 
    html.Div([
        html.H3('Let us build your interactive dashboard, and watch the insights pour right out.')], 
        style=dict(marginLeft=buff)), 

    sig]) 



# Elements with Callbacks 


## Steam Games 
@callback(
    Output('steam_histogram', 'figure'), 
    Input('steam_dropdown', 'value'), 
    Input('steam_m_dropdown', 'value'))

def steam_fig(col, marginal): 

    marginal = False if marginal == 'None' else marginal 

    fig = px.histogram(steam_df[steam_df[col]!=0], x=col, marginal=marginal) 

    title = f'Distribution of {col} for Games on Steam'
    fig.update_layout(title=title, title_x=.45, title_font_size=18, 
                      template=template, font_family=font, height=600)
    return fig 









## CO Timeseries 
@callback(
    Output('co_county_dropdown', 'options'), 
    Input('co_state_dropdown', 'value')) 

def filter_dropdown(state): 
    return co_df[co_df['State']==state]['County'].unique()


## CO Timeseries 
@callback(
    Output('co_timeseries', 'figure'), 
    Input('co_state_dropdown', 'value'), 
    Input('co_county_dropdown', 'value'))

def co_timeseries(state, counties): 
    
    dfi = co_df[(co_df['State']==state) & (co_df['County'].isin(counties))]

    title = 'Daily Max Carbon Monoxide by County in 1980'
    fig = px.line(dfi, x='Date', y='Max CO', color='Site') 
    
    fig.update_layout(title=title, title_x=.45, title_font_size=18, 
                      template=template, font_family=font, height=600)
    
    fig.update_yaxes(title='Max CO (ppm)', rangemode='tozero')

    return fig
