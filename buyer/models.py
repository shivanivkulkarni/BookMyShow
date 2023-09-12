from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Customer(models.Model):
    class Meta:
        db_table = 'Customer' 
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    people=models.IntegerField()
    price=models.IntegerField()


class Buyer(AbstractUser):

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='buyer_user_set',  # Change 'custom_user_set' to your preferred name
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='buyer_user_set',  # Change 'custom_user_set' to your preferred name
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
    )


    class Meta:
        db_table = 'Buyer'  
