# Generated by Django 4.2 on 2023-04-14 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bot_api', '0003_alter_road_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='road',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='roads', to='bot_api.city', verbose_name='Населённый пункт'),
        ),
    ]
