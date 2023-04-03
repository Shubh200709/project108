import pandas as pd
import plotly.figure_factory as ff

data = pd.read_csv('data.csv')
avg = data['Avg Rating'].tolist()
frame = ff.create_distplot([avg],['Average Rating'])
frame.show()