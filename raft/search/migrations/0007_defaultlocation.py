# Generated by Django 2.2.5 on 2019-09-06 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0006_viewedrafts'),
    ]

    operations = [
        migrations.CreateModel(
            name='DefaultLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=20)),
            ],
        ),
    ]
