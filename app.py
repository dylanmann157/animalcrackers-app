import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go



app = dash.Dash()
server = app.server

############# Make changes here


app.layout = html.Div(children=[
    html.H1('your changed title here'),
    dcc.Graph(
        id='this_is_an_id',
        figure={
            'data': [
                {'x': ['thing1','thing2','thing3'], 'y': [2,3,4], 'type': 'bar', 'name': 'new label 1'},
                {'x': ['thing1','thing2','thing3'], 'y': [3,4,5], 'type': 'bar', 'name': 'new label 2'},
            ],
            'layout': {
                'title': 'new title here',
                'xaxis':{'title':'Choice of data visualization'},
                'yaxis':{'title':'Approval rating by average data scientist'},
            }
        }
    )]
)


###### Don't change anything here



if __name__ == '__main__':
    app.run_server()
