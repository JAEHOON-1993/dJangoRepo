from django.urls import path

from app.post.views import PostListCreateView, PostDetailView

urlpatterns = [
    path('', PostListCreateView.as_view()),
    path('<int:post_id>', PostDetailView.as_view()),
]