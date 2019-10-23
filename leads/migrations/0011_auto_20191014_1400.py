# Generated by Django 2.2.6 on 2019-10-14 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0010_lead_teams'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='lead',
            name='type',
            field=models.CharField(blank=True, choices=[('Supplier', 'Supplier'), ('Customer', 'Customer')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='lead',
            name='products',
            field=models.ManyToManyField(limit_choices_to=5, related_name='company_products', to='leads.Product'),
        ),
    ]
