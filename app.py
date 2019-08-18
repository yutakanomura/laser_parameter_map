import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

df = pd.read_csv('laser_data.csv')

fig = px.scatter(df, x='lc', y='average_power', log_y=True, color='gain_medium')
fig.update_traces(marker=dict(size=12),
                  selector=dict(mode='markers'))

# Prepare the view
app = dash.Dash()
server = app.server

app.layout = html.Div(children=[
    html.H1(
        children='Hello Dash',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(
        children='Dash: A web application framework for Python',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    dcc.Graph(
        id='laser-data',
        figure=fig
    ),
])


if __name__ == '__main__':
    app.run_server(debug=True)
