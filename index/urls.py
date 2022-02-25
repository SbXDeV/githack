from django.urls import path
from index import views
from index.views import Detail

app_name = 'index'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('tools/', views.Tool.as_view(), name='tools'),
    path('news/', views.News.as_view(), name='news'),
    path('guide/', views.Guide.as_view(), name='guide'),
    path('content/id/<int:pk>/', Detail.as_view(), name='post-detail'),
]
