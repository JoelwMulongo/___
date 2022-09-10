# Django Template

{% extends 'base.html' %}
{% block content %}     {% endblock %} 
{% include 'header.html' %} 
{% if %}   {% else %}   {% endif %} 
{% for x in y %}   {% endfor %} 
{{ var_name }}

#Template variables formating
{{ title | lower }} 
{{ blog.post | truncatwords:50 }}
{{ order.date | date:"D M Y" }}
{{ list_items | slice:":3" }}
{{ total | default:"nil" }}

Current path (ex. posts/1/show)
{{ request.path }}   

URL by name with param
{% url 'posts.delete' id=post.id %}

Use static in template: 
{% load static %}
{% static 'css/main.css' %}