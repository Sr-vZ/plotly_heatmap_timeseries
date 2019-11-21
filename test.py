import plotly.graph_objects as go
import datetime
import numpy as np
import pandas as pd

np.random.seed(1)

programmers = ['Alex','Nicole','Sara','Etienne','Chelsea','Jody','Marianne']
excel_file = 'signupsbyday.xlsx'
data = pd.read_excel(excel_file)
data = data.sort_values(by='Days in Date')
# print(data['Days in Date'])


base = datetime.datetime.today()
dates = base - np.arange(180) * datetime.timedelta(days=1)
z = np.random.poisson(size=(len(programmers), len(dates))) 


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
mask = (data['Days in Date'] > start_date) & (data['Days in Date'] <= end_date)

data = data.loc[mask]

data['day_of_week'] = data['Days in Date'].dt.weekday_name
data ['weekno'] = data['Days in Date'].dt.week
data['month'] = data['Days in Date'].dt.month
dates = data['Days in Date']
weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
# z = data['Total Leads']

z = []
w = []
for index in data.index:
    w.append(data['Total Leads'][index])
    if index % 7 == 0:
        z.append(w)
        w = []
z = []
w = []
# for index in data.index:
#     if data['day_of_week'][index] == "Monday":
#         w.append(data['Total Leads'][index])
#     elif data['day_of_week'][index] == "Tuesday":
#         w.append(data['Total Leads'][index])
#     elif data['day_of_week'][index] == "Wednesday":
#         w.append(data['Total Leads'][index])
#     elif data['day_of_week'][index] == "Thursday":
#         w.append(data['Total Leads'][index])
#     elif data['day_of_week'][index] == "Friday":
#         w.append(data['Total Leads'][index])
#     elif data['day_of_week'][index] == "Saturday":
#         w.append(data['Total Leads'][index])
#     elif data['day_of_week'][index] == "Sunday":
#         w.append(data['Total Leads'][index])
#         z.append(w)
#         w = []

z = []
w = []
d = []
weekno = []
weekmon = []
subdates = []
text = []
tickmonths = []
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
 






print(data)
print(z)
print(np.transpose(z))
z = np.transpose(z)
# subdates = np.transpose(subdates)
text = np.transpose(text)
# print(text)
print(weekno)
print(weekmon)

tickmonthname = []
months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
for i in range(len(weekno)):
    if i>0 and weekmon[i] != weekmon[i-1]:
        tickmonths.append(weekno[i])
        tickmonthname.append(months[weekmon[i]-1])
    if i==0:
        tickmonths.append(weekno[0])
        tickmonthname.append(months[weekmon[i]-1])

print(tickmonths)
print(tickmonthname)
fig = go.Figure(data=go.Heatmap(
        z=z,
        x=weekno,
        y=weekdays,
        hovertemplate = 'Date: {x,y}',
        colorscale='Viridis'))
        # colorscale ='RdBu'))

# print(weeknumber_of_dates)
# print(weekdays_in_year)
# print(text)
data = [
    go.Heatmap(
        x = weekno,
        y = weekdays,
        # z = data_days,
        z=z,
        text = text,
        # hoverinfo="text",
        hovertemplate='Week: %{x}<br>Day: %{y}<br>Leads: %{z}<br>Date: %{text}<extra></extra>',
        xgap=3, # this
        ygap=3, # and this is used to make the grid-like apperance
        # showscale=False
    )
]
layout = go.Layout(
    # title='Ferielukket Kalender',
    height=600,
    yaxis=dict(
        showline=True, #draw axis option (maybe I should remove this?)
        tickmode="array",
        ticktext= weekdays,
        tickvals=[0,1,2,3,4,5,6],
        gridwidth = 2
        # title="Ugedag"
    ),
    xaxis=dict(
        showline = True,
        # gridwidth = 2,
        tickmode = 'array',
        # tickvals = [1, 3, 5, 7, 9, 11],
        # ticktext = ['One', 'Three', 'Five', 'Seven', 'Nine', 'Eleven']
        ticktext = tickmonthname,
        tickvals= tickmonths,
        # title="Uge Nr."
    ),
    #plot_bgcolor=('rgb(0,0,0)') #making grid appear black
)

fig = go.Figure(data=data, layout=layout)
fig.update_layout(
    title='Total leads per day')
fig.write_html('heatmap.html')
# fig.write_html('heatmap.html', auto_open=True)
# fig.show()