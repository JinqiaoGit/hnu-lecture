# Generated by Django 4.0.5 on 2022-06-24 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ner', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documents',
            name='doc_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]