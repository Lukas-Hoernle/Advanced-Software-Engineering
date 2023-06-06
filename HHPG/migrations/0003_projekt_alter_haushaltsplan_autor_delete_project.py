# Generated by Django 4.2.1 on 2023-05-31 18:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('HHPG', '0002_haushaltsplan_haushaltsposten_haushaltsplan'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projekt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('einnahmen', models.PositiveIntegerField(default=0)),
                ('ausgaben', models.PositiveIntegerField(default=0)),
                ('haushaltsposten', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HHPG.haushaltsposten')),
            ],
        ),
        migrations.AlterField(
            model_name='haushaltsplan',
            name='autor',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Project',
        ),
    ]