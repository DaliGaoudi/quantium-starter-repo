from dash import Dash, Output, html, dcc, Input, callback
import plotly.express as px
import pandas as pd

app = Dash("Pink Morsel Sales Dashboard")

colors = {
    'background': '#111111',
    'text': '#D96C57'
}

df = pd.read_csv('./data/sales_summary.csv')
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values('date')

fig = px.line(df, x="date", y="sales", color="region", title="Pink Morsel Sales by Region Over Time")

fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

app.layout = html.Div(children=[
    html.H1(children='Pink Morsel Sales Dashboard', style={"text-align": "center",
                                                           "color" : colors["text"]}),
    html.Div(children='''
        A dashboard to visualize the sales of pink morsels across different regions over time.
    ''', style={"text-align": "center", "color" : colors["text"]}),

    dcc.RadioItems(
        id='region-radio',
        options=[
            {'label': 'North', 'value': 'north'},
            {'label': 'East', 'value': 'east'},
            {'label': 'South', 'value': 'south'},
            {'label': 'West', 'value': 'west'},
            {'label': 'All', 'value': 'all'},
        ],
        value='all',
        labelStyle={'display': 'inline-block', 'margin-right': '12px'},
        inline=True,
        style={}
    ),

    dcc.Graph(
        id='sales-graph',
        figure=fig
    ),
])



@callback(
    Output('sales-graph', 'figure'),
    Input('region-radio', 'value')
)
def update_graph(selected_region):
    if selected_region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['region'] == selected_region]

    fig = px.line(filtered_df, x="date", y="sales", color="region", title="Pink Morsel Sales by Region Over Time")
    fig.update_layout(transition_duration=300)
    return fig


if __name__ == '__main__':
    app.run(debug=False)
