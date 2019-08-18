import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

df = pd.read_csv('laser_data.csv')

col_options = [dict(label=x, value=x) for x in df.columns]
dimensions = ['x', 'y', 'color', 'facet_col', 'facet_row']

# Prepare the view
app = dash.Dash()
server = app.server

app.layout = html.Div(
    [
        html.H1(
            children='Fiber Laser Parameters',
            style={
                'textAlign': 'center',
                'color': colors['text']
            }
        ),

        html.Div(
            [
                html.P([d + ":", dcc.Dropdown(id=d, options=col_options)])
                for d in dimensions
            ],
            style={"width": "25%", "float": "left"},
        ),

        dcc.Graph(
            id='laser-data-graph',
            style={"width": "75%", "display": "inline-block"}
        ),
    ]
)

@app.callback(
    Output('laser-data-graph', 'figure'),
    [Input(d, 'value') for d in dimensions]
)
def make_figure(x, y, color, facet_col, facet_row):
    fig = px.scatter(
        df,
        x=x,
        y=y,
        color=color,
        facet_col=facet_col,
        facet_row=facet_row,
        height=700,
    )
    fig.update_traces(marker=dict(size=12),
                      selector=dict(mode='markers'))
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
