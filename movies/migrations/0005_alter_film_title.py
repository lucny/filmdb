# Generated by Django 4.2 on 2023-05-17 18:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_alter_attachment_options_film_poster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='title',
            field=models.CharField(help_text='Zadejte název filmu', max_length=200, validators=[django.core.validators.MinLengthValidator(2, 'Název nesmí být kratší než 2 znaky!'), django.core.validators.RegexValidator('^[^+\\-*/%&;:.,]', 'Název nesmí začínat znaky  +-*/%&amp;;:.,!')], verbose_name='Název filmu'),
        ),
    ]
