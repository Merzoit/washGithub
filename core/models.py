from django.db import models
from numpy import blackman

# Create your models here.
class Blank(models.Model):
    #Related fields
    date = models.OneToOneField(
        'Date', db_column='date', on_delete=models.SET_NULL,
        blank=True, null=True, verbose_name="Дата"
        )

    car_class = models.ForeignKey(
        'Car_class', db_column='car_class', on_delete=models.SET_NULL, 
        blank=True, null=True, verbose_name="Класс авто"
        )

    wash_type = models.ForeignKey(
        'Wash_type', db_column='wash_type', on_delete=models.SET_NULL, 
        blank=True, null=True, verbose_name="Тип мойки"
        )

    wash_man = models.ForeignKey(
        'Wash_man', db_column='wash_man', on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Мойщик"
        )

    pay_type = models.ForeignKey(
        'Pay', db_column='pay', on_delete=models.SET_NULL,
        blank=True, null=True, verbose_name="Способ оплаты"
        )

    dry_clining = models.ForeignKey(
        'DryClining', db_column='dry_clining', on_delete=models.SET_NULL,
        blank=True, null=True, verbose_name="Химчистка"
        )
    #Local fields
    time = models.TimeField(
        auto_now=True
        )

    grz = models.CharField(
        max_length=9, blank=True, null=True,
        verbose_name="ГРЗ автомобиля"
        )

    car_mark = models.CharField(
        max_length=32, blank=True, null=True, 
        verbose_name="Марка автомобиля"
        )

    price = models.IntegerField(
        blank=True, null=True, verbose_name="Цена"
        )

    b_trunk = models.BooleanField(
        default=False, verbose_name="Багажник"
        )

    b_carpets = models.BooleanField(
        default=False, verbose_name="Коврики"
        )

    b_cleaning = models.BooleanField(
        default=False, verbose_name="Пылесос"
        )

    b_degreasing = models.BooleanField(
        default=False, verbose_name="Обезжиривание"
        )

    b_black = models.BooleanField(
        default=False, verbose_name="Чернение"
        )

    b_window = models.BooleanField(
        default=False, verbose_name="Стёкла"
        )

    b_rain = models.BooleanField(
        default=False, verbose_name="Анти-дождь"
        )

    b_tinting = models.BooleanField(
        default=False, verbose_name="Тонировка"
        )
    #Химчистка
    dry_clining = models.BooleanField(
        default=False, verbose_name="Химчистка"
        )

    chairs = models.IntegerField(
        blank=True, null=True, verbose_name="Кресло"
        )

    dc_full = models.BooleanField(
        default=False, verbose_name="Полная"
        )

    dc_floor = models.BooleanField(
        default=False, verbose_name="Пол"
        )

    dc_ceiling = models.BooleanField(
        default=False, verbose_name="Потолок"
        )
    ####
    notes = models.TextField(
        max_length=360, blank=True, null=True, 
        verbose_name="Примечания"
        )

    sale = models.IntegerField(
        blank=True, null=True,
        verbose_name="Скидка"
        )

    def __str__(self):
        """ UI админки """
        return self.grz

    class Meta:
        """ Конфигурация класса """
        verbose_name = "Бланк"
        verbose_name_plural = "Бланки"

class Date(models.Model):


    date = models.DateField(verbose_name="Дата")

    def __str__(self):
        """ UI админки """
        return str(self.date)

    class Meta:
        """ Конфигурация класса """
        verbose_name = "Дата"
        verbose_name_plural = "Даты"

class Wash_type(models.Model):


    type = models.CharField(
        max_length=32, blank=True, null=True, verbose_name="Тип"
        )

    def __str__(self):
        """ UI админки """
        return self.type

    class Meta:
        """ Конфигурация класса """
        verbose_name = "Тип мойки"
        verbose_name_plural = "Типы мойки"

class Wash_man(models.Model):


    man = models.CharField(
        max_length=32, blank=True, null=True, verbose_name="Мойщик"
        )

    def __str__(self):
        """ UI админки """
        return self.man

    class Meta:
        """ Конфигурация класса """
        verbose_name = "Мойщик"
        verbose_name_plural = "Мойщики"
        
class Car_class(models.Model):


    car_class = models.CharField(
        max_length=1, blank=True, null=True, verbose_name="Тип"
        )

    def __str__(self):
        """ UI админки """
        return self.car_class

    class Meta:
        """ Конфигурация класса """
        verbose_name = "Класс авто"
        verbose_name_plural = "Классы авто"

class Pay(models.Model):


    pay_type = models.CharField(
        max_length=8, null=True, blank=True, verbose_name="Оплата"
    )

    def __str__(self):
        """ UI админки """
        return self.pay_type

    class Meta:
        """ Конфигурация класса """
        verbose_name = "Способ оплаты"
        verbose_name_plural = "Способы оплаты"
