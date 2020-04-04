import json
import random

'''
    The context factory, instantiate object, passing chart type in constructor.
    define 'title' and 'legend' if you want show in chart. Indicated for construction more than one charts
'''
class ContextFactory:

    BARCHART = "bar"
    PIECHART = "pie"
    DOUGHNUT = "doughnut"
    LINE = "line"
    RADAR = "radar"
    HORIZONTAL = "horizontal"

    title = None
    legend = False

    def __init__(self, type_chart):
        self.type_chart = type_chart

    '''
        Generate context chart
    '''
    def generate_dataset(self, labels, data, unit_label):
        dataset = {}
        options = {}
        if self.type_chart == self.BARCHART or self.type_chart == self.PIECHART or self.type_chart == self.DOUGHNUT:
            dataset = {
                "labels": list(labels),
                "datasets": [{
                    "label": unit_label,
                    "backgroundColor": ["#{:02x}{:02x}{:02x}".format(*map(lambda x: random.randint(0, 255), range(3))) for entry in labels],
                    "data": list(data)
                }]
            }

            options = {
                "responsive": True,
                "maintainAspectRatio": False,
                "legend": {"display": self.legend, "position": 'right' },
                "title": {
                    "fontSize": 14,
                    "display": True if self.title is not None else False,
                    "text": self.title if self.title is not None else ""
                }
            }

        if self.type_chart == self.BARCHART:
            options["scales"] = {
                "yAxes": [{
                    "display": True,
                    "ticks": {
                        "beginAtZero": True
                    }
                }],
            }
        
        if self.type_chart == self.HORIZONTAL:
            options["scales"] = {
                "xAxes": [{
                    "display": True,
                    "ticks": {
                        "beginAtZero": True
                    }
                }],
            }

        return {
            "type": self.type_chart,
            "data": json.dumps(dataset),
            "options": json.dumps(options)
        }