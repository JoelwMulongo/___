#Form (forms.py)

from django import forms
class ArticleForm(forms.Form): 
    name = forms.Charfield(max_length=100)
    description = forms.Charfield(blank=True, null = True)


# Model Form 
from django.forms import ModelForm
from .models import Article
class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['name', 'description', 'price']


# Render form in template
<form method=“post” action=“” novalidate> 
    {% csrf_token %}
    {{ form }} 
    <button type="submit">Submit</button>
</form>

# Bootstrap (pip install django-crispy-forms + installed_apps: 'crispy_forms')
{% load crispy_forms_tags %}
{{ form|crispy }}
{{ form.email|as_crispy_field }}