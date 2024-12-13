from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.user_list),
    # path('get_user_datatable', DataTableAPIView.as_view())
]