# Generated by Django 4.1.7 on 2023-04-10 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Profileapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('transaction_id', models.AutoField(primary_key=True, serialize=False)),
                ('item', models.CharField(max_length=255)),
                ('price_paid', models.DecimalField(decimal_places=2, max_digits=10)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Profileapp.profile')),
            ],
        ),
    ]
