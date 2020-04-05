from django import template
import json

register = template.Library()

@register.filter
def parse(texte):   
    return json.loads(texte)