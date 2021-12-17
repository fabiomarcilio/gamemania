from django.shortcuts import render


# def home(request):
#     return render(request, 'core/index.html')

def dashboard(request):
    return render(request, 'base/dashboard.html')
