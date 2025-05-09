from netbox.api.routers import NetBoxRouter
from . import views

router = NetBoxRouter()
router.register("pdus", views.ControllerView)
urlpatterns = router.urls
