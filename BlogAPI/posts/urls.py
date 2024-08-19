from django.urls import path
from .views import PostViewSet, UserViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register("users", UserViewSet, basename="users"),
router.register("posts", PostViewSet, basename="posts")

urlpatterns = router.urls

# urlpatterns = [
#     path('', PostListView.as_view(), name='post_list'),
#     path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
#     path('users/', UserList.as_view(), name='users'),
#     path('users/<int:pk>/', UserDetail.as_view(), name='user_detail')
# ]
