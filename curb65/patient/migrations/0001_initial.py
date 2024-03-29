# Generated by Django 4.1.7 on 2023-03-04 19:32

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
                ('patient_id', models.CharField(max_length=10, unique=True)),
                ('dob', models.DateField(default=None)),
                ('confusion', models.BooleanField()),
                ('blood_urea', models.IntegerField()),
                ('respiratory_rate', models.IntegerField()),
                ('systolic_bp', models.IntegerField()),
                ('diastolic_bp', models.IntegerField()),
                ('score', models.IntegerField(default=0)),
            ],
        ),
    ]
