# Generated by Django 4.1.1 on 2022-10-09 10:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='blogs')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='County',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('email', models.EmailField(max_length=254)),
                ('adress', models.CharField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('code', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Farmer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=254)),
                ('second_name', models.CharField(max_length=254)),
                ('age', models.IntegerField(null=True)),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female'), ('other', 'other')], max_length=254)),
                ('email', models.EmailField(max_length=254)),
                ('adress', models.CharField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('county', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='efarm.county')),
            ],
        ),
        migrations.CreateModel(
            name='Produce',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('generic_name', models.CharField(max_length=254)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=7)),
                ('image', models.ImageField(blank=True, null=True, upload_to='produce')),
                ('farmer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='efarm.farmer')),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('date_created', models.DateField(auto_now_add=True, null=True)),
                ('invoice_no', models.AutoField(primary_key=True, serialize=False)),
                ('invoice_id', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('quantity', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('VAT', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_method', models.CharField(choices=[('Cash', 'Cash'), ('Bank', 'Bank'), ('Mpesa', 'Mpesa')], max_length=254)),
                ('status', models.CharField(choices=[('Paid', 'Paid'), ('Not Paid', 'Not Paid')], max_length=254)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='efarm.farmer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='efarm.produce')),
            ],
        ),
        migrations.CreateModel(
            name='CountyAgriOfficer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=254)),
                ('second_name', models.CharField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('county', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='efarm.county')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CentreManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=254)),
                ('second_name', models.CharField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('county', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='efarm.county')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=254)),
                ('second_name', models.CharField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('county', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='efarm.county')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
