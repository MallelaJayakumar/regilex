# Generated by Django 2.1.4 on 2019-07-08 12:37

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('Action', models.CharField(choices=[('1', 'Pending'), ('2', 'Done'), ('3', 'Edit')], default='', max_length=2)),
                ('status', models.CharField(choices=[('1', 'Yes'), ('2', 'No')], default='No', max_length=2)),
            ],
            managers=[
                ('Objects', django.db.models.manager.Manager()),
            ],
        ),
    ]