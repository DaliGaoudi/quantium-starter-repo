from app import app 

from dash import html,dcc 

def test_app_vis():
    vis = app.layout.children[3]
    assert isinstance(vis, dcc.Graph), 'Expected the graph to be wrapped in a Graph component'

