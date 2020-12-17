import dash_bootstrap_components as dbc
import dash
import dash_core_components as dcc

app = dash.Dash(
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)

app.layout = dbc.Container([
    dbc.Alert("Hello Bootstrap!", color="success"),
    dcc.Slider(id="Q1",marks ={
        0: '0 °F',
        3: '3 °F',
        5: '5 °F',
        7.65: '7.65 °F',
        10: '10 °F'
    }, ),
]
)

if __name__ == "__main__":
    app.run_server(debug=True,port=8080)