# Generated by Django 5.0.2 on 2024-02-29 16:33

import django_ckeditor_5.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_alter_article_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=django_ckeditor_5.fields.CKEditor5Field(blank=True, verbose_name='Content'),
        ),
    ]
