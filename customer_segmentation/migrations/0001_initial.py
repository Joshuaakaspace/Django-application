# Generated by Django 3.2.8 on 2022-12-02 19:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Accounts1',
            fields=[
                ('a_number', models.CharField(max_length=20, primary_key='true', serialize=False)),
                ('account_name', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('account_status', models.CharField(blank=True, choices=[('Active', 'Active'), ('Inactive', 'Inactive'), ('Cancelled', 'Cancelled')], default='', max_length=40, null=True)),
                ('address', models.CharField(blank=True, default='', max_length=300, null=True)),
                ('country', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('exit_rate', models.IntegerField(blank=True, default=0, null=True)),
                ('exit_rate_usd', models.IntegerField(blank=True, default=0, null=True)),
                ('oppertunity_type', models.IntegerField(blank=True, default=0, null=True)),
                ('ultimate_parent', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('sfdc_segmentation', models.CharField(blank=True, default='', max_length=300, null=True)),
                ('org_type_1', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('org_type_2', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('org_type_3', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('org_type_4', models.CharField(blank=True, default=None, max_length=300, null=True)),
                ('org_type_5', models.CharField(blank=True, default=None, max_length=300, null=True)),
                ('segment_source', models.CharField(blank=True, default=None, max_length=300, null=True)),
                ('entity_url', models.CharField(blank=True, default=None, max_length=300, null=True)),
                ('unavailable', models.CharField(blank=True, default='', max_length=300, null=True)),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='date_modified')),
                ('last_updated', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
