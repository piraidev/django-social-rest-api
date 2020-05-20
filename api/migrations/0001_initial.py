# Generated by Django 2.1 on 2020-05-20 17:45

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
            name='ContactMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='contact_message', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'api_contact_message',
            },
        ),
        migrations.CreateModel(
            name='MenteeProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mentee_profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'api_mentee_profile',
            },
        ),
        migrations.CreateModel(
            name='MentorProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skills', models.TextField(blank=True, null=True)),
                ('finished_mentorships_count', models.IntegerField(default=0)),
                ('mentorships_ranking_accumulator', models.IntegerField(default=0)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mentor_profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'api_mentor_profile',
            },
        ),
        migrations.CreateModel(
            name='Mentorship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.TextField()),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_finished', models.DateTimeField(blank=True, null=True)),
                ('objective', models.TextField()),
                ('rejection_reason', models.TextField(blank=True, null=True)),
                ('finish_reason', models.TextField(blank=True, null=True)),
                ('mentee_request_comments', models.TextField(blank=True, null=True)),
                ('ranking', models.IntegerField(blank=True, null=True)),
                ('mentee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mentorship_mentee', to=settings.AUTH_USER_MODEL)),
                ('mentor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mentorship_mentor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date_sent', models.DateTimeField(default=django.utils.timezone.now)),
                ('mentorship', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.Mentorship')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.TextField()),
                ('notification_type', models.TextField()),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('viewed', models.BooleanField(default=False)),
                ('from_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='from_user', to=settings.AUTH_USER_MODEL)),
                ('mentorship', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='mentorship', to='api.Mentorship')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='notifications', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
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
                ('education', models.TextField(blank=True, null=True)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
