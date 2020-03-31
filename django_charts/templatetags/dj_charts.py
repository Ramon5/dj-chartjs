from django import template

register = template.Library()

@register.inclusion_tag("django_charts/chart.html", takes_context=True)
def load_chart(context,values):
    chart = {
        "dataChart": values,
        "id_chart": context["id"],
        "type_chart": context["type"]
    }
    return chart