from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px

from app import app

def test_header():
    header = app.layout.children[0]
    assert isinstance(header, html.H1), 'Expected the first child of the layout to be an H1 header'
    assert header.children == 'Pink Morsel Sales Dashboard', 'Expected the header text to be "Pink Morsel Sales Dashboard"'

