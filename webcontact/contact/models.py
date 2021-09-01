from django.db import models

class Data(models.Model):
    timewrite = models.DateTimeField(auto_now_add=True, verbose_name='Записано')
    lastname = models.CharField(max_length=50, blank=True, null=True, verbose_name='Фамилия:')
    firstname = models.CharField(max_length=100, blank=True, null=True, verbose_name='Имя (Отчество):')
    address = models.CharField(max_length=300, blank=True, null=True, verbose_name='Адрес:')
    phonenumber = models.CharField(max_length=50, blank=True, null=True, verbose_name='Телефонный номер:')
    email = models.CharField(max_length=100, blank=True, null=True, verbose_name='Электронный адрес:')
    addinform = models.CharField(max_length=500, blank=True, null=True, verbose_name='Дополнительная информация:')
    dt = models.CharField(max_length=50, blank=True, null=True, verbose_name='Дата и время записи контакта:')
    d = models.CharField(max_length=20, blank=True, null=True, verbose_name='Дата записи контакта:')
    url_photo = models.CharField(max_length=100, blank=True, null=True, verbose_name='Ссылка на фото контакта:')
    img = models.ImageField(upload_to='image/', verbose_name='Фотография:')

