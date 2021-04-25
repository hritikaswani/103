import pandas as pd
import plotly.express as px

df=pd.read_csv('line_chart.csv')
# line chart
fig=px.line(df,x='Year',y='Per capita income',color='Country',title='Per Capita Income')
fig.show()