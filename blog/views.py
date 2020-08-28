from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Post

# Create your views here.

class HomePageView(ListView):
    template_name = 'home.html'
    model = Post


# class SnacksPageView(ListView):
#     template_name = 'snacks.html'
#     model = Snack


# class SnackDetailPageView(DetailView):
#     template_name = 'snacks_detail.html'
#     model = Snack
