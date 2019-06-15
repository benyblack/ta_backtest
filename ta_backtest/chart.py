import numpy as np
from bokeh.layouts import column
from bokeh.plotting import figure, show, output_file
# imports for the example
# import random
# from bokeh.sampledata.stocks import AAPL, GOOG, IBM, MSFT


def datetime(x):
    return np.array(x, dtype=np.datetime64)


def create_plot(chart_title):
    plot = figure(x_axis_type="datetime", title=chart_title, plot_height=500, width=1000)
    plot.grid.grid_line_alpha = 0.3
    plot.xaxis.axis_label = 'Date'
    plot.yaxis.axis_label = 'Price'
    return plot


def create_plot_oscillator(related_plot):
    plot = figure(x_axis_type="datetime", x_range=related_plot.x_range, plot_height=150, width=1000)
    plot.grid.grid_line_alpha = 0.3
    plot.xaxis.axis_label = 'Date'
    plot.yaxis.axis_label = 'Value'
    return plot


def create_plot_trades(related_plot):
    plot = figure(x_axis_type="datetime", x_range=related_plot.x_range, plot_height=150, width=1000)
    plot.grid.grid_line_alpha = 0.3
    plot.xaxis.axis_label = 'Date'
    plot.yaxis.axis_label = 'Price'
    return plot


def add_line_to_plot(plot, data_title, data_date, data_close, color):
    plot.line(datetime(data_date), data_close, color=color, legend=data_title)
    return plot


def add_line_to_plot_with_yrange(plot, data_title, data_date, data_close, color, y_range_name):
    plot.line(datetime(data_date), data_close, color=color, legend=data_title, y_range_name=y_range_name)
    return plot


def add_up_to_plot(plot, data_title, data_date, data_close, color="green"):
    plot.triangle(x=datetime(data_date), y=data_close, color=color, legend=data_title)
    return plot


def add_down_to_plot(plot, data_title, data_date, data_close, color="red"):
    plot.inverted_triangle(x=datetime(data_date), y=data_close,
                           color=color, legend=data_title)
    return plot


def show_plot(plot, oscillator, trades):
    plot.legend.location = "top_left"
    oscillator.legend.location = "top_left"
    trades.legend.location = "top_left"
    output_file("chart.html", title=plot.title.text)
    show(column(children=[plot, oscillator, trades]))


# Example of how to use this code
# plot = create_plot("My chart title")
# new_plot = add_line_to_plot(plot, "APPL", datetime(
#     AAPL['date']), AAPL['adj_close'], '#33A02C')
# new_plot = add_up_to_plot(plot, "GOOG", datetime(GOOG['date']), GOOG['adj_close'])
# new_plot = add_down_to_plot(plot, "MSFT", datetime(MSFT['date']), MSFT['adj_close'])

# oscillator = create_plot_oscillator(new_plot)
# indicator = []
# for x in IBM['adj_close']:
#     indicator.append(random.random()*100)

# add_line_to_plot(oscillator, "IBM", datetime(IBM['date']), indicator, 'blue')
# show_plot(new_plot, oscillator)
