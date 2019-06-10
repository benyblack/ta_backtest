import unittest
import ta_backtest.chart as chart
import bokeh
import numpy as np


class TestChart(unittest.TestCase):

    def test_datetime(self):
        dates=['2012-02-23', '2012-02-25']
        new_dates = chart.datetime(dates)
        self.assertIsInstance(new_dates[0], np.datetime64)

    def test_create_plot(self):
        title = "Test title"
        plot = chart.create_plot(title)
        print(plot.xaxis)
        self.assertEqual(plot.title.text, title)

    def test_add_line_to_plot(self):
        plot = chart.create_plot("Test")
        data_date = [10,20,30]
        data_close = [1,2,3]
        new_plot = chart.add_line_to_plot(plot, "test title", data_date, data_close, "red")
        
        self.assertEqual(new_plot.renderers[0].data_source.data['x'], data_date)
        self.assertEqual(new_plot.renderers[0].data_source.data['y'], data_close)
        self.assertIsInstance(new_plot.renderers[0].glyph, bokeh.models.glyphs.Line)

    def test_add_up_to_plot(self):
        plot = chart.create_plot("Test")
        data_date = [10,20,30]
        data_close = [1,2,3]
        new_plot = chart.add_up_to_plot(plot, "test title", data_date, data_close, "red")
        
        self.assertEqual(new_plot.renderers[0].data_source.data['x'], data_date)
        self.assertEqual(new_plot.renderers[0].data_source.data['y'], data_close)
        self.assertIsInstance(new_plot.renderers[0].glyph, bokeh.models.glyphs.Triangle)

    def test_add_down_to_plot(self):
        plot = chart.create_plot("Test")
        data_date = [10,20,30]
        data_close = [1,2,3]
        new_plot = chart.add_down_to_plot(plot, "test title", data_date, data_close, "red")
        
        self.assertEqual(new_plot.renderers[0].data_source.data['x'], data_date)
        self.assertEqual(new_plot.renderers[0].data_source.data['y'], data_close)
        self.assertIsInstance(new_plot.renderers[0].glyph, bokeh.models.glyphs.InvertedTriangle)


if __name__ == '__main__':
    unittest.main()