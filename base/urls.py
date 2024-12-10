from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.loginPage, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path("register/", views.registerPage, name="register"),
    path('profile/<str:pk>', views.userProfile, name="userProfile"),
    path("", views.home, name="home"),
    path("rooms/<str:pk>/", views.room, name="room"),
    path("create-room/", views.createRoom, name="createRoom"),
    path("update-room/<str:pk>/", views.updateRoom, name="updateRoom"),
    path("delete-room/<str:pk>/", views.deleteRoom, name="deleteRoom"),
    path("delete-message/<str:pk>/", views.deleteMessage, name="deleteMessage"),
    path("update-user/", views.updateUser, name="updateUser"),
    path("topics/", views.topicsPage, name="topics"),
    path("activity/", views.activityPage, name="activity"),

]
