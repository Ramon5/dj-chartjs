=====
Usage
=====

To use dj-chartjs in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'dj_chartjs',
        ...
    )

Using the RadarChartView:

.. code-block:: python

    from dj_chartjs.views import RadarChartView
    from django.views.generic import TemplateView

    class ExampleView(RadarChartView, TemplateView):

        template_name = "core/example.html"    
        title = "Casos confirmados de coronavírus"

        def generate_labels(self):
            return ["Africa","Brasil","Mexico","Itália","Japão"]

        def generate_values(self):
            dataset = []
            dataset.append(self.create_node("Brasil", [12,8,6,9,64])) # append more nodes if you want
            ....
            return dataset

Use the create_node method to generate object for radar dataset, this method will return an dict for datatype radarchart. The method accept two parameters: label of unit data and dataset list.

To use **LineChartView** is a same method that **RadarChartView** example.

Using the GroupChartView:

.. code-block:: python

    from dj_chartjs.views import GroupChartView
    from django.views.generic import TemplateView

    class ExampleView(GroupChartView, TemplateView):

        template_name = "core/example.html"    
        title = "Casos confirmados de coronavírus"

        def generate_labels(self):
            return ["2017","2018","2019","2020"]

        def generate_values(self):
            dataset = []
            dataset.append(self.create_node("Brasil", [12,8,6,9])) # append more nodes if you want
            dataset.append(self.create_node("Africa", [3,20,6,9]))
            ....
            return dataset

