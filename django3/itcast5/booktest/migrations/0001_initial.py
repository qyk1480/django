# Generated by Django 2.0.6 on 2018-06-20 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=10)),
                ('upwd', models.CharField(max_length=40)),
                ('isDelete', models.BooleanField()),
            ],
        ),
    ]
