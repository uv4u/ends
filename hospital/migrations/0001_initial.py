# Generated by Django 4.0.6 on 2022-07-26 14:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital_Information',
            fields=[
                ('hospital_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('hospital_name', models.CharField(max_length=200)),
                ('hospital_address', models.TextField()),
                ('hospital_email', models.CharField(max_length=200)),
                ('hospital_phone_number', models.IntegerField(default=0)),
                ('hospital_type', models.CharField(choices=[('private', 'Private hospital'), ('public', 'Public hospital')], max_length=200)),
            ],
        ),
    ]