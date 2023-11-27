from django.contrib import messages
from django.shortcuts import render

def example_view(request):
    return render(request, 'mi_template.html')

