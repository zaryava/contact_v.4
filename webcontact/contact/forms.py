from .models import Data
from django.forms import ModelForm


class ContactForm(ModelForm):

    class Meta:
        model = Data # Название модели Data на основе
                     # которой создается форма.

        # Выбираю следующие поля все модели Data
        # для отображения в форме.
        fields = ['lastname', 'firstname', 'address', 'phonenumber',
                  'email', 'addinform', 'img']