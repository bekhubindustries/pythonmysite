# Generated by Django 4.2.6 on 2023-10-22 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_category_alter_shop_options_shop_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='photo_path1',
            field=models.ImageField(default='2144250001_2_1_16.png', upload_to='photo/%Y/%M/%D/', verbose_name='Картинка '),
        ),
        migrations.AddField(
            model_name='shop',
            name='photo_path2',
            field=models.ImageField(default='2144250001_2_1_16.png', upload_to='photo/%Y/%M/%D/', verbose_name='Картинка '),
        ),
        migrations.AddField(
            model_name='shop',
            name='photo_path3',
            field=models.ImageField(default='2144250001_2_1_16.png', upload_to='photo/%Y/%M/%D/', verbose_name='Картинка '),
        ),
    ]
