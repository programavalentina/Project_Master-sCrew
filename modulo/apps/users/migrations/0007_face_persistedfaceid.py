# Generated by Django 2.1.2 on 2018-12-18 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_person_idpersonapi'),
    ]

    operations = [
        migrations.AddField(
            model_name='face',
            name='PersistedFaceId',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]