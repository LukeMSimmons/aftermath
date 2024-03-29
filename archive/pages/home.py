from config import project_folder, buff, template, font, sig 
import dash; from dash import html, dcc, callback, Input, Output 
import plotly.express as px 
import pandas as pd 


# Get DataFrames 
co_df = pd.read_pickle(f'{project_folder}/data/pkl/co_df.pkl') 
steam_df = pd.read_pickle(f'{project_folder}/data/pkl/steam_games.pkl') 
health_df = pd.read_pickle(f'{project_folder}/data/pkl/us_health.pkl') 
energy_df = pd.read_pickle(f'{project_folder}/data/pkl/energy_df.pkl') 
heatmap_df = pd.read_pickle(f'{project_folder}/data/pkl/heatmap_df.pkl') 
wildfires_df = pd.read_pickle(f'{project_folder}/data/pkl/wildfires_df.pkl') 

# Register to app.py 
dash_title = 'Aftermath Dashboards' 
dash.register_page(__name__, title=dash_title) 



# Figures with no callbacks 


## Heatmap
title = f'Correlation Matrix: Object Class vs Feature'
heatmap_fig = px.imshow(heatmap_df, text_auto='.2f') 

heatmap_fig.update_layout(title=title, template=template, font_family=font, 
                          coloraxis_showscale=False)

heatmap_fig.update_layout(title_x=.5, title_y=.95, title_font_size=18)


## Energy Bubble 
title = f'Energy Trends by Country over time'
energy_fig = px.scatter(energy_df, x='Population', range_x=[0, 40e6], 
                        y='Energy Consumption (tWh)', range_y=[0, 1200], 
                        color='% Renewable', size='Per Capita (kWh)', size_max=70, 
                        animation_frame='Year', animation_group='ISO Code', 
                        hover_name='Country', text='ISO Code', 
                        color_continuous_scale='Temps_r') 

energy_fig.update_layout(title=title, title_x=.5, title_font_size=18, title_y=.95, 
                         template=template, font_family=font, height=600)

energy_fig.update_traces(textposition='top center') 


## Wildfires Map 
title = 'Wildfires in the US by Year'
wildfire_map = px.scatter_geo(wildfires_df, lat='Latitude', lon='Longitude', 
                              size='Size', color='Cause', hover_name='Name', 
                              animation_frame='Year', size_max=50)

wildfire_map.update_geos(visible=True, scope='usa', 
                         showcountries=True, countrycolor="Black", 
                         showsubunits=True, subunitcolor="Black", 
                         showlakes=True, lakecolor="LightBlue")

wildfire_map.update_layout(title=title, title_x=.5, title_y=.97, title_font_size=18, 
                           template=template, font_family=font, height=600, 
                           margin={'r':0,'t':0,'l':0,'b':0}, 
                           legend={'xanchor':'right', 'x':.99, 
                                   'yanchor':'bottom', 'y':-.16, 
                                   'bgcolor':'rgba(0,0,0,0)'}) 



# Layout
 
