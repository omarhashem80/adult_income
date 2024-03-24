import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.express as px


df = pd.read_csv('./adult.csv')
cats = df.select_dtypes(include='O').columns.to_list()
nums = df.select_dtypes(include='number').columns.to_list()
nums.remove('income')
cats.append('income')
nums.remove('education-num')
