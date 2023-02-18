# from jinja2 import Environment, PackageLoader, select_autoescape
# env = Environment(
#     loader=PackageLoader("yourapp"),
#     autoescape=select_autoescape()
# )

# import pandas as pd
# import matplotlib.pyplot as plt
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

data = pd.read_csv('Data/Stocks/a.us.txt')

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

# testing displaying open through all time for the stock with abb: "a"

fig2 = px.bar(data, x="Date", y="Open", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Stonks'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig2
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)

app = Dash(__name__)

# def imp(path_to_file):
#     # importing dataset

#     f = open(path_to_file,'r')
#     data = f.readlines()


#     f.close()

#     return data

# if __name__ == "__main__":
#     file = "Data/Stocks/a.us.txt"
#     data = imp(file)

#     labels = data[0][:-1] # to get rid of newline

#     info = data[1:]

#     labels = labels.split(",")

#     print(labels)