layout = html.Div([

    html.Div([
        html.Div([
            html.Img(src='/assets/aftermath_logo.png')], 
            style=dict(marginLeft=buff, marginTop='10px', display='inline-block')), 
        html.Div([
            html.H2(dash_title)], 
            style=dict(marginLeft='6px', verticalAlign='top', marginTop='6px', fontSize=16, display='inline-block')), 
        html.Div([], 
            style=dict(marginLeft=buff, height='2px', backgroundColor='#00c790', width='313px')), 
        html.Div([
            html.H4('Do you have data but want insights instead?')], 
            style=dict(marginLeft=buff, marginTop='26px')), 
        html.Div([
            html.H4(['A web app like this one might be right for you!'])], 
            style=dict(marginLeft=buff)), 
        html.Div([], 
            style=dict(marginLeft=buff, marginTop='30px', height='2px', backgroundColor='#00aa7b', width='380px'))], 
        style=dict()), 

    html.Br(), 
    html.Div([
        html.H4('The distribution of numerical variables is often a good place to start')], 
        style=dict(marginLeft=buff)), 

    html.Div([
        html.Div([
            html.H4('Select a variable'), 
            dcc.Dropdown(steam_df.columns, 'Metacritic Score', id='steam_dropdown')], 
            style=dict(marginLeft=buff, width='180px', display='inline-block')), 
        html.Div([
            html.H4('Marginal Plot'), 
            dcc.Dropdown(['box', 'violin', 'rug', 'None'], 'box', id='steam_m_dropdown')], 
            style=dict(marginLeft=buff, width='140px', display='inline-block'))], 
        style=dict()), 

    html.Div([
        html.Div([
            dcc.Graph(id='steam_histogram')], 
            style=dict())]), 

    html.Div([], style=dict(marginLeft=buff, marginTop='30px', height='2px', backgroundColor='#00aa7b')), 

    html.Br(), 
    html.Div([
        html.H4('Heatmaps are great for analyzing categorical relationships'), 
        html.H5('Callout: cosmic object type is correlated with redshift')], 
        style=dict(marginLeft=buff)), 

    html.Div([
        html.Div([
            dcc.Graph(figure=heatmap_fig)], 
            style=dict())]), 

    html.Div([], style=dict(marginLeft=buff, marginTop='30px', height='2px', backgroundColor='#00aa7b')), 

    html.Br(), 
    html.Div([
        html.H4("You can track variables over time with a line plot"), 
        html.H5('Protip: try double-clicking one of the items in the legend')], 
        style=dict(marginLeft=buff)), 

    html.Div([
        html.Div([
            html.H4('Select a State'), 
            dcc.Dropdown(co_df['State'].unique(), 'California', 
                         id='co_state_dropdown')], 
            style=dict(marginLeft=buff, width='150px', display='inline-block')), 
        html.Div([
            html.H4('Select Counties'), 
            dcc.Dropdown(value=['San Diego'], 
                         multi=True, id='co_county_dropdown')], 
            style=dict(marginLeft=buff, width='180px', display='inline-block'))]), 

    html.Div([
        html.Div([
            dcc.Graph(id='co_timeseries')], 
            style=dict())]), 

    html.Div([], style=dict(marginLeft=buff, marginTop='30px', height='2px', backgroundColor='#00aa7b')), 

    html.Br(), 
    html.Div([
        html.H4("Let's check out something a bit more animated"), 
        html.H5('Hint: pick a metric and hit the play button')], 
        style=dict(marginLeft=buff)), 

    html.Div([
        html.Div([
            html.H4('Select a Metric'), 
            dcc.Dropdown(sorted(health_df['Question'].unique(), reverse=True), 
                         'Sale of cigarette packs', id='health_dropdown')], 
            style=dict(marginLeft=buff, width='600px', display='inline-block'))]), 

    html.Div([
        html.Div([
            dcc.Graph(id='health_bar')], 
            style=dict())]), 

    html.Div([], style=dict(marginLeft=buff, marginTop='30px', height='2px', backgroundColor='#00aa7b')), 

    html.Br(), 
    html.Div([
        html.H4('Bubble Charts are great for analyzing a bunch of related metrics'), 
        html.H5('Pop Quiz: Can you find the US?')], 
        style=dict(marginLeft=buff)), 

    html.Div([
        html.Div([
            dcc.Graph(figure=energy_fig)], 
            style=dict())]), 

    html.Div([], style=dict(marginLeft=buff, marginTop='30px', height='2px', backgroundColor='#00aa7b')), 

    html.Br(), 
    html.Div([
        html.H4("Sometimes we're especially interested in where stuff happens geographically"), 
        html.H5('Suggestion: double-click a Cause to isolate it, and hit play')], 
        style=dict(marginLeft=buff)), 

    html.Br(), 
    html.Div([
        html.Div([
            dcc.Graph(figure=wildfire_map)], 
            style=dict())]), 

    html.Div([], style=dict(marginLeft=buff, marginTop='30px', height='2px', backgroundColor='#00aa7b')), 

    html.Br(), 
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

    title = f'{col} for Games on Steam'
    fig.update_layout(title=title, title_x=.5, title_y=.95, title_font_size=18, 
                      template=template, font_family=font, height=600)
    return fig 


## Filter Dropdown 
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

    title = 'Daily Max CO by County in 1980'
    fig = px.line(dfi, x='Date', y='Max CO', color='Site') 
    
    fig.update_layout(title=title, title_x=.5, title_y=.95, title_font_size=18, 
                      template=template, font_family=font, height=600, 
                      legend={'xanchor':'center', 'x':.5, 
                              'yanchor':'top', 'y':1, 
                              'bgcolor':'rgba(0,0,0,0)', 
                              'title':''})
    
    fig.update_yaxes(title='Max CO (ppm)', rangemode='tozero')

    return fig


## Health Bar 
@callback(
    Output('health_bar', 'figure'), 
    Input('health_dropdown', 'value'))

def health_bar(question): 

    dfi = health_df[health_df['Question']==question] 

    title = question[0:30] + '...' if len(question)>30 else question 
    title+= ' by State over time'

    fig = px.bar(dfi, x='DataValue', y='LocationDesc', orientation='h', 
                 animation_frame='YearStart', animation_group='LocationDesc', 
                 range_x=[0, dfi['DataValue'].max()])

    fig.update_layout(title=title, title_x=.5, title_y=.96, title_font_size=18, 
                      template=template, xaxis_title= '', yaxis_title='', 
                      font_family=font, height=700) 

    return fig 
