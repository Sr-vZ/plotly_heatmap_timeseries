# import plotly.graph_objects as go
import plotly as plotly
import plotly.plotly as py
from plotly import graph_objs as go
from plotly import tools
import plotly.figure_factory as ff

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
mask = (data['Days in Date'] >= start_date) & (data['Days in Date'] <= end_date)

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
w = ['','','','','','','']
# w = [0,0,0,0,0,0,0]
d = []
weekno = []
weekmon = []
subdates = []
text = []
tickmonths = []

last3months = data['month'].unique()
# data = data[data['month']==9]
print(len(data['day_of_week']))
print(data['weekno'].unique())
print(data['Days in Date'].iat[-1])


def get_heatmap_data(monthdata,monthname):
    data = monthdata
    w = ['','','','','','','']
    w_text = ['','','','','','','']
    d = ['','','','','','','']
    z = []
    z_text = []
    text = []
    weekno = []
    weekmon = []
    weeknonormalized = []
    i=1
    for index in data.index:       
        if data['day_of_week'][index] == "Sunday":
            # d.append(data['Days in Date'][index].strftime('%m-%d-%Y'))
            d[6] = data['Days in Date'][index].strftime('%m-%d-%Y')
            w[6] = data['Total Leads'][index]
            w_text[6] = data['Days in Date'][index].strftime('%d')
            z_text.append(w_text)
            z.append(w)
            # w = [0,0,0,0,0,0,0]
            w = ['','','','','','','']
            weekno.append(data['weekno'][index])
            weekmon.append(data['month'][index])
            weeknonormalized.append(i)
            subdates.append(d)        
            text.append(d)
            d = ['','','','','','','']
            i=i+1
        elif data['day_of_week'][index] == "Monday":
            w[0] = data['Total Leads'][index]
            d[0] = data['Days in Date'][index].strftime('%m-%d-%Y')
            w_text[0] = data['Days in Date'][index].strftime('%d')
            if data['Days in Date'][index] == data['Days in Date'].iat[-1]:
                z.append(w)
                text.append(d)
                z_text.append(w_text)
                weekno.append(data['weekno'][index])
                weekmon.append(data['month'][index])
                weeknonormalized.append(i)
        elif data['day_of_week'][index] == "Tuesday":
            w[1] = data['Total Leads'][index]
            d[1] = data['Days in Date'][index].strftime('%m-%d-%Y')
            w_text[1] = data['Days in Date'][index].strftime('%d')
            if data['Days in Date'][index] == data['Days in Date'].iat[-1]:
                z.append(w)
                text.append(d)
                z_text.append(w_text)
                weekno.append(data['weekno'][index])
                weekmon.append(data['month'][index])
                weeknonormalized.append(i)
        elif data['day_of_week'][index] == "Wednesday":
            w[2] = data['Total Leads'][index]
            d[2] = data['Days in Date'][index].strftime('%m-%d-%Y')
            w_text[2] = data['Days in Date'][index].strftime('%d')
            if data['Days in Date'][index] == data['Days in Date'].iat[-1]:
                z.append(w)
                text.append(d)
                z_text.append(w_text)
                weekno.append(data['weekno'][index])
                weekmon.append(data['month'][index])
                weeknonormalized.append(i)
        elif data['day_of_week'][index] == "Thursday":
            w[3] = data['Total Leads'][index]
            d[3] = data['Days in Date'][index].strftime('%m-%d-%Y')
            w_text[3] = data['Days in Date'][index].strftime('%d')
            if data['Days in Date'][index] == data['Days in Date'].iat[-1]:
                z.append(w)
                text.append(d)
                z_text.append(w_text)
                weekno.append(data['weekno'][index])
                weekmon.append(data['month'][index])
                weeknonormalized.append(i)
        elif data['day_of_week'][index] == "Friday":
            w[4] = data['Total Leads'][index]
            d[4] = data['Days in Date'][index].strftime('%m-%d-%Y')
            w_text[4] = data['Days in Date'][index].strftime('%d')
            if data['Days in Date'][index] == data['Days in Date'].iat[-1]:
                z.append(w)
                text.append(d)
                z_text.append(w_text)
                weekno.append(data['weekno'][index])
                weekmon.append(data['month'][index])
                weeknonormalized.append(i)
        elif data['day_of_week'][index] == "Saturday":
            w[5] = data['Total Leads'][index]
            d[5] = data['Days in Date'][index].strftime('%m-%d-%Y')
            w_text[5] = data['Days in Date'][index].strftime('%d')
            if data['Days in Date'][index] == data['Days in Date'].iat[-1]:
                text.append(d)
                z.append(w)
                z_text.append(w_text)
                weekno.append(data['weekno'][index])
                weekmon.append(data['month'][index])
                weeknonormalized.append(i)
    # z = z[::-1]
    # text = text[::-1]
    weekno = weekno[::-1]
    weeknonormalized = weeknonormalized[::-1]
    print(z)
    print(text)
    print(weekno)
    # trace = ff.create_annotated_heatmap(
    trace = go.Heatmap(
        z=z,
        x=weekdays,
        y=weeknonormalized,
        colorscale='Viridis',
        text = text,
        # textposition='center',
        # annotation_text=z_text,
        name = monthname,
        # type = 'heatmap',
        # hoverinfo="text",
        # hovertemplate='Week: %{x}<br>Day: %{y}<br>Leads: %{z}<br>Date: %{text}<extra></extra>',
        xgap=3, # this
        ygap=3, # and this is used to make the grid-like apperance
    )
    # annotations = go.Annotations()
    # a = go.Annotations()
    # for n, row in enumerate(z):
    #     for m, val in enumerate(row):
    #         annotations.append(go.Annotation(text=str(z_text[n][m]), x=weekdays[m], y=weekno[n],xref='x1', yref='y1', showarrow=False))
            # a.append(go.Annotation(text=str(z_text[n][m]), x=weekdays[m], y=weekno[n],xref='x1', yref='y1', showarrow=False))
        # annotations.append(a)
    return trace


