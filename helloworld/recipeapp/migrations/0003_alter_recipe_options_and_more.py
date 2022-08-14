# Generated by Django 4.0.6 on 2022-07-12 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipeapp', '0002_alter_recipe_calories_alter_recipe_rating'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recipe',
            options={'ordering': ['recipe_name', 'rating']},
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='cooksetting',
            new_name='cook_setting',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='cooktime',
            new_name='cook_time_min',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='preptime',
            new_name='prep_time_min',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='name',
            new_name='recipe_name',
        ),
        migrations.AlterField(
            model_name='recipe',
            name='directions',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='utensils',
            field=models.CharField(max_length=500),
        ),
    ]
