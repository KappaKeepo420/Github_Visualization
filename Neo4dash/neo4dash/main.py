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
import developer as dev

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
n, r = filter.filter_by_year(nodes, relations, 2018)
data = n + r
db.dev_last_active('37')
print (len(n))
print (len(r))

styles = {
    'json-output': {
        'overflow-y': 'scroll',
        'height': 'calc(50% - 25px)',
        'border': 'thin lightgrey solid',
    },
    'tab': {'height': 'calc(98vh - 115px)'}
}

app.layout = html.Div([
    html.Div(className='eight columns', children=[
		html.Div(className='nine columns', children=[
		    dcc.Dropdown(
		        id='dropdown-update-layout',
		        value='grid',
		        clearable=False,
		        style={
		            'height': '6vh',
					'width': '30vh',
		            'display' : 'inline-block'
		        },
		        options=[
		            {'label': name.capitalize(), 'value': name}
		            for name in ['grid', 'random', 'circle', 'cose', 'concentric']
		        ]),
		    dcc.Dropdown(
		        id='dropdown-slider-day',
		        value='Select day',
		        clearable=False,
		        style={
		            'height': '6vh',
					'width': '30vh',
		            'display' : 'inline-block',
		        },
		        options=[
		            {'label': name.capitalize(), 'value': name}
		            for name in ['Select day', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22',
									'23', '24', '25', '26', '27', '28', '29', '30', '31']
		        ]),
		    dcc.Dropdown(
		        id='dropdown-slider-month',
		        value='Select month',
		        clearable=False,
		        style={
		            'height': '6vh',
					'width': '30vh',
		            'display' : 'inline-block'
		        },
		        options=[
		            {'label': name.capitalize(), 'value': name}
		            for name in ['Select month', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
		        ]),
		    dcc.Dropdown(
		        id='dropdown-slider-year',
		        value='Select year',
		        clearable=False,
		        style={
		            'height': '6vh',
					'width': '30vh',
		            'display' : 'inline-block'
		        },
		        options=[
		            {'label': name.capitalize(), 'value': name}
		            for name in ['Select year', '2017', '2018', '2019']
		        ]),
			html.Div( dcc.Markdown('''# **Github Visualization**'''),
				style={'display' : 'inline-block',
						'color': '#4544ae',
						'padding-left': '100px',
						}),
		]),
        cyto.Cytoscape(
            id='cytoscape',
            layout={'name': 'grid'},
            elements=data,
            style={
                'height': '80vh',
                'width': '100%',
            },
        )
    ]),

    html.Div(className='four columns', children=[
        dcc.Tabs(id='tabs', children=[
            dcc.Tab(label='Tap Objects', children=[
                html.Div(style=styles['tab'], children=[
                    html.P('Node Object JSON:'),
                    html.Pre(
                        id='tap-node-json-output',
                        style=styles['json-output']
                    ),
                    html.P('Edge Object JSON:'),
                    html.Pre(
                        id='tap-edge-json-output',
                        style=styles['json-output']
                    )
                ])
            ]),

            dcc.Tab(label='Developer Information', children=[
                html.Div(style=styles['tab'], children=[
                    html.P('Developer name:'),
                    html.Pre(
                        id='developer-output'
                    ),
                ])
            ]),

            dcc.Tab(label='List of active developers', children=[
                html.Div(style=styles['tab'], children=[
                    html.P('Developer name and last activity:'),
                ])
            ]),


            dcc.Tab(label='Tap Data', children=[
                html.Div(style=styles['tab'], children=[
                    html.P('Node Data JSON:'),
                    html.Pre(
                        id='tap-node-data-json-output',
                        style=styles['json-output']
                    ),
                    html.P('Edge Data JSON:'),
                    html.Pre(
                        id='tap-edge-data-json-output',
                        style=styles['json-output']
                    )
                ])
            ]),
            dcc.Tab(label='Mouseover Data', children=[
                html.Div(style=styles['tab'], children=[
                    html.P('Node Data JSON:'),
                    html.Pre(
                        id='mouseover-node-data-json-output',
                        style=styles['json-output']
                    ),
                    html.P('Edge Data JSON:'),
                    html.Pre(
                        id='mouseover-edge-data-json-output',
                        style=styles['json-output']
                    )
                ])
            ]),
            dcc.Tab(label='Selected Data', children=[
                html.Div(style=styles['tab'], children=[
                    html.P('Node Data JSON:'),
                    html.Pre(
                        id='selected-node-data-json-output',
                        style=styles['json-output']
                    ),
                    html.P('Edge Data JSON:'),
                    html.Pre(
                        id='selected-edge-data-json-output',
                        style=styles['json-output']
                    )
                ])
            ])
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


@app.callback(Output('tap-node-json-output', 'children'),
              [Input('cytoscape', 'tapNode')])
def displayTapNode(data):
    return json.dumps(data, indent=2)


#TO-DO: Show developer name
'''
@app.callback(Output('developer-output', 'children'),
              [Input('cytoscape', 'tapNode')])
def displayDeveloper(data):
	if data['data']['type'] == 'Developer':
		#return data['data']['Id']
		return 'jawel'
	else:
		pass
'''

@app.callback(Output('tap-edge-json-output', 'children'),
              [Input('cytoscape', 'tapEdge')])
def displayTapEdge(data):
    return json.dumps(data, indent=2)


@app.callback(Output('tap-node-data-json-output', 'children'),
              [Input('cytoscape', 'tapNodeData')])
def displayTapNodeData(data):
    return json.dumps(data, indent=2)


@app.callback(Output('tap-edge-data-json-output', 'children'),
              [Input('cytoscape', 'tapEdgeData')])
def displayTapEdgeData(data):
    return json.dumps(data, indent=2)


@app.callback(Output('mouseover-node-data-json-output', 'children'),
              [Input('cytoscape', 'mouseoverNodeData')])
def displayMouseoverNodeData(data):
    return json.dumps(data, indent=2)


@app.callback(Output('mouseover-edge-data-json-output', 'children'),
              [Input('cytoscape', 'mouseoverEdgeData')])
def displayMouseoverEdgeData(data):
    return json.dumps(data, indent=2)


@app.callback(Output('selected-node-data-json-output', 'children'),
              [Input('cytoscape', 'selectedNodeData')])
def displaySelectedNodeData(data):
    return json.dumps(data, indent=2)


@app.callback(Output('selected-edge-data-json-output', 'children'),
              [Input('cytoscape', 'selectedEdgeData')])
def displaySelectedEdgeData(data):
    return json.dumps(data, indent=2)


if __name__ == '__main__':
    app.run_server(debug=True)
