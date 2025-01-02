from django.urls import path
from . import views

# this like app.use() in express
urlpatterns = [
    path('objectives/', views.ObjectiveList.as_view(), name='objectives'),
    path('objectives/new/', views.ObjectiveCreate.as_view(), name='objective_create'),
    path('objectives/<int:pk>', views.ObjectiveDetail.as_view(), name='objective_detail'),
    path('objectives/<int:pk>/update', views.ObjectiveUpdate.as_view(), name='objective_update'),
    path('objectives/<int:pk>/delete', views.ObjectiveDelete.as_view(), name='objective_delete'),

]
