# Copyright 2019 NullConvergence
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import json

import dash
import dash_cytoscape as cyto
import dash_core_components as dcc
import dash_html_components as html

from dash.dependencies import Input, Output

from db import Database
import filter
import developers
import files

from datetime import datetime, date

DB_URL = 'localhost'
PORT = 13000
DB_USER = 'neo4j'
DB_PWD = 'letmein'

app = dash.Dash(__name__)

db = Database()
db.configure(
    db_url=DB_URL,
    port=PORT,
    db_user=DB_USER,
    db_pwd=DB_PWD,
)

data = db.get_all_data(merge=True)
nodes, relations = db.get_all_data(merge=False)

dev = developers.Developers(nodes, relations)
fil = files.Files(nodes, relations)

# dev.print_dev_last(dev.list_dev_ids())
# dev.show_developers_activity(dev.list_dev_ids())

devs = ['Select developer']
devs += dev.list_dev_name()

n_files = ['Select file']
n_files += fil.list_file_name()

filetypes = ['Select filetype']
filetypes += fil.list_filetype_name()


styles = {
    'json-output': {
        'overflow-y': 'scroll',
        'height': 'calc(50% - 25px)',
        'border': 'thin lightgrey solid',
    },
    'tab': {'height': 'calc(98vh - 115px)'}
}
#UI NODE AND EDGE STYLES
default_stylesheet = [
    {
        "selector": '[type = "Year"]',
        'style': {
            "opacity": 0.9,
            'height': 25,
            'width': 25,
            'background-color': '#000080',
            'content': 'data(label)'
        }
    },
    {
        "selector": '[type = "Month"]',
        'style': {
            "opacity": 0.9,
            'height': 25,
            'width': 25,
            'background-color': '#6495ED',
            'content': 'data(label)'
        }
    },
    {
        "selector": '[type = "Day"]',
        'style': {
            "opacity": 0.9,
            'height': 25,
            'width': 25,
            'background-color': '#ADD8E6',
            'content': 'data(label)'
        }
    },
    {
        "selector": '[type = "Developer"]',
        'style': {
            "opacity": 0.9,
            'height': 25,
            'width': 25,
            'shape' : 'triangle',
            'background-color': '#00CCCC',
            'content': 'data(label)'
        }
    },
    {
        "selector": '[type = "File"]',
        'style': {
            "opacity": 0.9,
            'height': 25,
            'width': 25,
            'shape' : 'square',
            'background-color': '#330099',
            'content': 'data(label)'
        }
    },
    {
        "selector": '[type = "Filetype"]',
        'style': {
            "opacity": 0.9,
            'height': 25,
            'width': 25,
            'shape' : 'square',
            'background-color': '#4544ae',
            'content': 'data(label)'
        }
    },
    {
        "selector": '[type = "Branch"]',
        'style': {
            "opacity": 0.9,
            'height': 25,
            'width': 25,
            'shape' : 'octagon',
            'background-color': '#4544ae',
            'content': 'data(label)'
        }
    },
    {
        "selector": '[type = "Commit"]',
        'style': {
            "opacity": 0.9,
            'height': 25,
            'width': 25,
            'shape' : 'circle',
            'background-color': '#4544ae',
            'content': 'data(type)'
        }
    },
    {
        "selector": 'edge',
        'style': {
            "curve-style": "bezier",
            "opacity": 1,
            'width': 3,
            'line-color' : '#fe9803'
        }
    },

]
#UI DROPDOWN MENUS AND CYTOSCAPE
app.layout = html.Div([
    html.Div(className='eight columns', children=[
		html.Div(className='nine columns', children=[
		    dcc.Dropdown(
		        id='dropdown-update-layout',
		        value='grid',
		        clearable=False,
		        style={
		            'height': '6vh',
					'width': '18vh',
		            'display' : 'inline-block'
		        },
		        options=[
		            {'label': name.capitalize(), 'value': name}
		            for name in ['grid', 'random', 'circle', 'cose', 'concentric', 'breadthfirst']
		        ]),
        #DATE INPUT AREA
            dcc.Input(
                id='input-start-date',
                placeholder='Start-date (dd-mm-yyyy)',
                type='text',
		        style={
		            'height': '6vh',
					'width': '18vh',
		            'display' : 'inline-block'
		        },
                value=''
            ),

            dcc.Input(
                id='input-end-date',
                placeholder='End-date (dd-mm-yyyy)',
                type='text',
		        style={
		            'height': '6vh',
					'width': '18vh',
		            'display' : 'inline-block'
		        },
                value=''
            ),
		    dcc.Dropdown(
		        id='dropdown-slider-devs',
                value=devs[0],
		        clearable=False,
		        style={
		            'height': '6vh',
					'width': '18vh',
		            'display' : 'inline-block',
		        },
		        options=[{'label' : i, 'value' : i} for i in devs],

            ),
            dcc.Dropdown(
		        id='dropdown-slider-files',
                value=n_files[0],
		        clearable=False,
		        style={
		            'height': '6vh',
					'width': '18vh',
		            'display' : 'inline-block',
		        },
		        options=[{'label' : i, 'value' : i} for i in n_files],

            ),
            dcc.Dropdown(
                id='dropdown-slider-filetype',
                value=filetypes[0],
                clearable=False,
                style={
                    'height': '6vh',
                    'width': '18vh',
                    'display' : 'inline-block',
                },
                options=[{'label' : i, 'value' : i} for i in filetypes],

            ),

			html.Button('Reset',
						id='reset_button',
						style={
							'width' : '10vh',
							'height' : '6vh',
							'padding-top' : '0px',
							'display' : 'inline-block',
						},
			),
			html.Div( dcc.Markdown('''# **Github Visualization**'''),
				style={'display' : 'inline-block',
						'color': '#4544ae',
						'padding-left': '60px',
						}),
		]),
        cyto.Cytoscape(
            id='cytoscape',
            layout={'name': 'grid'},
            elements=data,
            style={
                'height': '70vh',
                'width': '100%',
                'display': 'inline-block',
            },
          stylesheet=default_stylesheet
        ),

    ]),
    #UI TABS
    html.Div(className='two columns', children=[

        dcc.Tabs(id='tabs', children=[

            dcc.Tab(label='List of active developers', children=[
                html.Div(style=styles['tab'], children=[
                    html.P('Developer name and last activity:'),
                    html.Pre(
                        id='all-developers',

                    ),
                ])
            ]),

            dcc.Tab(label='List of files', children=[
                html.Div(style=styles['tab'], children=[
                    html.P('File names and number of commits: '),
                    html.Pre(
                        id='all-files',

                    ),
                ])
            ]),

        ]),

    ])
])

