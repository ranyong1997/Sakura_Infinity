# -*- coding: utf-8 -*-

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CheckTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_name', models.CharField(max_length=100, verbose_name='扫描任务名称')),
                ('file', models.FileField(upload_to='./upload/', verbose_name='上传文件路径')),
                ('task_state',
                 models.CharField(choices=[('runing', 'runing'), ('finish', 'finish'), ('notstarted', 'notstarted')],
                                  default='notstarted', max_length=32, verbose_name='任务状态')),
                ('task_results', models.CharField(blank=True, max_length=32, null=True, verbose_name='任务结果')),
                ('task_report', models.CharField(blank=True, max_length=1000, null=True, verbose_name='任务报告')),
                ('createtime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('creator', models.CharField(max_length=32, verbose_name='创建人')),
            ],
            options={
                'verbose_name': '扫描任务',
                'verbose_name_plural': '扫描任务',
            },
        ),
    ]
