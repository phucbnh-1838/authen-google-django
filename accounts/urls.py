from django.conf.urls import url
from views import UserProfile

namespace = 'accounts'
urlpatterns = [
    url(r'^/profile/', UserProfile.as_view(), name="profile")
]
