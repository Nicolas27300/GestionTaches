# Generated by Django 2.1.1 on 2018-09-14 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('created_date', models.DateField(auto_now_add=True)),
                ('closed', models.BooleanField(default=False)),
            ],
        ),
    ]