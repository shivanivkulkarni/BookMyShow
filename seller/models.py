from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, AbstractUser


class Seller(AbstractUser):
    

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='seller_user_set',  # Change 'custom_user_set' to your preferred name
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='seller_user_set',  # Change 'custom_user_set' to your preferred name
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
    )
    class Meta:
        db_table = 'Seller'  


# class TicketSeller(models.Model):
#     class Meta:
#         db_table = 'TicketSeller'   
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
#     name=models.CharField(max_length=50)
#     # email=models.CharField(max_length=50,unique=True)
#     # password=models.CharField(max_length=60)


# class Show(models.Model):
#     class Meta:
#         db_table = 'Show'   
#     name=models.CharField(max_length=50)
#     city=models.CharField(max_length=50,default='Pune')
#     location=models.CharField(max_length=50)
#     date=models.DateField()
#     time=models.CharField(max_length=50)
#     ticketSeller = models.ForeignKey(TicketSeller, on_delete=models.CASCADE)