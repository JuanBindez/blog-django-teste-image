# Generated by Django 4.0.1 on 2022-02-12 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carbonoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='sub_titulo',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
