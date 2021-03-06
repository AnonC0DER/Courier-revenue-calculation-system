# Generated by Django 3.2.9 on 2022-04-28 20:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courier', '0001_initial'),
        ('income', '0003_decreaseincome_increaseincome'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeeklyIncome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saturday', models.DateField(help_text='Put date of first day of the week')),
                ('income', models.PositiveIntegerField()),
                ('courier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courier.courier')),
            ],
        ),
        migrations.CreateModel(
            name='DailyIncome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField()),
                ('date', models.DateField(auto_now_add=True)),
                ('courier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courier.courier')),
            ],
        ),
    ]
