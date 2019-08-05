# Generated by Django 2.2.2 on 2019-07-21 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchaser_name', models.CharField(max_length=30)),
                ('purchaser_address', models.TextField()),
                ('gstin_no', models.IntegerField()),
                ('description', models.CharField(max_length=25)),
                ('hsn_code', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('rate', models.IntegerField()),
                ('taxable_value', models.IntegerField()),
                ('packaging', models.IntegerField()),
                ('total_amount_before_tax', models.IntegerField()),
                ('cgst', models.IntegerField()),
                ('sgst', models.IntegerField()),
                ('total_amount_after_tax', models.IntegerField()),
                ('date', models.DateField(auto_now_add=True, verbose_name='Date')),
            ],
        ),
    ]