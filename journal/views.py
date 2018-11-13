import datetime
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy


# Create your views here.

def home(request):

    return render(request, 'journal/home.html')