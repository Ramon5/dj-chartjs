============
Usage
============


Charts as views
---------------

If you want render only one chart, you can inherit ChartViews available

Available BarChartView, PieChartView, DoughnutChartView, RadarChartView, HorizontalBarChartView, PolarAreaChartView

in views.py import type chart to want use:

.. code-block:: python

    from django.views.generic.base import TemplateView
    from django_charts.views import BarChartView

    class ExampleChart(BarChartView, TemplateView):
        ...
        title = "Index of ..."
        id_chart = "barchart_example" #any value

        def generate_labels(self):
            return ["Africa","Brazil","Japan","EUA"]

        def generate_values(self):
            return [1,10,15,8]

**in your template that you want render chart, use this tag:**

.. code-block:: html

    {% load dj_chartjs %}
    <html>
    <head></head>
    <body>

    {% render_chart chart %}

    </body>
    </html>


**Options to charts views (below default values)**

.. code-block:: python

    title = ""
    legend = False
    beginAtZero = False
    aspectRatio = True
    width = 100
    height = 100

If you want resize the chart, just define width an height properties and set aspectRatio as False:

.. code-block:: python

    from django.views.generic.base import TemplateView
    from django_charts.views import BarChartView

    class ExampleChart(BarChartView, TemplateView):
        ...
        title = "Index of ..."
        id_chart = "barchart_example" #any value
        aspectRatio = False
        width = 300
        height = 250

        def generate_labels(self):
            return ["Africa","Brazil","Japan","EUA"]

        def generate_values(self):
            return [1,10,15,8]




Charts as objects
-----------------

in your views.py:

.. code-block:: python

    from django.views.generic import TemplateView
    from dj_chartjs.charts import BarChart

    class ExampleView(TemplateView):

        template_name = "core/example.html"

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            barchart = BarChart()
            barchart.title = "Example charts title"

            labels = ["test 1","test 2", "test 3", "test 4"]
            data = [2,3,10,6]
            label = "Test"

            context["chart"] = barchart.generate_dataset(labels, data, label)
            return context

**And in your "example.html" template use this:**

.. code-block:: html

    <canvas id="mychart"></canvas>

**on script section:**

.. code-block:: javascript

    $(function(){
        new Chart(document.getElementById("mychart"), {
            type: "{{ chart.type }}",
            data: {{ chart.data|safe }},
            options: {{ chart.options|safe }}
        });
    })

**You can be use chart object in any function in your views.py, for example:**

.. code-block:: python

    class ExampleView(TemplateView):

        template_name = "core/example.html"

        def my_method(self):
            barchart = BarChart()
            barchart.title = "Example charts title"

            labels = ["test 1","test 2", "test 3", "test 4"]
            data = [2,3,10,6]
            label = "Test"

            return barchart.generate_dataset(labels, data, label)

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context["chart"] = self.my_method() #any key in context

            return context


The charts available in package is: BarChart, PieChart, HorizontalBarChart, DoughnutChart, PolarAreaChart, RadarChart, LineChart, GroupChart

It's possible define options to object chart, for example:

| barchart.title = "..."
| barchart.legend = True


Many charts by views
--------------------

Here you can be render more than one charts in your template html, just call
instances of charts and define key in context

.. code-block:: python

    from dj_chartjs.charts import BarChart, PieChart

    class ExampleView(TemplateView):

        template_name = "core/example.html"

        def my_barchart(self):
            barchart = BarChart()
            barchart.title = "Example charts title"

            labels = ["test 1","test 2", "test 3", "test 4"]
            data = [2,3,10,6]
            label = "Test"

            return barchart.generate_dataset(labels, data, label)

        def my_piechart(self):
            piechart = PieChart()
            piechart.title = "Example charts title"

            labels = ["test 1","test 2", "test 3", "test 4"]
            data = [2,3,10,6]
            label = "Test"

            return piechart.generate_dataset(labels, data, label)


        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context["barchart"] = self.my_barchart()
            context["piechart"] = self.my_piechart()

            return context

**In your template body:**

Example using bootstrap:

.. code-block:: html

    <div class="row">
        <div class="col-6">
            <canvas id="mybarchart"></canvas>
        </div>
        <div class="col-6">
            <canvas id="mypiechart"></canvas>
        </div>
    </div>

and section scripts:

.. code-block:: javascript

    $(function(){
        new Chart(document.getElementById("mybarchart"), {
            type: "{{ barchart.type }}",
            data: {{ barchart.data|safe }},
            options: {{ barchart.options|safe }}
        });

        new Chart(document.getElementById("mypiechart"), {
            type: "{{ piechart.type }}",
            data: {{ piechart.data|safe }},
            options: {{ piechart.options|safe }}
        });
    });