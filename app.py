import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go



app = dash.Dash()
server = app.server

############# Make changes here


app.layout = html.Div(children=[
    html.H1('Animal Cracker Poularity'),
    dcc.Graph(
        id='this_is_an_id',
        figure={
            'data': [
                {'x': ['Elephant','Monkey','Lion'], 'y': [10,3,4], 'type': 'bar', 'name': 'Kids'},
                {'x': ['Elephant','Monkey','Lion'], 'y': [10,4,5], 'type': 'bar', 'name': 'Keepers'},
            ],
            'layout': {
                'title': 'Yummy Crackers',
                'xaxis':{'title':'Most Chosen by'},
                'yaxis':{'title':'Approval Rating'},
            }
        }
    )]
)


###### Don't change anything here



if __name__ == '__main__':
    app.run_server()
