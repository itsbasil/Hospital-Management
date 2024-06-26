# Generated by Django 4.2 on 2024-04-01 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patientname', models.CharField(max_length=150)),
                ('dob', models.CharField(max_length=150)),
                ('address', models.CharField(max_length=150)),
                ('age', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('contactnum', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=150)),
                ('password', models.CharField(max_length=150)),
                ('password1', models.CharField(max_length=150)),
            ],
        ),
    ]
