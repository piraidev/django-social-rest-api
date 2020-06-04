# Generated by Django 2.1 on 2020-05-28 20:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Connection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.TextField()),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_finished', models.DateTimeField(blank=True, null=True)),
                ('objective', models.TextField()),
                ('rejection_reason', models.TextField(blank=True, null=True)),
                ('finish_reason', models.TextField(blank=True, null=True)),
                ('consumer_request_comments', models.TextField(blank=True, null=True)),
                ('ranking', models.IntegerField(blank=True, null=True)),
                ('consumer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='connection_consumer', to=settings.AUTH_USER_MODEL)),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='connection_supplier', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ConsumerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='consumer_profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'on_demand_consumer_profile',
            },
        ),
        migrations.CreateModel(
            name='SupplierProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('finished_connections_count', models.IntegerField(default=0)),
                ('connections_ranking_accumulator', models.IntegerField(default=0)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='supplier_profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'on_demand_supplier_profile',
            },
        ),
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('picture', models.TextField(blank=True, null=True)),
                ('linkedin', models.TextField(blank=True, null=True)),
                ('behance', models.TextField(blank=True, null=True)),
                ('twitter', models.TextField(blank=True, null=True)),
                ('instagram', models.TextField(blank=True, null=True)),
                ('facebook', models.TextField(blank=True, null=True)),
                ('youtube', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='details', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
