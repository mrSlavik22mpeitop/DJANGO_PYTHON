# Generated by Django 3.1.4 on 2020-12-15 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_Date', models.DateField(max_length=50)),
                ('amount', models.CharField(max_length=50)),
                ('customers_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.customer')),
                ('products_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
    ]
