# Generated by Django 3.2.12 on 2022-03-24 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wordofmouth', '0002_recipe_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='instructions',
            field=models.TextField(blank=True),
        ),
    ]
