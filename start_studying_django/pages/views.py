from os import terminal_size
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView , ListView
from .models import Post

class homePageView(TemplateView):
    template_name ="home.html"
class AboutPageView(TemplateView):
    template_name = "about.html"

class BasePageView(ListView):
    model = Post
    template_name = "registration.html"
    context_object_name = 'all_posts_list'