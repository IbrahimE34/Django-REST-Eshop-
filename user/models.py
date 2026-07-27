


from django.contrib.auth.models import AbstractUser
from django.db import models

class ProductUser(AbstractUser):

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =  ['username']

    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"