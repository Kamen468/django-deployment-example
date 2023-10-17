from django.urls import path
from .views import index, other, relative

urlpatterns = [
    path("index/", index, name="index"),
    path("other/", other, name="other"),
    path("relative/", relative, name="relative")
]