from django.urls import path
from . import views

# this like app.use() in express
urlpatterns = [
    path('', views.Home.as_view(), name="home"), # <- here we have added the new path
    path('objectives/', views.ObjectiveList.as_view(), name='objectives'),
    path('objectives/new/', views.ObjectiveCreate.as_view(), name='objective_create'),
    path('objectives/<int:pk>', views.ObjectiveDetail.as_view(), name='objective_detail'),
    path('objectives/<int:pk>/update', views.ObjectiveUpdate.as_view(), name='objective_update'),
    path('objectives/<int:pk>/delete', views.ObjectiveDelete.as_view(), name='objective_delete'),
    path('accounts/signup/', views.Signup.as_view(), name="signup"),
    path('keyresults/', views.ObjectiveList.as_view(), name='keyresults'),
    path('keyresults/new/', views.KeyResultCreate.as_view(), name='objective_create'),
    path('keyresults/<int:pk>', views.KeyResultDetail.as_view(), name='objective_detail'),
    path('keyresults/<int:pk>/update', views.KeyResultUpdate.as_view(), name='objective_update'),
    path('keyresults/<int:pk>/delete', views.KeyResultDelete.as_view(), name='objective_delete'),

]
