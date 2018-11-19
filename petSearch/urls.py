from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('test',views.result,name='result'),
    path('<int:question_id>/detail/',views.detail,name = 'detail')
]
