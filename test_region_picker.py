from dash import html

from app import app
from selenium import webdriver


def test_reguin_picker(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element('#region-radio', timeout=10)


