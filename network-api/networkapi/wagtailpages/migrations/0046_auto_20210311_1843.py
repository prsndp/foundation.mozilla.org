# Generated by Django 2.2.17 on 2021-03-11 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailpages', '0045_buyersguideproductcategory_2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='partner_page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='partner_internal_link', to='wagtailcore.Page'),
        ),
    ]
