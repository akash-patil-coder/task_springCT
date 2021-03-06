# Generated by Django 4.0.3 on 2022-03-09 09:39

from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('Roll_no', models.IntegerField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=30)),
                ('Email', models.EmailField(max_length=254)),
                ('Phone', phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Course_Name', models.CharField(max_length=30)),
                ('Professor_Name', models.CharField(max_length=30)),
                ('Description', models.CharField(max_length=30)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Firstapp.student')),
            ],
        ),
    ]
