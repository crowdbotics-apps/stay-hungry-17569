# Generated by Django 2.2.12 on 2020-05-30 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_load_initial_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stay_Hungry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stayhungry', models.BigIntegerField()),
            ],
        ),
    ]
