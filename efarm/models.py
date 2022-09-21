from django.db import models
import uuid
from django.contrib.auth.models import User


class Farmer(models.Model):
    gender_choice = (
        ('male', 'male',),
        ('female', 'female'),
        ('other', 'other')
    )
    name = models.CharField(max_length=254)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    age = models.IntegerField(null=True)
    gender = models.CharField(max_length=254, choices=gender_choice)
    email = models.EmailField()
    adress = models.CharField(max_length=254)
    phone = models.IntegerField()
    county = models.CharField(max_length=254)
    town = models.CharField(max_length=254)

    def __str__(self):
        return self.first_name

    @property
    def get_name(self):
        full_name = self.first_name + ' ' + self.second_name

        return full_name




class County(models.Model):
    name = models.CharField(max_length=254)
    email = models.EmailField()
    adress = models.CharField(max_length=254)
    phone = models.IntegerField()
    code = models.IntegerField(null=False, max_length=4)

    def __str__(self):
        return self.name
    
class CentreManager(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=254)
    email = models.EmailField()
    staff = models.BooleanField(default=False) # a admin user; non super-user


    def __str__(self):
        return self.name
    
class CountyAgriOfficer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=254)
    email = models.EmailField()
    admin = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Produce(models.Model):
    name = models.CharField(max_length=254)
    generic_name = models.CharField(max_length=254)
    price = models.DecimalField(decimal_places=2, max_digits=7)
    quantity = models.DecimalField(decimal_places=2, max_digits=7)
    image = models.ImageField(upload_to='images', null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Invoice(models.Model):
    status_options = (
        ('Paid', 'Paid'),
        ('Not Paid', 'Not Paid'),
    )
    payment_choices = (
        ('Cash', 'Cash'),
        ('Bank', 'Bank'),
        ('Mpesa', 'Mpesa'),
    )

    customer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    date_created = models.DateField(auto_created=True, null=True)
    invoice_no = models.AutoField(primary_key=True)
    invoice_id = models.UUIDField(default=uuid.uuid4, editable=False)
    product = models.ForeignKey(Produce, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    discount = models.DecimalField(decimal_places=2, max_digits=10)
    VAT = models.DecimalField(decimal_places=2, max_digits=10)
    Total = models.DecimalField(decimal_places=2, max_digits=10)
    payment_method = models.CharField(max_length=254, choices=payment_choices)
    status = models.CharField(max_length=254, choices=status_options)

