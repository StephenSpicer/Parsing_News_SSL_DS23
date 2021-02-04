# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app
from joblib import load
pipeline = load('notebooks/saved_model.joblib')

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Predictions

            Your instructions: Paste content from an article that you would like to return a prediction on. 
            The number that comes back is the probability of your content being "Fake" based on the 40,000 news articles
            that my model was trained on. When pasting, be sure that you only include words from the body of the article, no HTML elements,
            images, advertisements, or anything that is not strictly text, since that is what the model is able to process.
            The model will count the term frequency of your content, compare it to the articles it was trained on, and return the probability 
            that what you pasted is "Fake", based off of what it has been trained on. 

            """
        )
    ],
    md=4,
)

column2 = dbc.Col(
    [
        dcc.Textarea(
        id='textarea-example',
        value='Textarea content initialized\nwith multiple lines of text',
        style={'width': 500, 'height': 300},
    ),
    html.Div(id='textarea-example-output', style={'whiteSpace': 'pre-line'})   

     ],
    md=4,
)

column3 = dbc.Col(
    [
        dcc.Textarea(
        id='textarea-example',
        value='Textarea content initialized\nwith multiple lines of text',
        style={'width': 500, 'height': 300},
    ),
    html.Div(id='textarea-example-output', style={'whiteSpace': 'pre-line'})   

     ],
    md=4,
)

layout = dbc.Row([column1, column2, column3])

# @app.callback(
#     Output('prediction-content','children'),
#     [Input('paste text here', 'value')])

# # #def predict(quantity,extraction_type_class,amount_tsh,population):
# #     df = pd.DataFrame(columns=['quantity','extraction_type_class','amount_tsh',
# #     'population'],
# #     data=[[quantity,extraction_type_class,amount_tsh,population]])
# #     y_pred = pipeline.predict(df)[0]
# #     return "The waterpump is {}!".format(y_pred)

# layout = dbc.Row([input_col,prediction_col])
