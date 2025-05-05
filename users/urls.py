from django.urls import path

from users.apps import UsersConfig
from users.views import PaymentListView

app_name = UsersConfig.name


urlpatterns = [
    path("users_list/", PaymentListView.as_view(), name="user_list"),
]
