import plotly.graph_objects as go
import datetime
import numpy as np
import pandas as pd

np.random.seed(1)

programmers = ['Alex','Nicole','Sara','Etienne','Chelsea','Jody','Marianne']
excel_file = 'signupsbyday.xlsx'
data = pd.read_excel(excel_file)

# print(data['Days in Date'])


base = datetime.datetime.today()
dates = base - np.arange(180) * datetime.timedelta(days=1)
z = np.random.poisson(size=(len(programmers), len(dates))) 


data['day_of_week'] = data['Days in Date'].dt.weekday_name

dates = data['Days in Date']
weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
z = data['Total Leads']

z = []
w = []
for index in data.index:
    w.append(data['Total Leads'][index])
    if index % 7 == 0:
        z.append(w)
        w = []
    

print(data.head())
print(z)
fig = go.Figure(data=go.Heatmap(
        z=z,
        x=dates,
        y=weekdays,
        colorscale='Viridis'))

fig.update_layout(
    title='GitHub commits per day',
    xaxis_nticks=36)
# fig.write_html('heatmap.html')
fig.write_html('heatmap.html', auto_open=True)
# fig.show()