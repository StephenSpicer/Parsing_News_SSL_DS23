# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import joblib 

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## We can predict fake news at least as well as flipping a coin by training a model. 

            Theoretically we can also let you paste text into this same model...

            ✅ REAL - a 0 will be displayed.

            ❌ Fake - a 1 will be displayed.

            """
        ),
        dcc.Link(dbc.Button('Predict', color='primary'), href='/predictions')
    ],
    md=4,
)

# # gapminder = px.data.gapminder()
# # fig = px.scatter(gapminder.query("year==2007"), x="gdpPercap", y="lifeExp", size="pop", color="continent",
# #            hover_name="country", log_x=True, size_max=60)

column2 = html.Div([
    dcc.Textarea(
        id='textarea-example',
        value='Textarea content initialized\nwith multiple lines of text',
        style={'width': '500%', 'height': 300},
    ),
    html.Div(id='textarea-example-output', style={'whiteSpace': 'pre-line'})
])

# column2 = dbc.Col(
#     [
#         #dcc.Graph(figure=fig),
#     ]
# )

layout = dbc.Row([column1, column2])

def predict(value=value):
    data = {'text': [value]}
    df = pd.DataFrame(data)
    y_pred = model.predict(df['text'])
    return "Fake = ".format(y_pred)

