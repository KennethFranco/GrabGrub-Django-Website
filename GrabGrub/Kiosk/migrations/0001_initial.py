# Generated by Django 3.1.6 on 2021-05-29 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=300)),
                ('password', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=300)),
                ('customer_address', models.CharField(max_length=300)),
                ('customer_city', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(max_length=300)),
                ('food_description', models.CharField(max_length=300)),
                ('food_price', models.FloatField(blank=True, default=None, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.FloatField(blank=True, default=None, null=True)),
                ('ordered_at', models.DateTimeField(blank=True, null=True)),
                ('payment_mode', models.CharField(choices=[('cash', 'Cash'), ('card', 'Card')], max_length=300)),
                ('cust_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Kiosk.customer')),
                ('order_food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Kiosk.food')),
            ],
        ),
    ]