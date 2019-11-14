from django.urls import path, include
from .views import BlogListView, BlogDetailView

urlpatterns =[
    path('', BlogListView.as_view(), name='index' ),
    path('posts/<int:pk>', BlogDetailView.as_view(), name='detail'),

]