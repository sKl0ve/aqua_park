from django.shortcuts import render
from django.http import HttpResponse
from .forms import TicketsForm
# Create your views here.

def index(request):
    data = {
        'title':'Главная страница',
    }
    return render(request, "main/index.html", data)


def about(request):
    return render(request, "main/about.html")


def contact(request):
    return render(request, "main/contact.html")


def tickets(request):
    message = ''
    if request.method == 'POST':
        form = TicketsForm(request.POST)
        if form.is_valid():
            form.save()
            message = "Вы успешно зарезерверовали билеты, c вами свяжется наш менеджер."
        else:
            message = "Форма была заполнена не верно"
    
    form = TicketsForm()
    
    data = {
        'form':form,
        'message':message
    }
    
    return render(request, "main/tickets.html", data)