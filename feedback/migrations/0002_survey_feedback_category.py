# Generated by Django 5.1.4 on 2024-12-07 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='feedback',
            name='category',
            field=models.CharField(choices=[('Workload', 'Workload'), ('Management', 'Management'), ('Team Collaboration', 'Team Collaboration')], default='Uncategorized', max_length=100),
            preserve_default=False,
        ),
    ]
