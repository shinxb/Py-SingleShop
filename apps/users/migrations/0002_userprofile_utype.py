# Generated by Django 2.1.7 on 2020-01-08 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='utype',
            field=models.CharField(choices=[('members', '会员'), ('admin', '管理员')], default='members', max_length=50),
        ),
    ]
