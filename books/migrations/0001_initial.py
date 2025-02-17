# Generated by Django 5.1.5 on 2025-01-29 12:20

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('genre', models.CharField(max_length=100)),
                ('publication_date', models.DateField()),
                ('availability', models.CharField(choices=[('available', 'Available'), ('checked_out', 'Checked Out'), ('lost', 'Lost')], default='available', max_length=20)),
                ('edition', models.CharField(blank=True, max_length=50, null=True)),
                ('summary', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
