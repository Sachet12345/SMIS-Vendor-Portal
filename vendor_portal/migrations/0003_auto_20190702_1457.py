# Generated by Django 2.2.2 on 2019-07-02 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor_portal', '0002_auto_20190702_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='vendorName',
            field=models.TextField(),
        ),
    ]
