import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.express as px


def create_histogram_with_boxplot(df, x):
    """
    Create a Plotly figure containing a histogram and a box plot for a specified column in a DataFrame.
    Parameters:
    - df (pd.DataFrame): The DataFrame containing the data.
    - x (str): The name of the column to plot.

    Returns:
    - fig (go.Figure): Plotly figure containing the histogram and box plot.
    """
    fig = make_subplots(rows=2, cols=1)
    fig.add_trace(go.Histogram(x=df[x], name='Histogram'), row=1, col=1)
    fig.add_trace(go.Box(x=df[x], name="Box"), row=2, col=1)
    fig.update_layout(
        title=f'Distribution of {x}',
        height=600,
    )
    return fig


def create_pie_chart(df, cat):
    """
    Create a Plotly pie chart for the distribution of categories in a specified column of a DataFrame.

    Parameters:
    - df (pd.DataFrame): The DataFrame containing the data.
    - cat (str): The name of the categorical column to plot.

    Returns:
    - fig (px.pie): Plotly pie chart.
    """
    fig = px.pie(names=df[cat], hole=0.3, title=f"Distribution of {cat}")
    fig.update_traces(textinfo='percent+label')
    fig.update_layout(height=800)  # Adjust height and width as desired
    return fig


def plot_histogram(df, cat):
    """
    Generate a histogram plot for a specific category in the DataFrame.

    Args:
    - df: DataFrame containing the data
    - cat: Name of the category

    Returns:
    - fig: Plotly figure object
    """
    fig = px.histogram(df, x=cat, color='income', barmode='group', text_auto='.2f')
    fig.update_layout(title = f"{cat} vs income")
    return fig