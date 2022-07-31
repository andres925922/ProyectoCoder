from django.urls import path
from Base.views import view_about

urlpatterns = [
    path('', view_about, name='about'),
]