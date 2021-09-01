from django.shortcuts import render
from .models import Data
from django.views.generic import CreateView
from .forms import ContactForm

class ContactCreate(CreateView):
    # Модель куда выполняется сохранение
    model = Data
    # Класс на основе которого будет валидация полей
    form_class = ContactForm
    # Выведем все существующие записи на странице
    contacts = Data.objects.all()
    extra_context = {'contacts': contacts}
    # Шаблон с помощью которого
    # будут выводиться данные
    template_name = 'contact/contact.html'
    # На какую страницу будет перенаправление
    # в случае успешного сохранения формы
    success_url = '/index/'


def lastnamev(request):
    contacts = Data.objects.all()
    return render(request, 'contact/index.html', context={'contacts': contacts})

