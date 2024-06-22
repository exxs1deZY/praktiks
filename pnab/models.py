from django.db import models
from django.contrib.auth.hashers import make_password

class User(models.Model):
    name = models.CharField('Имя', max_length=256)
    surname = models.CharField('Фамилия', max_length=256)
    patronymic = models.CharField('Отчество', max_length=256)
    login = models.CharField('Логин', max_length=256)
    email = models.CharField('Почта', max_length=256)
    password = models.CharField('Пароль', max_length=256)
    phone = models.CharField('Телефон', max_length=11)
    role = models.TextField('Роль', choices={('Пользователь', 'Пользователь'), ('Администратор', 'Администратор')})

    def __str__(self):
        return self.email
    
    def save(self, *args, **kwargs):
        new_user = self.pk is None
        if new_user or 'password' in kwargs.get('update_fields', []):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

class Stament(models.Model):
    name = models.CharField('Название', max_length=256)
    number_car = models.CharField('Номер машины', max_length=256)
    text = models.TextField('Описание')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField('Изображение', null=True)
    otvet = models.TextField('Ответ', choices={('Подтверждён', 'Подтверждён'), ('Новый', 'Новый'), ('Отклонён', 'Отклонён')})

    def __str__(self):
        return f"{self.name} написано {self.user}"
