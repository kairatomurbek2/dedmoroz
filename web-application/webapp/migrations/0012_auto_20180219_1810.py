# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-19 12:10
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0011_homecontent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homecontent',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='contents'),
        ),
    ]
