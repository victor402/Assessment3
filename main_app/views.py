from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Widget
from .forms import WidgetForm


# Create your views here.

def home(request):
     widget_form = WidgetForm()
     widgets = Widget.objects.all()
     print(widgets)
     print(widgets.__len__())


     return render(request, 'home.html',{'widget_form': widget_form, 'widgets': widgets})




def add_widget(request):
     print('this is the request')
     print(request.POST)
     if request.method == 'POST':
        form = WidgetForm(request.POST)
        if form.is_valid():
            new_widget = form.save(commit=False)
            new_widget.save()
     else:
        form = WidgetForm()
     return redirect('home')  
             
                

