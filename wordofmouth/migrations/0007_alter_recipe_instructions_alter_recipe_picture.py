# Generated by Django 4.1.dev20220219193601 on 2022-04-02 18:30

from django.db import migrations, models
import django_quill.fields
import wordofmouth.models


class Migration(migrations.Migration):

    dependencies = [
        ('wordofmouth', '0006_merge_20220328_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='instructions',
            field=django_quill.fields.QuillField(),
        ),

        migrations.AlterField(
            model_name='recipe',
            name='picture',
            field=models.FileField(upload_to='', verbose_name=wordofmouth.models.Recipe.rename_file),
        ),
    ]
