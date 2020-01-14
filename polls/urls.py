from django.conf.urls import url
from views import AuthenticationGoogle

namespace = 'polls'
urlpatterns = [
    url(r'', AuthenticationGoogle.as_view(), name='index')
]
