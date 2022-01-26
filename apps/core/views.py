from django.shortcuts import render
from django.views.generic.base import TemplateView


# def home(request):
#     return render(request, 'core/index.html')

# def dashboard(request):
#     return render(request, 'base/dashboard.html')

class Dashboard(TemplateView):
    template_name = 'base/dashboard.html'
