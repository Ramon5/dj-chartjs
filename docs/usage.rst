=====
Usage
=====

To use django-charts in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_charts.apps.DjangoChartsConfig',
        ...
    )

Add django-charts's URL patterns:

.. code-block:: python

    from django_charts import urls as django_charts_urls


    urlpatterns = [
        ...
        url(r'^', include(django_charts_urls)),
        ...
    ]
