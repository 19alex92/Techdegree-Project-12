# Generated by Django 2.2.1 on 2019-05-13 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_application'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='positions', to='projects.Project'),
        ),
    ]
