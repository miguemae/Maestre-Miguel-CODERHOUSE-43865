# Generated by Django 4.2.3 on 2023-07-29 19:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0004_autores'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='fechaInicio',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='tipo',
            field=models.CharField(choices=[('PLATINUM', 'Platinum'), ('GOLD', 'Gold'), ('SILVER', 'Silver'), ('BRONZE', 'Bronze'), ('FREE', 'Free')], default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='membresias',
            name='tipo',
            field=models.CharField(choices=[('PLATINUM', 'Platinum'), ('GOLD', 'Gold'), ('SILVER', 'Silver'), ('BRONZE', 'Bronze'), ('FREE', 'Free')], max_length=50),
        ),
    ]
