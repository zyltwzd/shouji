# Generated by Django 2.0 on 2019-01-02 02:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sbb', '0003_auto_20190102_0208'),
    ]

    operations = [
        migrations.CreateModel(
            name='sbb_gz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sbb_type', models.SmallIntegerField(choices=[(0, '测酒仪'), (1, '模拟机'), (2, '验卡器'), (3, '读卡器'), (4, '自助出退勤'), (5, '其他')], default=0, verbose_name='设备类型')),
                ('bianhao', models.CharField(max_length=64, verbose_name='设备编号')),
                ('guzhang_time', models.DateTimeField(blank=True, null=True, verbose_name='故障时间')),
                ('chuli_time', models.DateTimeField(blank=True, null=True, verbose_name='处理时间')),
                ('zhibanyuan', models.CharField(max_length=16, verbose_name='值班员')),
                ('chuliren', models.CharField(max_length=16, verbose_name='处理人')),
                ('yanshouren', models.CharField(max_length=16, verbose_name='验收人')),
                ('memo', models.TextField(blank=True, null=True, verbose_name='备注')),
                ('m_time', models.DateTimeField(auto_now=True, verbose_name='更新日期')),
                ('business_unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sbb.Shudi', verbose_name='属地')),
            ],
            options={
                'verbose_name': '设备故障记录表',
                'verbose_name_plural': '设备故障记录表',
                'ordering': ['-m_time'],
            },
        ),
    ]