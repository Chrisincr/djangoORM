# Generated by Django 2.1.7 on 2019-02-19 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_app', '0002_authors_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='authors',
            name='notes',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]