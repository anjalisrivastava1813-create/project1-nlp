# Import required libraries
from pathlib import Path

import pandas as pd
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px

# Read the airline data into pandas dataframe
DATA_PATH = Path(__file__).resolve().with_name("spacex_launch_dash.csv")

spacex_df = pd.read_csv(DATA_PATH)
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()
launch_site =  ['ALL']+sorted(spacex_df['Launch Site'].unique())
# Create a dash application
app = dash.Dash(__name__)

# Create an app layout
app.layout = html.Div(children=[html.H1('SpaceX Launch Records Dashboard',
                                        style={'textAlign': 'center', 'color': '#503D36',
                                               'font-size': 40}),
# TASK 1: Add a dropdown list to enable Launch Site selection
# # The default select value is for ALL sites

# dcc.Dropdown(id='site-dropdown',...)
                                dcc.Dropdown(id='site-dropdown',
                                             options = [{"label": site, "value": site} for site in launch_site],
                                             value='ALL',
                                ),
                                html.Br(),

                                # TASK 2: Add a pie chart to show the total successful launches count for all sites
                                # If a specific launch site was selected, show the Success vs. Failed counts for the site
                                html.Div(dcc.Graph(id='success-pie-chart')),

                                html.Br(),

                                html.P("Payload range (Kg):"),
# TASK 3: Add a slider to select payload range
                                #dcc.RangeSlider(id='payload-slider',...)
                                dcc.RangeSlider(id='payload-slider',
                                min = 0,
                                max = 10000,
                                step = 1000,
                                marks = {0:'0',2500:'2500',5000:'5000',7500:'7500', 10000:'10000'},
                                value = [min_payload, max_payload],
                                ),



# TASK 4: Add a scatter chart to show the correlation between payload and launch success
                                html.Div(dcc.Graph(id='success-payload-scatter-chart')),
                                ])

# TASK 2:
# Add a callback function for `site-dropdown` as input, `success-pie-chart` as output
@app.callback(Output('success-pie-chart', 'figure'), Input('site-dropdown', 'value'))
def dropdown_list_update(selected_site):
    if selected_site== 'ALL':
        success_df = spacex_df[spacex_df['class'] == 1]
        return px.pie(success_df,
               names = "Launch Site",
               title = "Total Successfull Launches")
    else:
        filter_df = spacex_df[spacex_df['Launch Site'] == selected_site]
        fail_dic =  filter_df['class'].value_counts()
        return px.pie(names=['Failure', 'Success'],
                      values=[fail_dic.get(0, 0), fail_dic.get(1, 0)],
                    title=f'Launch Outcomes for Site {selected_site}'
                      )
        





# TASK 4:
# Add a callback function for `site-dropdown` and `payload-slider` as inputs, `success-payload-scatter-chart` as output



# Run the app
if __name__ == '__main__':
    app.run()
