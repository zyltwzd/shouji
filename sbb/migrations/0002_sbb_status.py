# Generated by Django 2.0 on 2019-01-02 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sbb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sbb',
            name='status',
            field=models.SmallIntegerField(choices=[(0, '在用'), (1, '备用'), (2, '返厂'), (3, '故障')], default=0, verbose_name='设备状态'),
        ),
    ]
