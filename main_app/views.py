from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Widget
from .forms import WidgetForm


# Create your views here.

def home(request):
     widget_form = WidgetForm()
     
    

     return render(request, 'home.html',{'widget_form': widget_form})




def add_widget(request):
     if request.method == 'POST':
        form = WidgetForm(request.POST)
        if form.is_valid():
            new_widget = form.save(commit=False)
            new_widget.save()
     else:
        form = WidgetForm()
     return redirect('home', {'form': form})  
             
                

# def add_widget(request, widget_id):
#      form = WidgetForm(request.POST)
#      if form.is_valid():
#           new_widget = form.save(commit=False)
#           new_widget.save()
#      return redirect('home', widget_id=widget_id)     
            
          

#     #  {'widget':widget, 'widget_form': widget_form}
