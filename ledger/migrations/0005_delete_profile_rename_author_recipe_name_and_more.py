# Generated by Django 5.0.2 on 2024-03-15 02:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ledger', '0004_profile_rename_name_recipe_author_recipe_created_on_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='author',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='created_on',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='updated_on',
        ),
    ]