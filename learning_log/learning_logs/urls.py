#定义learning_logs的url模式
from django.urls import path
from . import views
app_name = 'learning_logs'
urlpatterns = [
    #主题
    path('', views.index, name='index'),
    #显示所有主题
    path('topics/', views.topics, name='topics'),
    #显示特点主题
    path('topics/<int:topic_id>/', views.topic, name='topic'),
]