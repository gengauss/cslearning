# Generated by Django 2.1.2 on 2018-12-13 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Python',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('content', models.TextField(default='')),
                ('exercise', models.TextField(default='')),
                ('solution', models.TextField(default='')),
            ],
        ),
    ]