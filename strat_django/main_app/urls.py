from django.urls import path
from . import views

# this like app.use() in express
urlpatterns = [
    path('', views.Home.as_view(), name="home"), # <- here we have added the new path
    path('roadmaps/', views.Home.as_view(), name="home"), # <- here we have added the new path
    path('objectives/', views.ObjectiveList.as_view(), name='objectives'),
    path('objectives/new/', views.ObjectiveCreate.as_view(), name='objective_create'),
    path('objectives/<int:pk>', views.ObjectiveDetail.as_view(), name='objective_detail'),
    path('objectives/<int:pk>/update', views.ObjectiveUpdate.as_view(), name='objective_update'),
    path('objectives/<int:pk>/delete', views.ObjectiveDelete.as_view(), name='objective_delete'),
    path('swots/', views.SwotList.as_view(), name='swots'),
    path('swots/new/', views.SwotCreate.as_view(), name='swots_create'),
    path('swots/<int:pk>', views.SwotDetail.as_view(), name='swots_detail'),
    path('swots/<int:pk>/update', views.SwotUpdate.as_view(), name='swots_update'),
    path('swots/<int:pk>/delete', views.SwotDelete.as_view(), name='swots_delete'),
    path('swotitems/', views.SwotItemList.as_view(), name='swotitems'),
    path('swotitems/new/<int:swots_id>/', views.SwotItemCreate.as_view(), name='swotitem_create'),
    path('swotitems/<int:pk>', views.SwotItemDetail.as_view(), name='swotitem_detail'),
    path('swotitems/<int:pk>/update', views.SwotItemUpdate.as_view(), name='swotitem_update'),
    path('swotitems/<int:pk>/delete', views.SwotItemDelete.as_view(), name='swotitem_delete'),
    path('accounts/signup/', views.Signup.as_view(), name="signup"),
    path('keyresults/', views.KeyResultList.as_view(), name='keyresults'),
    path('keyresults/new/<int:objective_id>/', views.KeyResultCreate.as_view(), name='keyresult_create'),
    path('keyresults/<int:pk>', views.KeyResultDetail.as_view(), name='keyresult_detail'),
    path('keyresults/<int:pk>/update', views.KeyResultUpdate.as_view(), name='keyresult_update'),
    path('keyresults/<int:pk>/delete', views.KeyResultDelete.as_view(), name='keyresult_delete'),
    path('keyresults/<int:pk>/delete', views.KeyResultDelete.as_view(), name='keyresult_delete'),

]
    