def get_ff_heatmap_data(monthdata,monthname):
    data = monthdata
    w = [0,0,0,0,0,0,0]
    # w = ['','','','','','','']
    w_text = ['','','','','','','']
    d = ['','','','','','','']
    z = []
    z_text = []
    text = []
    weekno = []
    weeknonormalized = []
    weekmon = []
    i=1
    for index in data.index:       
        if data['day_of_week'][index] == "Sunday":
            # d.append(data['Days in Date'][index].strftime('%m-%d-%Y'))
            d[6] = data['Days in Date'][index].strftime('%m-%d-%Y')
            w[6] = data['Total Leads'][index]
            w_text[6] = data['Days in Date'][index].strftime('%d')
            z_text.append(w_text)
            z.append(w)
            w = [0,0,0,0,0,0,0]
            # w = ['','','','','','','']
            weekno.append(data['weekno'][index])
            weekmon.append(data['month'][index])
            weeknonormalized.append(i)
            subdates.append(d)        
            text.append(d)
            d = ['','','','','','','']
            i=i+1
        elif data['day_of_week'][index] == "Monday":
            w[0] = data['Total Leads'][index]
            d[0] = data['Days in Date'][index].strftime('%m-%d-%Y')
            w_text[0] = data['Days in Date'][index].strftime('%d')
            if data['Days in Date'][index] == data['Days in Date'].iat[-1]:
                z.append(w)
                text.append(d)
                z_text.append(w_text)
                weekno.append(data['weekno'][index])
                weekmon.append(data['month'][index])
                weeknonormalized.append(i)
        elif data['day_of_week'][index] == "Tuesday":
            w[1] = data['Total Leads'][index]
            d[1] = data['Days in Date'][index].strftime('%m-%d-%Y')
            w_text[1] = data['Days in Date'][index].strftime('%d')
            if data['Days in Date'][index] == data['Days in Date'].iat[-1]:
                z.append(w)
                text.append(d)
                z_text.append(w_text)
                weekno.append(data['weekno'][index])
                weekmon.append(data['month'][index])
                weeknonormalized.append(i)
        elif data['day_of_week'][index] == "Wednesday":
            w[2] = data['Total Leads'][index]
            d[2] = data['Days in Date'][index].strftime('%m-%d-%Y')
            w_text[2] = data['Days in Date'][index].strftime('%d')
            if data['Days in Date'][index] == data['Days in Date'].iat[-1]:
                z.append(w)
                text.append(d)
                z_text.append(w_text)
                weekno.append(data['weekno'][index])
                weekmon.append(data['month'][index])
                weeknonormalized.append(i)
        elif data['day_of_week'][index] == "Thursday":
            w[3] = data['Total Leads'][index]
            d[3] = data['Days in Date'][index].strftime('%m-%d-%Y')
            w_text[3] = data['Days in Date'][index].strftime('%d')
            if data['Days in Date'][index] == data['Days in Date'].iat[-1]:
                z.append(w)
                text.append(d)
                z_text.append(w_text)
                weekno.append(data['weekno'][index])
                weekmon.append(data['month'][index])
                weeknonormalized.append(i)
        elif data['day_of_week'][index] == "Friday":
            w[4] = data['Total Leads'][index]
            d[4] = data['Days in Date'][index].strftime('%m-%d-%Y')
            w_text[4] = data['Days in Date'][index].strftime('%d')
            if data['Days in Date'][index] == data['Days in Date'].iat[-1]:
                z.append(w)
                text.append(d)
                z_text.append(w_text)
                weekno.append(data['weekno'][index])
                weekmon.append(data['month'][index])
                weeknonormalized.append(i)
        elif data['day_of_week'][index] == "Saturday":
            w[5] = data['Total Leads'][index]
            d[5] = data['Days in Date'][index].strftime('%m-%d-%Y')
            w_text[5] = data['Days in Date'][index].strftime('%d')
            if data['Days in Date'][index] == data['Days in Date'].iat[-1]:
                text.append(d)
                z.append(w)
                z_text.append(w_text)
                weekno.append(data['weekno'][index])
                weekmon.append(data['month'][index])
                weeknonormalized.append(i)
    # z = z[::-1]
    # text = text[::-1]
    weekno = weekno[::-1]
    print(z)
    print(z_text)
    print(text)
    print(weekno)
    trace = ff.create_annotated_heatmap(
    # trace = go.Heatmap(
        z=z,
        x=weekdays,
        y=weekno,
        colorscale='Viridis',
        text = text,
        # textposition='center',
        annotation_text=z_text,
        zmin=1,
        name = monthname,
        # type = 'heatmap',
        # hoverinfo="text",
        # hovertemplate='Week: %{x}<br>Day: %{y}<br>Leads: %{z}<br>Date: %{text}<extra></extra>',
        xgap=3, # this
        ygap=3, # and this is used to make the grid-like apperance
    )
    return trace



