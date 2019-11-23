# import plotly.graph_objects as go
import plotly as plotly
import plotly.plotly as py
from plotly import graph_objs as go

import datetime
import numpy as np
import pandas as pd

np.random.seed(1)

excel_file = 'signupsbyday.xlsx'
data = pd.read_excel(excel_file)
data = data.sort_values(by='Days in Date')
# print(data['Days in Date'])


base = datetime.datetime.today()
dates = base - np.arange(180) * datetime.timedelta(days=1)


year = datetime.datetime.now().year

d1 = datetime.date(year, 1, 1)
d2 = datetime.date(year, 12, 31)

delta = d2 - d1

dates_in_year = [d1 + datetime.timedelta(i) for i in range(delta.days+1)] #gives me a list with datetimes for each day a year
weekdays_in_year = [i.weekday() for i in dates_in_year] #gives [0,1,2,3,4,5,6,0,1,2,3,4,5,6,...] (ticktext in xaxis dict translates this to weekdays
weeknumber_of_dates = [int(i.strftime("%V")) for i in dates_in_year] #gives [1,1,1,1,1,1,1,2,2,2,2,2,2,2,...] name is self-explanatory
z = np.random.uniform(low=0.0, high=1.0, size=(len(dates_in_year,))) #random numbers to give some mad colorz
text = [str(i) for i in dates_in_year] #gives something like list of strings like '2018-01-25' for each date. Used in data trace to make good hovertext.


end_date = data['Days in Date'].max()
start_date = end_date - pd.offsets.MonthBegin(3)

# flitering data based on latest date on the dataset and 3 months back
mask = (data['Days in Date'] > start_date) & (data['Days in Date'] <= end_date)

data = data.loc[mask]

data['day_of_week'] = data['Days in Date'].dt.weekday_name
data ['weekno'] = data['Days in Date'].dt.week
data['month'] = data['Days in Date'].dt.month
dates = data['Days in Date']
weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
# z = data['Total Leads']

# z = []
# w = []
# for index in data.index:
#     w.append(data['Total Leads'][index])
#     if index % 7 == 0:
#         z.append(w)
#         w = []
z = []
w = []
z = []
w = []
d = []
weekno = []
weekmon = []
subdates = []
text = []
tickmonths = []
# transforming flat data to 2d Array
for index in data.index:
    if data['day_of_week'][index] == "Sunday":
        d.append(data['Days in Date'][index].strftime('%m-%d-%Y'))
        w.append(data['Total Leads'][index])
        z.append(w)
        subdates.append(d)
        w = []
        text.append(d)
        weekno.append(data['weekno'][index])
        weekmon.append(data['month'][index])
        d = []
    else:
        w.append(data['Total Leads'][index])
        d.append(data['Days in Date'][index].strftime('%m-%d-%Y'))

# print(data)
# print(z)
# print(np.transpose(z))
z = np.transpose(z)
text = np.transpose(text)
# print(text)
# print(weekno)
# print(weekmon)

tickmonthname = []
months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
for i in range(len(weekno)):
    if i>0 and weekmon[i] != weekmon[i-1]:
        tickmonths.append(weekno[i])
        tickmonthname.append(months[weekmon[i]-1])
    if i==0:
        tickmonths.append(weekno[0])
        tickmonthname.append(months[weekmon[i]-1])

# print(tickmonths)
# print(tickmonthname)

# trace = go.Heatmap(z=[[1, 20, 30, 50, 1], [20, 1, 60, 80, 30], [30, 60, 1, -10, 20]],
#                    x=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
#                    y=['Morning', 'Afternoon', 'Evening'])
# data=[trace]
# py.iplot(data, filename='labelled-heatmap')


# fig = go.Figure(data=go.Heatmap(
#         z=z,
#         x=weekno,
#         y=weekdays,
#         # hovertemplate = 'Date: {x,y}',
#         colorscale='Viridis'))
        # colorscale ='RdBu'))
# data = [
#     go.Heatmap(
#         x = weekno,
#         y = weekdays,
#         z=z,
#         text = text,
#         type = 'heatmap',
#         # hoverinfo="text",
#         # hovertemplate='Week: %{x}<br>Day: %{y}<br>Leads: %{z}<br>Date: %{text}<extra></extra>',
#         # xgap=3, # this
#         # ygap=3, # and this is used to make the grid-like apperance
#     )
# ]
layout = go.Layout(
    height=600,
    yaxis=dict(
        showline=True,
        tickmode="array",
        ticktext= weekdays,
        tickvals=[0,1,2,3,4,5,6],
        gridwidth = 2,
        # title="Weekdays"
    ),
    xaxis=dict(
        showline = True,
        gridwidth = 2,
        tickmode = 'array',
        ticktext = tickmonthname,
        tickvals= tickmonths,
        # title="Months"
    ),
)

data = [
    go.Heatmap(
        z=z,
        x=weekno,
        y=weekdays,
        colorscale='Viridis',
        text = text,
        # type = 'heatmap',
        # hoverinfo="text",
        # hovertemplate='Week: %{x}<br>Day: %{y}<br>Leads: %{z}<br>Date: %{text}<extra></extra>',
        xgap=3, # this
        ygap=3, # and this is used to make the grid-like apperance
    )
]

# layout = go.Layout(
#     title='total leads',
#     xaxis = dict(ticks='', nticks=36),
#     yaxis = dict(ticks='' )
# )


fig = go.Figure(data=data, layout=layout)
plotly.offline.plot(fig, filename='datetime-heatmap')
# py.iplot(fig, filename='datetime-heatmap')
# fig.show(renderer="png", width=800, height=300)


# fig = go.Figure(data=data, layout=layout)
# fig.update_layout(
#     title='Total leads per day')
# fig.write_html('heatmap.html')
# fig.write_html('heatmap.html', auto_open=True)
# fig.show()