import dash
from dash import html, dash_table
import pandas as pd
import os

# Sample data
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [24, 30, 22],
    'City': ['New York', 'Paris', 'London']
}
df = pd.DataFrame(data)

# Create app
app = dash.Dash(__name__)

# Layout
app.layout = html.Div([
    html.H2("Simple Table Example"),
    dash_table.DataTable(
        data=df.to_dict('records'),
        columns=[{"name": i, "id": i} for i in df.columns],
        style_table={'width': '50%', 'margin': 'auto'},
        style_cell={'textAlign': 'center'}
    )
])

# Get the port from environment variable for Render
port = os.environ.get('PORT', 8080)

# Run the app
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(port), debug=True)
