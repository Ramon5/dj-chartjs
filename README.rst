=============================
django-charts
=============================

Documentation
-------------

The full documentation is at https://django-charts.readthedocs.io/en/latest/

Quickstart
----------

Install django-charts::

    pip install dj-charts

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_charts',
        ...
    )

How to render chart:

in views.py import type chart to want use:

.. code-block:: python

    from django.views.generic.base import TemplateView
    from django_charts.charts import BarChart

    class ExampleChart(BarChart, TemplateView):
        ...
        title = "Index of ..."
        id_chart = "barchart_example" #any value

        def generate_labels(self):
            return ["Africa","Brazil","Japan","EUA"]

        def generate_values(self):
            return [1,10,15,8]

in your template that you want render chart:

{% load dj_charts %}

<canvas id="{{ id }}"></canvas>

in extra javascript block
{% load_chart dataChart %}


Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
