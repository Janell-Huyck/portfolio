# Generated by Django 3.0.6 on 2020-07-27 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='repository',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='language',
            field=models.CharField(blank=True, choices=[('JS', 'JavaScript'), ('DJ', 'Django'), ('RR', 'React-Redux'), ('RE', 'React')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='slug',
            field=models.SlugField(editable=False, unique=True),
        ),
    ]