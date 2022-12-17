from dash import html 

template = 'simple_white' 
font = 'Helvetica' 
buff = '14px' 

sig = html.Div([
        html.Div([
            html.H4('For more information, or a quote, send an email to:')], 
            style=dict(marginLeft=buff, display='inline-block')), 
        html.Div([
            html.A('contactlukesimmons@gmail.com', 
                   href='https://linkedin.com/in/lukemsimmons', 
                   style=dict(color='darkcyan', textDecoration='none'))], 
            style=dict(marginLeft='4px', fontSize='20px', display='inline-block'))], 
        style=dict(marginLeft='27%', color='#595959')) 
