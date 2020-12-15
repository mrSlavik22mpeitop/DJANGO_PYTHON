# Generated by Django 3.1.4 on 2020-12-07 21:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.CharField(max_length=50)),
                ('required_date', models.CharField(max_length=50)),
                ('shipped_date', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
                ('customers_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.customer')),
            ],
        ),
    ]