# Generated by Django 2.2.5 on 2020-03-02 15:48

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('assets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('e556798d-0201-43dc-a1c2-61e321038c81'), editable=False, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('id_number', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=200)),
                ('employee_id', models.CharField(max_length=200)),
                ('role', models.CharField(max_length=200)),
                ('onboarded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Privilege',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('ae2d31fb-c20b-462d-85c2-f2fa349704db'), editable=False, primary_key=True, serialize=False)),
                ('status', models.CharField(max_length=200)),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assets.Asset')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.Staff')),
            ],
        ),
    ]