from django.db import models

# Create your models here.
class User(models.Model):
    id = models.BigIntegerField(primary_key=True)
    first_name = models.TextField(blank=True, null=True)
    last_name = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    gender = models.TextField(blank=True, null=True)
    ip_address = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'


class SecondaryConnectionManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().using('secondary')


class UserSecondary(models.Model):
    id = models.BigIntegerField(primary_key=True)
    first_name = models.TextField(blank=True, null=True)
    last_name = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    gender = models.TextField(blank=True, null=True)
    ip_address = models.TextField(blank=True, null=True)

    objects = SecondaryConnectionManager()

    class Meta:
        managed = False
        db_table = 'user'