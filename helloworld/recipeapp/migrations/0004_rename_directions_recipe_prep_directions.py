# Generated by Django 4.0.6 on 2022-07-12 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipeapp', '0003_alter_recipe_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='directions',
            new_name='prep_directions',
        ),
    ]
