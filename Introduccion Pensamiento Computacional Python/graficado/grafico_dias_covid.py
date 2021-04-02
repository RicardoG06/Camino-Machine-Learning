from bokeh.io import output_file, show
from bokeh.plotting import figure
from bokeh.palettes import Spectral7
from bokeh.models import ColumnDataSource


output_file("1stgraph.html")

dates = ['12 May', '13 May', '14 May', '15 May', '16 May', '17 May', '18 May']
confirmed = [85631, 88412, 96443, 103677, 90688, 82488, 89148]

source = ColumnDataSource(data=dict(dates=dates, confirmed=confirmed, color=Spectral7))

p = figure(x_range=dates, y_range=(0, 150000), plot_height=500, title="Confirmados Globales por Día", toolbar_location=None, tools="")
p.left[0].formatter.use_scientific = False

p.vbar(x='dates', top='confirmed', width=0.8, color='color', legend_field="dates", source=source)

p.xgrid.grid_line_color = None
p.legend.orientation = "horizontal"
p.legend.location = "top_center"
p.y_range.start = 0

show(p)