from django.urls import path
from . import views

# this like app.use() in express
urlpatterns = [
    path('objectives/new/', views.ObjectiveCreate.as_view(), name='objective_create')
]
