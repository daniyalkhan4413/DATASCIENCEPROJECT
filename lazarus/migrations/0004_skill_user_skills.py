# Generated by Django 5.2 on 2025-04-06 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lazarus', '0003_jobposting'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='skills',
            field=models.ManyToManyField(null=True, to='lazarus.skill'),
        ),
    ]
