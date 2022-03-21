# -*- coding: utf-8 -*-

from django.db import migrations, models
import tool.models


class Migration(migrations.Migration):
    dependencies = [
        ('tool', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checktask',
            name='file',
            field=models.FileField(upload_to=tool.models.get_photo_path, verbose_name='上传文件路径'),
        ),
    ]
