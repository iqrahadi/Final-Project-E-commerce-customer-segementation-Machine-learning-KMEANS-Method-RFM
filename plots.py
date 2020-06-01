import plotly 
import plotly.express as px
from cleaning_data import data_retail3
import json

def pairplot():
    df =data_retail3()
    fig = px.scatter_matrix(df,dimensions=['Recency','Frequency','Monetary'])
    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json

def distribution_r():
    df = data_retail3()
    fig = px.histogram(df, x='Recency', hover_data=df.columns)
    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json

def distribution_f():
    df = data_retail3()
    fig = px.histogram(df, x='Frequency', hover_data=df.columns)
    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json

def distribution_m():
    df = data_retail3()
    fig = px.histogram(df, x='Monetary', hover_data=df.columns)
    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json