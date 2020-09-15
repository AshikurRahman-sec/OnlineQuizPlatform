# Generated by Django 3.1.1 on 2020-09-15 20:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ExamManagement', '0002_auto_20200916_0120'),
        ('Accounts', '0001_initial'),
        ('ResultsManagement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marks', models.FloatField(default=0)),
                ('time', models.IntegerField(default=1)),
                ('exam', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ExamManagement.exam')),
                ('examinee', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Accounts.examinee')),
            ],
        ),
    ]
