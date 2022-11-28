from django.urls import path
from polls import views
from django.views.generic import RedirectView

app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    path('policy', views.policy, name='policy'),
    path('survey', views.survey, name='survey'),
    path('result', views.results, name='result'),
    path('values', views.values, name='values'),
    path('finish', views.finish, name='finish')
]