# Generated by Django 2.2.6 on 2019-10-15 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0011_auto_20191014_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='products',
            field=models.ManyToManyField(blank=True, limit_choices_to=5, null=True, related_name='company_products', to='leads.Product'),
        ),
    ]