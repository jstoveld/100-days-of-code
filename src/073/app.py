"""
Created 7-25-20 07:50 AM
Edited Last: 7-25-20 07:50 AM

@author: JS
"""

import flask
from flask_caching import Cache
import dash
import dash_bootstrap_components as dbc


server = flask.Flask(__name__)
app = dash.Dash(
    __name__,
    server=server,
    external_stylesheets = [
        dbc.themes.SLATE, #This is our bootstrap theme
        "https://use.fontawesome.com/releases/v5.9.0/css/all.css", #Importing SoMed icons

    ],
    meta_tags= [
        {
            "name": "description",
            "content": "Covid19 - Dashboard",
        },
        {
            "name": "Viewpoint",
            "content": "width=device-width, initial-scale=1.0"
        },
    ],
)