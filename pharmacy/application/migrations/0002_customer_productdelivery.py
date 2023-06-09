# Generated by Django 4.2 on 2023-04-13 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('sex', models.CharField(choices=[['M', 'Male'], ['F', 'Female']], max_length=20)),
                ('pharmacy', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='application.pharmacy')),
            ],
        ),
        migrations.CreateModel(
            name='ProductDelivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery_person', models.CharField(blank=True, max_length=100)),
                ('fee', models.IntegerField(blank=True, default=0)),
                ('date', models.DateField()),
                ('pickup', models.BooleanField()),
                ('details', models.TextField(blank=True, max_length=300)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='application.customer')),
                ('pharmacy', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='application.pharmacy')),
            ],
        ),
    ]
