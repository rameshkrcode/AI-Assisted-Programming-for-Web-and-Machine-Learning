
from bokeh.plotting import figure, show

p = figure(title="Dynamic Plot")
p.line(x=[1, 2, 3], y=[4, 5, 6])

show(p)
