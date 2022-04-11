# Generated by Django 3.2.12 on 2022-04-07 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wordofmouth', '0010_recipe_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='forked_id',
            field=models.PositiveBigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='recipe',
            name='is_forked',
            field=models.BooleanField(default=False),
        ),
    ]