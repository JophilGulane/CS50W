from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("jays", views.jays, name="jays"),
    path("david", views.david, name="david")
]