 
# Project URLS 
# Create all auth routes
from django.contrib.auth.views import LoginView, LogoutView
from posts.views import SignupView

# Include all auth routes
path('account/', include('django.contrib.auth.urls')),

# Some example of auth routes
# path('account/login/', LoginView.as_view(), name='login'),
# path('account/logout/', LogoutView.as_view(), name='logout'),
# path('account/signup/', SignupView.as_view(), name='signup'),

# Views
# LoginView and LogoutView already exist in django.contrib.auth.views
# custom SignupView:
class SignupView(generic.CreateView):
    template_name = 'registration/signup.html'
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse("login")

# Forms
# Login form already exist
# Custom signup form:
from django.contrib.auth.forms import UserCreationForm, UsernameField

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}

# settings.py 
LOGIN_REDIRECT_URL = '/posts'
LOGIN_URL = '/login'

# templates
# registration/login.html
{% extends "base.html" %}
{% block content %}
    <form method="post">
        {% csrf_token %}
        {{ form }}
        <button type="submit">Login</button>
    </form>
{% endblock content %}

# registration/signup.html
{% extends "base.html" %}
{% block content %}
    <form method="post">
        {% csrf_token %}
        {{ form }}
        <button type="submit">Signup</button>
    </form>
{% endblock content %}

# Authentication links
<a href="{% url 'login' %}">Login</a>
<a href="{% url 'signup' %}">Signup</a>
<a href="{% url 'logout' %}">Logout</a>

# Auth in template
{% if request.user.is_authenticated %}
    Logged in as: {{ request.user.username }}
{% endif %}

# Restrict views to auth user only
# views.py
from django.contrib.auth.mixins import LoginRequiredMixin

class PostsCreateView(LoginRequiredMixin, generic.CreateView):
   ...
   ...

# Function base view auth
def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            log_user(request, user)
            return redirect("index")

return render(request, "registration/login.html", {})