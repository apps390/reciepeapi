# Generated by Django 5.0.5 on 2024-05-07 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='recipe_ingredients',
            field=models.CharField(max_length=500),
        ),
    ]