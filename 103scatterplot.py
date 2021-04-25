import pandas as pd
import plotly.express as px 

df=pd.read_csv('data.csv')
fig=px.scatter_3d(df,x='Population',y='Per capita',size='Percentage',color='Country',size_max=60)
fig.show()