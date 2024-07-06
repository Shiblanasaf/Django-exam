from django.urls import path
from user.views import *


urlpatterns=[
    path('uhome',userhomeview.as_view(),name="uhome"),
    path('jreg',jobregview.as_view(),name="jreg"),
    path('jlist',JobListView.as_view(),name='jlist')
]