months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
trace = []
anno = []
plotTitle = []
for m in last3months:
    t = get_heatmap_data(data[data['month']==m],months[m])
    # t = get_ff_heatmap_data(data[data['month']==m],months[m])
    trace.append(t)
    # anno.append(a)
    plotTitle.append(months[m-1])

print(plotTitle)
print(len(anno))
# print(data['Days in Date'].dt.day)
i = 0
# for index in data.index:
#     i=i+1
#     if data['day_of_week'][index] == "Sunday":
#         d.append(data['Days in Date'][index].strftime('%m-%d-%Y'))
#         w[6] = data['Total Leads'][index]
#         z.append(w)
#         # w = [0,0,0,0,0,0,0]
#         w = ['','','','','','','']
#         weekno.append(data['weekno'][index])
#         weekmon.append(data['month'][index])
#         subdates.append(d)        
#         text.append(d)
#         d = []
#     elif data['day_of_week'][index] == "Monday":
#         w[0] = data['Total Leads'][index]
#         d.append(data['Days in Date'][index].strftime('%m-%d-%Y'))
#     elif data['day_of_week'][index] == "Tuesday":
#         w[1] = data['Total Leads'][index]
#         d.append(data['Days in Date'][index].strftime('%m-%d-%Y'))
#     elif data['day_of_week'][index] == "Wednesday":
#         w[2] = data['Total Leads'][index]
#         d.append(data['Days in Date'][index].strftime('%m-%d-%Y'))
#     elif data['day_of_week'][index] == "Thursday":
#         w[3] = data['Total Leads'][index]
#         d.append(data['Days in Date'][index].strftime('%m-%d-%Y'))
#     elif data['day_of_week'][index] == "Friday":
#         w[4] = data['Total Leads'][index]
#         d.append(data['Days in Date'][index].strftime('%m-%d-%Y'))
#     elif data['day_of_week'][index] == "Saturday":
#         w[5] = data['Total Leads'][index]
#         d.append(data['Days in Date'][index].strftime('%m-%d-%Y'))
#     elif data['Days in Date'][index] == data['Days in Date'].iat[-1]:
#         z.append(w)

