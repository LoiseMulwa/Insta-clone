# Generated by Django 4.0.5 on 2022-06-07 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0002_alter_like_response'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='response',
            field=models.CharField(choices=[('Like', 'Like'), ('Unlike', 'Unlike')], default='like', max_length=70),
        ),
    ]
