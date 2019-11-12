# Generated by Django 2.2.4 on 2019-11-10 18:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PersonModel',
            fields=[
                ('aadhar', models.IntegerField(primary_key=True, serialize=False)),
                ('pname', models.CharField(max_length=30)),
                ('contact', models.IntegerField()),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PassportModel',
            fields=[
                ('pno', models.IntegerField(primary_key=True, serialize=False)),
                ('p_details', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app1.PersonModel')),
            ],
        ),
    ]