# weekdays_list =['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
# for index in data.index:
#     i=i+1        
#     if data['day_of_week'][index] == "Sunday":
#         d.append(data['Days in Date'][index].strftime('%m-%d-%Y'))
#         w[6] = data['Total Leads'][index]
#         z.append(w)
#         # w = [0,0,0,0,0,0,0]
#         w = ['','','','','','','']
#         weekno.append(data['weekno'][index])
#         weekmon.append(data['month'][index])
#         subdates.append(d)        
#         text.append(d)
#         d = []
#     elif data['day_of_week'][index] == "Monday":
#         w[0] = data['Total Leads'][index]
#         d.append(data['Days in Date'][index].strftime('%m-%d-%Y'))
#         if data['Days in Date'][index] == data['Days in Date'].iat[-1]:
#             z.append(w)
#     elif data['day_of_week'][index] == "Tuesday":
#         w[1] = data['Total Leads'][index]
#         d.append(data['Days in Date'][index].strftime('%m-%d-%Y'))
#         if data['Days in Date'][index] == data['Days in Date'].iat[-1]:
#             z.append(w)
#     elif data['day_of_week'][index] == "Wednesday":
#         w[2] = data['Total Leads'][index]
#         d.append(data['Days in Date'][index].strftime('%m-%d-%Y'))
#         if data['Days in Date'][index] == data['Days in Date'].iat[-1]:
#             z.append(w)
#     elif data['day_of_week'][index] == "Thursday":
#         w[3] = data['Total Leads'][index]
#         d.append(data['Days in Date'][index].strftime('%m-%d-%Y'))
#         if data['Days in Date'][index] == data['Days in Date'].iat[-1]:
#             z.append(w)
#     elif data['day_of_week'][index] == "Friday":
#         w[4] = data['Total Leads'][index]
#         d.append(data['Days in Date'][index].strftime('%m-%d-%Y'))
#         if data['Days in Date'][index] == data['Days in Date'].iat[-1]:
#             z.append(w)
#     elif data['day_of_week'][index] == "Saturday":
#         w[5] = data['Total Leads'][index]
#         d.append(data['Days in Date'][index].strftime('%m-%d-%Y'))
#         if data['Days in Date'][index] == data['Days in Date'].iat[-1]:
#             z.append(w)
    # elif weekdays_list.index(data['day_of_week'][index]):
    #     w[weekdays_list.index(data['day_of_week'][index])-1] = data['Total Leads'][index]
    #     d.append(data['Days in Date'][index].strftime('%m-%d-%Y'))
    #     if data['Days in Date'][index] == data['Days in Date'].iat[-1]:
    #         z.append(w)

    # for week in data['weekno'].unique():
    #     z.append(w)
    #     w = [0,0,0,0,0,0,0]
    #     weekno.append(data['weekno'][index])
    #     weekmon.append(data['month'][index])
    #     subdates.append(d)        
    #     text.append(d)
    #     d = []


# for index in data.index:
#     if data['day_of_week'][index] == "Sunday":
#         d.append(data['Days in Date'][index].strftime('%m-%d-%Y'))
#         w[6] = data['Total Leads'][index]
#         z.append(w)
#         subdates.append(d)
#         w = [0,0,0,0,0,0,0]
#         text.append(d)
#         weekno.append(data['weekno'][index])
#         weekmon.append(data['month'][index])
#         d = []
#     elif data['day_of_week'][index] == "Monday":
#         w[0] = data['Total Leads'][index]
#         d.append(data['Days in Date'][index].strftime('%m-%d-%Y'))
#     elif data['day_of_week'][index] == "Tuesday":
#         w[1] = data['Total Leads'][index]
#         d.append(data['Days in Date'][index].strftime('%m-%d-%Y'))
#     elif data['day_of_week'][index] == "Wednesday":
#         w[2] = data['Total Leads'][index]
#         d.append(data['Days in Date'][index].strftime('%m-%d-%Y'))
#     elif data['day_of_week'][index] == "Thursday":
#         w[3] = data['Total Leads'][index]
#         d.append(data['Days in Date'][index].strftime('%m-%d-%Y'))
#     elif data['day_of_week'][index] == "Friday":
#         w[4] = data['Total Leads'][index]
#         d.append(data['Days in Date'][index].strftime('%m-%d-%Y'))
#     elif data['day_of_week'][index] == "Saturday":
#         w[5] = data['Total Leads'][index]
#         d.append(data['Days in Date'][index].strftime('%m-%d-%Y'))

