# Generated by Django 2.2.5 on 2019-11-01 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestModel', '0006_auto_20191031_1143'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='账号')),
                ('pwd', models.CharField(max_length=100, verbose_name='密码')),
                ('email', models.EmailField(max_length=254, verbose_name='电子邮箱')),
                ('phone', models.CharField(max_length=100, verbose_name='电话')),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
