from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd
import dash_ag_grid as dag

df = pd.read_csv("../3)combine each new file/pink_morsels.csv")   # change path if yours differs

df["Sales"] = pd.to_numeric( #converts each value to float
    df["Sales"].astype(str) #converts everything in the sales coloumn into a string

      .str.replace("$", "", regex=False), #replaces the dollar symbol with  nothing
    errors="coerce" #passes the "sales"
)


# Initialize the app
app = Dash()

# App layout
app.layout = [
    html.Div(children='Sales Histograms'),
    dag.AgGrid(
        rowData=df.to_dict('records'), columnDefs=[{"field": i} for i in df.columns]
    ),
    dcc.Graph(figure=px.histogram(df, x='date', y='Sales', histfunc='avg'))
]

if __name__ == '__main__':
    app.run(debug=True)