# transforming flat data to 2d Array
# for index in data.index:
#     if data['day_of_week'][index] == "Sunday":
#         d.append(data['Days in Date'][index].strftime('%m-%d-%Y'))
#         w.append(data['Total Leads'][index])
#         z.append(w)
#         subdates.append(d)
#         w = []
#         text.append(d)
#         weekno.append(data['weekno'][index])
#         weekmon.append(data['month'][index])
#         d = []
#     else:
#         w.append(data['Total Leads'][index])
#         d.append(data['Days in Date'][index].strftime('%m-%d-%Y'))

# print(data)
# print(z)
# print(np.transpose(z))
# z = np.transpose(z)
# text = np.transpose(text)
# print(text)
# print(weekno)
# print(weekmon)

# z = z[::-1]
# tickmonthname = []

# for i in range(len(weekno)):
#     if i>0 and weekmon[i] != weekmon[i-1]:
#         tickmonths.append(weekno[i])
#         tickmonthname.append(months[weekmon[i]-1])
#     if i==0:
#         tickmonths.append(weekno[0])
#         tickmonthname.append(months[weekmon[i]-1])

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
# layout = go.Layout(
#     height=600,
#     yaxis=dict(
#         showline=True,
#         tickmode="array",
#         ticktext= weekdays,
#         tickvals=[0,1,2,3,4,5,6],
#         gridwidth = 2,
#         # title="Weekdays"
#     ),
#     xaxis=dict(
#         showline = True,
#         gridwidth = 2,
#         tickmode = 'array',
#         # ticktext = tickmonthname,
#         # tickvals= tickmonths,
#         # title="Months"
#     ),
# )


# data = [
#     go.Heatmap(
#         z=z,
#         x=weekdays,
#         y=weekno,
#         colorscale='Viridis',
#         text = text,
#         # type = 'heatmap',
#         # hoverinfo="text",
#         # hovertemplate='Week: %{x}<br>Day: %{y}<br>Leads: %{z}<br>Date: %{text}<extra></extra>',
#         xgap=3, # this
#         ygap=3, # and this is used to make the grid-like apperance
#     )
# ]

# layout = go.Layout(
#     title='total leads',
#     xaxis = dict(ticks='', nticks=36),
#     yaxis = dict(ticks='' )
# )



# data = trace
# print(anno[0])
# fig = tools.make_subplots(rows=3, cols=1, subplot_titles=('Plot 1', 'Plot 2','Plot 3'))
fig = tools.make_subplots(rows=3, cols=1, subplot_titles=plotTitle)
i=1
for t in trace:
    fig.append_trace(t,i,1)
    fig['layout']['yaxis'+str(i)].update(showticklabels=False)
    # fig['layout'].update(annotations)
    i=i+1
# fig = go.Figure()
# fig.add_traces([fig1.data[0], fig2.data[0]])
# i=1
# print(trace[0].data[0])
# fig.add_trace(trace[0].data[0])
# fig.add_traces([trace[0].data,trace[1].data,trace[2].data])
# for t in trace:
#     fig.add_traces(t)
#     fig['layout']['yaxis'+str(i)].update(showticklabels=False)
#     # fig['layout'].update(annotations)
#     i=i+1
# print(fig)
# fig.update_layout(
#     yaxis1 = dict(showticklabels=False),
#     yaxis2 = dict(showticklabels=False),
#     yaxis3 = dict(showticklabels=False)
# )


# fig = go.Figure(data=data, layout=layout)
plotly.offline.plot(fig, filename='datetime-heatmap')
# py.iplot(fig, filename='datetime-heatmap')
# fig.show(renderer="png", width=800, height=300)


# fig = go.Figure(data=data, layout=layout)
# fig.update_layout(
#     title='Total leads per day')
# fig.write_html('heatmap.html')
# fig.write_html('heatmap.html', auto_open=True)
# fig.show()



