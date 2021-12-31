from django.urls import path
from .views import AllPostView, PostView

urlpatterns = [
    path('', AllPostView.as_view(), name="all_posts"),
    path('<slug:slug>/', PostView.as_view(), name="detail_post"),
]

