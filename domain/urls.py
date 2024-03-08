from rest_framework import routers

from .views import AuthorViewSet, UserViewSet, BookViewSet

router = routers.SimpleRouter()
router.register(r"authors", AuthorViewSet)
router.register(r"users", UserViewSet)
router.register(r"books", BookViewSet)
urlpatterns = router.urls