# Update layout

@app.callback(Output('cytoscape', 'layout'),
              [Input('dropdown-update-layout', 'value')])
def update_layout(layout):
    return {
        'name': layout,
        'animate': True
    }

@app.callback(Output('all-files', 'children'),
              [Input('cytoscape', 'tapNode')])
def displayFiles(data):
    nodes, relations = db.get_all_data(merge=False)
    result = filter.commits_per_file(nodes, relations)
    result2 = []
    entry = ""
    for element in result:
        entry += element
        entry += " : "
        entry += str(result[element])
        entry += "\n"
        result2.append(entry)
        entry = ""

    return result2

@app.callback(Output('cytoscape', 'elements'),
              [Input('input-start-date', 'value'),
                Input('input-end-date', 'value'),
                Input('dropdown-slider-devs', 'value'),
                Input('dropdown-slider-files','value'),
                Input('dropdown-slider-filetype','value')],)
def update_layout2(start_date, end_date, developer, file, filetype):
    xnodes, xrelations = db.get_all_data(merge=False)

    ft = filter.Filter(xnodes, xrelations)

    # #TODO: need to convert developer string to id

    d = None
    f = None
    t = None

    if developer != 'Select developer':
        d = filter.developer_to_id(xnodes, developer)

    if file != 'Select file':
        f = filter.file_to_id(xnodes, file)

    if filetype != 'Select filetype':
        t = filter.filetype_to_id(xnodes, filetype)
        print(t)

    try:
        d1 = datetime.strptime(start_date, '%d-%m-%Y')
        d1 = d1.date()
    except ValueError:
        #to do: output that the input is wrong
        d1 = None
        # print("Wrong input d1")
    try:
        d2 = datetime.strptime(end_date, '%d-%m-%Y')
        d2 = d2.date()
    except ValueError:
        #to do: output that the input is wrong
        d2 = None
        # print("Wrong input d2")

    n, r = ft.filter_handler(d, f, t, d1, d2)

    return n + r

@app.callback(Output('all-developers', 'children'),
              [Input('cytoscape', 'tapNode')])
def displayDevs(data):
	dev = developers.Developers(nodes, relations)
	return dev.print_dev_last(dev.list_dev_ids())


#RESET BUTTON CALLBACKS

@app.callback(Output('dropdown-slider-devs', 'value'),
              [Input('reset_button', 'n_clicks')])
def update_reset(n_clicks):
        return 'Select developer'

@app.callback(Output('dropdown-slider-files', 'value'),
              [Input('reset_button', 'n_clicks')])
def update_reset(n_clicks):
        return 'Select file'

@app.callback(Output('dropdown-slider-filetype', 'value'),
              [Input('reset_button', 'n_clicks')])
def update_reset(n_clicks):
        return 'Select filetype'

@app.callback(Output('input-start-date', 'value'),
              [Input('reset_button', 'n_clicks')])
def update_reset(n_clicks):
        return ''

@app.callback(Output('input-end-date', 'value'),
              [Input('reset_button', 'n_clicks')])
def update_reset(n_clicks):
        return ''

#RESET BUTTON CALLBACKS ^

if __name__ == '__main__':
    app.run_server(debug=True)
