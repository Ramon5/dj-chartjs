import json
import random
from abc import ABC, abstractmethod

from django.shortcuts import render


class BaseChartView(ABC):

    type_chart = None
    title = None
    legend = False
    beginAtZero = False
    aspectRatio = True
    width = 100
    height = 100

    @abstractmethod
    def generate_values(self):
        pass

    def generate_options(self):
        options = {
            "legend": {"display": self.legend},
            "title": {
                "display": True if self.title is not None else False,
                "text": self.title,
            },
        }
        return options

    @abstractmethod
    def generate_labels(self):
        pass

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["chart"] = {
            "data": self._generate_data(),
            "options": self.generate_options(),
        }
        context["type"] = self.type_chart
        if self.aspectRatio is not True:
            context["width"] = self.width
            context["height"] = self.height

        return context


class BarChartView(BaseChartView):
    label = ""
    type_chart = "bar"

    def _generate_data(self):
        data = {
            "labels": self.generate_labels(),
            "datasets": self._generate_dataset(self.generate_values()),
        }
        return json.dumps(data)

    def generate_options(self):
        options = super().generate_options()
        options["scales"] = {
            "yAxes": [{"display": True, "ticks": {"beginAtZero": True}}]
        }

        """options["tooltips"] = {
            "callbacks": { 
                "label": json.dumps("function(tooltipItem,data){ var dataset = data.datasets[tooltipItem.datasetIndex]; return dataset; }")
            }
        }"""

        return json.dumps(options)

    def _generate_dataset(self, values):
        collection = []
        dataset = {
            "label": self.label,
            "backgroundColor": [self._get_color() for entry in self.generate_labels()],
            "data": values,
        }
        collection.append(dataset)
        return collection

    def _get_color(self):
        return "#{:02x}{:02x}{:02x}".format(
            *map(lambda x: random.randint(0, 255), range(3))
        )


class RadarChartView(BaseChartView):

    type_chart = "radar"

    def generate_labels(self):
        return []

    """
        Create RadarNodes object and add to datasets list
    """

    def generate_values(self):
        return []

    def create_node(self, label, data):
        color = self._get_color()
        return {
            "label": label,
            "fill": True,
            "backgroundColor": color,
            "borderColor": color,
            "pointBorderColor": "#fff",
            "pointBackgroundColor": color,
            "data": list(data),
        }

    def _get_color(self):
        return "rgba({},{},{},0.4)".format(
            *map(lambda x: random.randint(0, 255), range(5))
        )

    def _generate_data(self):
        return json.dumps(
            {"labels": self.generate_labels(), "datasets": self.generate_values()}
        )

    def generate_options(self):
        options = super().generate_options()
        return json.dumps(options)

    """
        Generate random rgba colors
    """

    def _get_color(self):
        return "rgba({},{},{},0.4)".format(
            *map(lambda x: random.randint(0, 255), range(5))
        )


class LineChartView(BaseChartView):

    type_chart = "line"

    """
        the params accept `label` string, and `data` list of values (numeric)
        fill is False to default
    """

    def create_node(self, label, data, fill=False):
        color = self._get_color()
        return {
            "data": list(data),
            "label": label,
            "borderColor": color,
            "backgroundColor": color,
            "fill": fill,
        }

    def generate_options(self):
        options = super().generate_options()
        options["scales"] = {
            "yAxes": [
                {
                    "display": True,
                    "ticks": {"beginAtZero": self.beginAtZero, "stepSize": 1},
                }
            ]
        }
        return json.dumps(options)

    def _get_color(self):
        return "rgba({},{},{},0.4)".format(
            *map(lambda x: random.randint(0, 255), range(5))
        )

    def _generate_data(self):
        return json.dumps(
            {"labels": self.generate_labels(), "datasets": self.generate_values()}
        )


class GroupChartView(BaseChartView):

    type_bar = "bar"

    def create_node(self, data, label):
        return {
            "label": label,
            "backgroundColor": "#{:02x}{:02x}{:02x}".format(
                *map(lambda x: random.randint(0, 255), range(3))
            ),
            "data": list(data),
        }

    def _generate_data(self):
        return json.dumps(
            {"labels": self.generate_labels(), "datasets": self.generate_values()}
        )


class HorizontalBarChartView(BarChartView):
    type_chart = "horizontalBar"


class PolarAreaChartView(BarChartView):
    type_chart = "polarArea"


class PieChartView(BarChartView):
    type_chart = "pie"

    def generate_options(self):
        options = {
            "legend": {"display": self.legend, "position": "right"},
            "title": {
                "display": True if self.title is not None else False,
                "text": self.title,
            },
        }

        return json.dumps(options)

    def get_legend_text(self):
        return ""

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["legend"] = self.get_legend_text()
        return context


class DoughnutChartView(PieChartView):
    type_chart = "doughnut"
