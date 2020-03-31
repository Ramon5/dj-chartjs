import json
import abc
import random
from django_charts.entity import RadarNode

class BaseChart:

    id_chart = None
    type_chart = None
    title = None
    enable_legend = False
    

    @abc.abstractmethod
    def generate_values(self):
        pass

    @abc.abstractmethod
    def generate_options(self):
        return {}
    
    @abc.abstractmethod
    def generate_labels(self):
        return []

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        if self.id_chart:
            context["dataChart"] = { "data": self._generate_data(), "options": self.generate_options()}
            context["type"] = self.type_chart
            context["id"] = self.id_chart
        return context


class BarChart(BaseChart):
    label = ""
    type_chart = "bar"

    def _generate_data(self):
        data = {
            "labels": self.generate_labels(),
            "datasets": self._generate_dataset(self.generate_values())
        }
        return json.dumps(data)

    def generate_options(self):
        options = {
            "legend": { "display": self.enable_legend },
            "title": {
                "display": True if self.title is not None else False,
                "text": self.title
            }
        }
        return json.dumps(options)
        
    
    def _generate_dataset(self,values):
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

class RadarChart:
    id_chart = None
    type_chart = "radar"
    title = None

    def generate_labels(self):
        return []

    '''
        Create RadarNodes object and add to datasets list
    '''
    def generate_values(self):
        return []


    def _get_data(self):        
        return json.dumps({
            "labels": self.generate_labels(),
            "datasets": self.generate_nodes() 
        })

    def generate_options(self):
        options = {
            "title": {
                "display": True if self.title is not None else False,
                "text": self.title
            }
        }
        return json.dumps(options)

    '''
        Generate random rgba colors
    '''
    def get_color(self):
        return "rgba({},{},{},0.2)".format(
            *map(lambda x: random.randint(0, 255), range(5))
        )


    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)               
        if self.id_chart:
            context["type"] = self.type_chart
            context["id"] = self.id_chart
            context["dataChart"] = {"data": self._get_data(), "options": self.generate_options()}
        return context


class HorizontalBarChart(BarChart):
    type_chart = "horizontalBar"


class PolarAreaChart(BarChart):
    type_chart = "polarArea"


class PieChart(BarChart):
    type_chart = "pie"


class DoughnutChart(PieChart):
    type_chart = "doughnut"

    
