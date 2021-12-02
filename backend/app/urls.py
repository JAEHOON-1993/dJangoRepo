from django.urls import path, include

urlpatterns = [
    path('user/', include('app.user.urls')),
    path('verifier/', include('app.verifier.urls')),
    path('post/', include('app.post.urls')),
]
