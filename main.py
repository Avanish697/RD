import dash
from dash import html, dash_table  # ✅ Updated import
import pandas as pd

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

# Run app
if __name__ == '__main__':
    app.run_server(debug=True)
