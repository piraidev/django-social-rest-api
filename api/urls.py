from django.conf.urls import url, include
from rest_framework import routers
from api.views import (views,
                       user_viewset,
                       login_view,
                       mentor_profile_views,
                       mentee_profile_views,
                       search_views,
                       conversation_views,
                       mentorship_views,
                       notifications_views,
                       contact_message_view)

router = routers.DefaultRouter(trailing_slash=False)
router.register('users', user_viewset.UserViewSet)
router.register('mentorship', mentorship_views.MentorshipViewSet)

urlpatterns = [
    url('status/', views.status),
    url('facebook_login/', login_view.fb_login),
    url('linkedin_login/', login_view.linkedin_login),
    url('google_login/', login_view.google_login),
    url('users/change_role/', login_view.change_role),
    url(r'^users/(?P<user_id>[0-9]+)/mentor_profile', mentor_profile_views.mentor_profile),
    url(r'^users/(?P<user_id>[0-9]+)/mentee_profile', mentee_profile_views.mentee_profile),
    url('newest_mentors', search_views.newest_mentors),
    url(r'^find-mentors/$', search_views.find_mentors),
    url(r'^conversations/(?P<mentorship_id>[0-9]+)', conversation_views.get_messages),
    url(r'^get_notifications/(?P<user_id>[0-9]+)', notifications_views.get_notifications),
    url(r'^notifications_viewed/(?P<user_id>[0-9]+)', notifications_views.notifications_viewed),
    url('contact_message', contact_message_view.register_contact_message),
    url('', include(router.urls))
]