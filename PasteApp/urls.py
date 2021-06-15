from django.urls import path
from . import views
from PasteApp.views import CodePostListView

app_name = 'PasteApp'
urlpatterns = [
    path('', views.home_page, name='home'),
    path('add/', views.add_paste, name='add'),
    path('onadd/', views.on_add_paste, name='on_add'),
    path('paste-list/', CodePostListView.as_view(), name='list'),
    path('delete-paste/<int:paste_id>/', views.delete_paste, name='on_delete'),
    path('paste-view/<int:paste_id>/', views.pasteid, name='pasteid'),
]