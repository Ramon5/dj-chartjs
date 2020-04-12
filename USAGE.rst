============
Usage
============


Charts as views
---------------

If you want render only one chart, you can inherit ChartViews available. Is required that you define two essential methods: "generate_labels" and "generate_values".

Available BarChartView, PieChartView, DoughnutChartView, RadarChartView, HorizontalBarChartView, PolarAreaChartView, LineChartView, GroupChartView

in views.py import type chart to want use:

.. code-block:: python

    from django.views.generic.base import TemplateView
    from django_charts.views import BarChartView

    class ExampleChart(BarChartView, TemplateView):
        ...
        title = "Index of ..."

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
        aspectRatio = False
        width = 300
        height = 250

        def generate_labels(self):
            return ["Africa","Brazil","Japan","EUA"]

        def generate_values(self):
            return [1,10,15,8]


RadarChartView
~~~~~~~~~~~~~~

To use `RadarChartView` you need create an special node to add dataset. Using 'create_node' method
you can pass 'label', data (list) and optional parameter 'color', if you don't pass color, will be generate random color to node. Use this in generate_values method.

Example below:

.. code-block:: python

    from django.views.generic.base import TemplateView
    from django_charts.views import RadarChartView

    class ExampleChart(RadarChartView, TemplateView):
        ...
        title = "Index of ..."

        def generate_labels(self):
            return ["Africa","Brazil","Japan","EUA"]

        def generate_values(self):
            dataset = []
            nodeOne = self.create_node("Example 1", [15,5,2,50]) #you can create many nodes to view in chart
            ....
            dataset.append(nodeOne)

            return dataset

LineChartView
~~~~~~~~~~~~~

If you want use `LineChartView`, is same method that RadarChartView, 
but have unique difference is the parameter 'fill' that by default is False. 
The linechart too have create_node method to generate special node for chart.


For generate a AreaChart define fill as True on create_node method. 
You too can be pass a color as parameter on this method.

The color must be passed as a string "#606060"

**Example:** self.create_node("Test", [1,2,3,4,5], "#606060")


GroupChartView
~~~~~~~~~~~~~~

Too heve a crete_node method and same method generate of charts above.


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
~~~~~~~~~~~~~~~~~~~~

Here you can be render more than one charts in your template html, just call
instances of charts and define key in context

.. code-block:: python

    from django.views.generic import TemplateView
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


RadarChart
~~~~~~~~~~

For use radar charts as a object in your view, do this:

.. code-block:: python

    from django.views.generic import TemplateView
    from dj_chartjs.charts import RadarChart

    class ExampleView(TemplateView):

        template_name = "core/example.html"

        def my_method(self):
            radarchart = RadarChart()
            radarchart.title = "Example charts title"

            labels = ["test 1","test 2", "test 3", "test 4"]
            data = []
            data.append(self.create_node("Example 1", [5,8,9,64,3])
            data.append(self.create_node("Example 2", [10,1,19,6,13])
            ....

            return radarchart.generate_dataset(labels, data, label)

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context["chart"] = self.my_method()

            return context


LineChart
~~~~~~~~~

.. code-block:: python

    from djanfo.views.generic import TemplateView
    from dj_chartjs.charts import LineChart

    class ExampleView(TemplateView):

        template_name = "core/example.html"

        def my_method(self):
            chart = LineChart()
            chart.title = "Example charts title"

            labels = ["test 1","test 2", "test 3", "test 4"]
            data = []
            data.append(self.create_node("Example 1", [5,8,9,64,3])
            ....

            return chart.generate_dataset(labels, data, label)

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context["chart"] = self.my_method()

            return context


AreaChart
~~~~~~~~~

Just use LineChart and define fill parameter as a True, you can define color to node if you want.

.. code-block:: python

    from djanfo.views.generic import TemplateView
    from dj_chartjs.charts import LineChart

    class ExampleView(TemplateView):

        template_name = "core/example.html"

        def my_method(self):
            chart = LineChart()
            chart.title = "Example charts title"

            labels = ["test 1","test 2", "test 3", "test 4"]
            data = []
            data.append(self.create_node("Example 1", [5,8,9,64,3], True)
            ....

            return chart.generate_dataset(labels, data, label)

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context["chart"] = self.my_method()

            return context


GroupChart
~~~~~~~~~~

The same method that charts above, only difference is the create_node method have a color parameter.
