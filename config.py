from dash import html 

template = 'simple_white' 
font = 'Helvetica' 
buff = '14px' 

sig = html.Div([
        html.Div([
            html.A('contact', href='https://linkedin.com/in/lukemsimmons', 
                style=dict(color='darkcyan', textDecoration='none'))], 
            style=dict(marginLeft=buff))], 
        style=dict(color='#595959')) 
