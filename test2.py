import datetime
import plotly.graph_objs as go
import numpy as np

def holidays():
	year = datetime.datetime.now().year

	d1 = datetime.date(year, 1, 1)
	d2 = datetime.date(year, 12, 31)

	delta = d2 - d1

	dates_in_year = [d1 + datetime.timedelta(i) for i in range(delta.days+1)] #gives me a list with datetimes for each day a year
	weekdays_in_year = [i.weekday() for i in dates_in_year] #gives [0,1,2,3,4,5,6,0,1,2,3,4,5,6,...] (ticktext in xaxis dict translates this to weekdays
	weeknumber_of_dates = [int(i.strftime("%V")) for i in dates_in_year] #gives [1,1,1,1,1,1,1,2,2,2,2,2,2,2,...] name is self-explanatory
	z = np.random.uniform(low=0.0, high=1.0, size=(len(dates_in_year,))) #random numbers to give some mad colorz
	text = [str(i) for i in dates_in_year] #gives something like list of strings like '2018-01-25' for each date. Used in data trace to make good hovertext.

	data = [
		go.Heatmap(
			x = weekdays_in_year,
			y = weeknumber_of_dates,
			# z = data_days,
            z=z,
			text=text,
			hoverinfo="text",
			xgap=3, # this
			ygap=3, # and this is used to make the grid-like apperance
			showscale=False
		)
	]
	layout = go.Layout(
		title='Ferielukket Kalender',
		height=1000,
		xaxis=dict(
			showline=True, #draw axis option (maybe I should remove this?)
			tickmode="array",
			ticktext=["Man", "Tirs", "Ons", "Tors", "Fre", "Lør", "Søn"],
			tickvals=[0,1,2,3,4,5,6],
			title="Ugedag"
		),
		yaxis=dict(
			showline=True,
			title="Uge Nr."
		),
		plot_bgcolor=('rgb(0,0,0)') #making grid appear black
	)

	fig = go.Figure(data=data, layout=layout)
	return fig

fig = holidays()
fig.write_html('heatmap2.html')