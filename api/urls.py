from django.urls import path
from . import views

urlpatterns = [
    path("tiffins/", views.TiffinListCreate.as_view(), name="Tiffin-Create-List"),
    path("tiffins/<int:pk>/", views.TiffinRecords.as_view(), name="Update-Delete-Tiffin")
]