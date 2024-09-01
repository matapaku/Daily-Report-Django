from django.urls import path
from .views import NippoCreateView, nippoCreateView, NippoListView, nippoListView, nippoDetailView, nippoUpdateView, nippoDeleteView, NippoDetailView

urlpatterns = [
    # path("", nippoListView, name="nippo-list"),
    # path("detail/<int:pk>/", nippoDetailView, name="nippo-detail"),
    # path("create/", nippoCreateView, name="nippo-create"),
    path("update/<int:pk>/", nippoUpdateView, name="nippo-update"),
    path("delete/<int:pk>/", nippoDeleteView, name="nippo-delete"),

    path("", NippoListView.as_view(), name="nippo-list"),
    path("detail/<int:pk>/", NippoDetailView.as_view(), name="nippo-detail"),
    path("create/", NippoCreateView.as_view(), name="nippo-create"),
]
