# Generated by Django 4.2.11 on 2024-05-05 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whatsappServiceApi', '0002_user_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
