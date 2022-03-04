from django.urls import path
from index import views

app_name = 'index'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('tools/', views.Tool.as_view(), name='tools'),
    path('news/', views.News.as_view(), name='news'),
    path('guide/', views.Guide.as_view(), name='guide'),
    path('content/news/id/<int:pk>/', views.DetailNews.as_view(), name='post-News'),
    path('content/tools/id/<int:pk>/', views.DetailTools.as_view(), name='post-Tools'),
    path('content/guid/id/<int:pk>/', views.DetailGuid.as_view(), name='post-Guid'),
]
