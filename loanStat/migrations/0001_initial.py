# Generated by Django 3.1.7 on 2021-11-14 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Borrowers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('loan_id', models.IntegerField()),
                ('state', models.CharField(max_length=255)),
                ('loan_amt', models.IntegerField()),
                ('amt_paid', models.IntegerField()),
            ],
        ),
    ]