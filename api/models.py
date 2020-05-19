from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class User(AbstractUser):
    email = models.EmailField(unique=True)
    picture = models.TextField(blank=True, null=True)
    linkedin = models.TextField(blank=True, null=True)
    behance = models.TextField(blank=True, null=True)
    twitter = models.TextField(blank=True, null=True)
    instagram = models.TextField(blank=True, null=True)
    facebook = models.TextField(blank=True, null=True)
    youtube = models.TextField(blank=True, null=True)

class BaseProfile(models.Model):
    description = models.TextField(blank=True, null=True)
    education = models.TextField(blank=True, null=True)
    date_joined = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True

class MentorProfile(BaseProfile):
    user = models.OneToOneField(
        User,
        on_delete=models.SET_NULL,
        related_name='mentor_profile',
        null=True
    )
    skills = models.TextField(blank=True, null=True)
    finished_mentorships_count = models.IntegerField(default=0)
    mentorships_ranking_accumulator = models.IntegerField(default=0)

    class Meta:
        db_table = 'api_mentor_profile'

class MenteeProfile(BaseProfile):
    user = models.OneToOneField(
        User,
        on_delete=models.SET_NULL,
        related_name='mentee_profile',
        null=True
    )

    class Meta:
        db_table = 'api_mentee_profile'

class Mentorship(models.Model):
    status = models.TextField()
    mentor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='mentorship_mentor')
    mentee = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='mentorship_mentee')
    date_created = models.DateTimeField(default=timezone.now)
    date_finished = models.DateTimeField(blank=True, null=True)
    objective = models.TextField()
    rejection_reason = models.TextField(blank=True, null=True)
    finish_reason = models.TextField(blank=True, null=True)
    mentee_request_comments = models.TextField(blank=True, null=True)
    ranking = models.IntegerField(blank=True, null=True)

class Message(models.Model):
    mentorship = models.ForeignKey(
        Mentorship,
        on_delete=models.DO_NOTHING)
    sender = models.ForeignKey(
        User,
        on_delete=models.CASCADE)
    text = models.TextField()
    date_sent = models.DateTimeField(default=timezone.now) 

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='notifications')
    from_user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='from_user', null=True)
    mentorship = models.ForeignKey(Mentorship, on_delete=models.DO_NOTHING, related_name='mentorship', null=True)
    role = models.TextField()
    notification_type = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    viewed = models.BooleanField(default=False)

class ContactMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='contact_message')
    message = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'api_contact_message'