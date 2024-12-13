from django.urls import path
from . import views
from user.views import DataTableAPIView

urlpatterns = [
    path('list/', views.user_list),
    path('datatable_list', DataTableAPIView.as_view())
]