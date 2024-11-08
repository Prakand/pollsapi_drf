from django.urls import include, path
from .views import polls_detail,polls_list
from .apiviews import PollList,PollDetail,LoginView,RegisterView,LogoutView


urlpatterns = [
    path("polls/", PollList.as_view(), name="polls_list"),
    path("polls/<int:pk>/", PollDetail.as_view(), name="polls_detail"),
    path("login/",LoginView.as_view(),name = "login"),
    path('register/',RegisterView.as_view(),name='register_user'),
    path('logout/',LogoutView.as_view(),name="logout_user"),
]