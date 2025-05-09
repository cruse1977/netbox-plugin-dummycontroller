from netbox.api.routers import NetBoxRouter
from . import views

router = NetBoxRouter()
router.register("say-hello", views.SayHelloView)
urlpatterns = router.urls