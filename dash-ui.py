from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash("Pink Morsel Sales Dashboard")


df = pd.read_csv('./data/sales_summary.csv')

fig = px.line(df, x="date", y="sales", color="region", title="Pink Morsel Sales by Region Over Time")

app.layout = html.Div(children=[
    html.H1(children='Pink Morsel Sales Dashboard'),
    html.Div(children='''
        A dashboard to visualize the sales of pink morsels across different regions over time.
    '''),

    dcc.Graph(
        id='sales-graph',
        figure=fig
    )
])

app.run(debug=True)