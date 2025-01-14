# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-15 15:02
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='devCompChEvi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detectType', models.CharField(blank=True, max_length=20, null=True, verbose_name='检测类型')),
                ('elementsList', models.CharField(blank=True, max_length=300, null=True, verbose_name='元素列表')),
            ],
            options={
                'verbose_name': '爆炸装置案件物证成分子元素表',
                'verbose_name_plural': '爆炸装置案件物证成分子元素表',
            },
        ),
        migrations.CreateModel(
            name='devCompEvi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caseID', models.CharField(max_length=10, verbose_name='案件编号')),
                ('evidenceID', models.CharField(max_length=10, verbose_name='物证编号')),
                ('inputDate', models.DateTimeField(default=datetime.datetime.now, verbose_name='录入日期')),
                ('eviState', models.CharField(blank=True, max_length=30, null=True, verbose_name='物证状态')),
                ('eviMake', models.CharField(blank=True, max_length=30, null=True, verbose_name='物证制备方法')),
                ('eviDraw', models.CharField(blank=True, max_length=30, null=True, verbose_name='物证提取方法')),
                ('eviAnalyse', models.CharField(blank=True, max_length=30, null=True, verbose_name='物证分析方法')),
                ('analyseCondition', models.CharField(blank=True, max_length=30, null=True, verbose_name='分析条件')),
                ('picUrl', models.ImageField(blank=True, null=True, upload_to='image/devCompEvi/', verbose_name='装置物证外观图片路径')),
                ('picDescrip', models.CharField(blank=True, max_length=100, null=True, verbose_name='图片描述')),
                ('note', models.CharField(blank=True, max_length=200, null=True, verbose_name='备注')),
            ],
            options={
                'verbose_name': '爆炸装置案件物证成分表',
                'verbose_name_plural': '爆炸装置案件物证成分表',
            },
        ),
        migrations.CreateModel(
            name='devCompEviFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detectDevice', models.CharField(blank=True, max_length=30, null=True, verbose_name='检测设备名称及型号')),
                ('detectMrfs', models.CharField(blank=True, max_length=20, null=True, verbose_name='仪器厂家')),
                ('inputDate', models.DateTimeField(default=datetime.datetime.now, verbose_name='录入日期')),
                ('detectType', models.IntegerField(choices=[(1, 'FTIF'), (2, 'Raman'), (3, 'XRD'), (4, 'XRF'), (5, 'GC-MS')], verbose_name='检测数据类型')),
                ('docType', models.IntegerField(blank=True, choices=[(1, 'txt'), (2, 'excel'), (3, 'PDF')], null=True, verbose_name='录入文档格式')),
                ('docUrl', models.FileField(blank=True, null=True, upload_to='file/devCompEviFile/', verbose_name='录入文档路径')),
                ('handledUrl', models.FileField(blank=True, null=True, upload_to='', verbose_name='处理完的文件')),
            ],
            options={
                'verbose_name': '爆炸装置案件物证成分文件存储表',
                'verbose_name_plural': '爆炸装置案件物证成分文件存储表',
            },
        ),
        migrations.CreateModel(
            name='devCompEviPeak',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('peakPos', models.FloatField(default=0, verbose_name='峰高位置')),
                ('peakHeight', models.FloatField(default=0, verbose_name='峰高')),
                ('peakArea', models.FloatField(default=0, verbose_name='峰面积')),
            ],
            options={
                'verbose_name': '爆炸装置案件物证成分峰值表',
                'verbose_name_plural': '爆炸装置案件物证成分峰值表',
            },
        ),
        migrations.CreateModel(
            name='devShapeEvi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isCircuit', models.BooleanField(default=False, verbose_name='是否是电路板')),
                ('eviID', models.CharField(max_length=10, verbose_name='物证编号')),
                ('inputDate', models.DateTimeField(default=datetime.datetime.now, verbose_name='录入日期')),
                ('rectCoordi', models.CharField(blank=True, max_length=100, null=True, verbose_name='矩形框坐标（4个）')),
                ('proCoordi', models.CharField(blank=True, max_length=400, null=True, verbose_name='前景颜色点坐标')),
                ('backCoordi', models.CharField(blank=True, max_length=400, null=True, verbose_name='背景颜色点坐标')),
                ('boardCoordi', models.CharField(blank=True, max_length=400, null=True, verbose_name='主板颜色点坐标')),
                ('blackWhiteUrl', models.ImageField(blank=True, null=True, upload_to='image/devShapeEvi/blackWhite/', verbose_name='黑白图像路径')),
                ('interColorUrl', models.ImageField(blank=True, null=True, upload_to='image/devShapeEvi/interColor/', verbose_name='中间彩色图像路径')),
                ('compCheckCoordi', models.CharField(blank=True, max_length=400, null=True, verbose_name='元器件点坐标（校验）')),
                ('boardCheckCoordi', models.CharField(blank=True, max_length=400, null=True, verbose_name='主板像素坐标（校验）')),
                ('featureUrl', models.FileField(blank=True, null=True, upload_to='file/devShapeEvi/feature', verbose_name='特征文件路径')),
                ('resultPicUrl', models.ImageField(blank=True, null=True, upload_to='image/devShapeEvi/result/', verbose_name='结果图像形式路径')),
                ('resultFileUrl', models.FileField(blank=True, null=True, upload_to='file/devShapeEvi/result/', verbose_name='结果文件形式路径')),
                ('originalUrl', models.ImageField(blank=True, null=True, upload_to='image/devShapeEvi/original/', verbose_name='原始图像文件路径')),
                ('originalResolution', models.CharField(blank=True, max_length=30, null=True, verbose_name='原始图像采集分辨率')),
                ('nomUrl', models.ImageField(blank=True, null=True, upload_to='image/devShapeEvi/nom/', verbose_name='归一化图像文件路径')),
                ('nomResolution', models.CharField(blank=True, max_length=30, null=True, verbose_name='归一化图像分辨率')),
                ('note', models.CharField(blank=True, max_length=200, null=True, verbose_name='备注')),
            ],
            options={
                'verbose_name': '爆炸装置案件物证形态表',
                'verbose_name_plural': '爆炸装置案件物证形态表',
            },
        ),
        migrations.CreateModel(
            name='exploChEvi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detectType', models.CharField(blank=True, max_length=20, null=True, verbose_name='检测类型')),
                ('elementsList', models.CharField(blank=True, max_length=300, null=True, verbose_name='元素列表')),
            ],
            options={
                'verbose_name': '炸药及原材料案件物证子元素表',
                'verbose_name_plural': '炸药及原材料案件物证子元素表',
            },
        ),
        migrations.CreateModel(
            name='exploEvi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caseID', models.CharField(max_length=10, verbose_name='案件编号')),
                ('evidenceID', models.CharField(max_length=10, verbose_name='物证编号')),
                ('inputDate', models.DateTimeField(default=datetime.datetime.now, verbose_name='录入日期')),
                ('eviState', models.CharField(blank=True, max_length=30, null=True, verbose_name='物证状态')),
                ('eviMake', models.CharField(blank=True, max_length=30, null=True, verbose_name='物证制备方法')),
                ('eviDraw', models.CharField(blank=True, max_length=30, null=True, verbose_name='物证提取方法')),
                ('eviAnalyse', models.CharField(blank=True, max_length=30, null=True, verbose_name='物证分析方法')),
                ('analyseCondition', models.CharField(blank=True, max_length=30, null=True, verbose_name='分析条件')),
                ('picUrl', models.ImageField(blank=True, null=True, upload_to='image/exploEvi/', verbose_name='炸药物证外观图片路径')),
                ('picDescrip', models.CharField(blank=True, max_length=100, null=True, verbose_name='图片描述')),
                ('note', models.CharField(blank=True, max_length=200, null=True, verbose_name='备注')),
            ],
            options={
                'verbose_name': '炸药及原材料案件物证表',
                'verbose_name_plural': '炸药及原材料案件物证表',
            },
        ),
        migrations.CreateModel(
            name='exploEviFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detectDevice', models.CharField(blank=True, max_length=30, null=True, verbose_name='检测设备名称及型号')),
                ('detectMrfs', models.CharField(blank=True, max_length=20, null=True, verbose_name='仪器厂家')),
                ('inputDate', models.DateTimeField(default=datetime.datetime.now, verbose_name='录入日期')),
                ('detectType', models.IntegerField(choices=[(1, 'FTIF'), (2, 'Raman'), (3, 'XRD'), (4, 'XRF'), (5, 'GC-MS')], verbose_name='检测数据类型')),
                ('docType', models.IntegerField(blank=True, choices=[(1, 'txt'), (2, 'excel'), (3, 'PDF')], null=True, verbose_name='录入文档格式')),
                ('docUrl', models.FileField(blank=True, null=True, upload_to='file/exploEviFile/', verbose_name='录入文档路径')),
                ('handledUrl', models.FileField(blank=True, null=True, upload_to='', verbose_name='处理完的文件')),
                ('exploEvi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exploEviFile', to='evis.exploEvi', verbose_name='对应的物证')),
            ],
            options={
                'verbose_name': '炸药及原材料案件物证文件存储表',
                'verbose_name_plural': '炸药及原材料案件物证文件存储表',
            },
        ),
        migrations.CreateModel(
            name='exploEviPeak',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('peakPos', models.FloatField(default=0, verbose_name='峰高位置')),
                ('peakHeight', models.FloatField(default=0, verbose_name='峰高')),
                ('peakArea', models.FloatField(default=0, verbose_name='峰面积')),
                ('exploEviFile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exploEviPeak', to='evis.exploEviFile', verbose_name='对应的物证文件')),
            ],
            options={
                'verbose_name': '炸药及原材料案件物证峰值表',
                'verbose_name_plural': '炸药及原材料案件物证峰值表',
            },
        ),
    ]
