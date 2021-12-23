from django.urls import path
from .views import homePageView , AboutPageView , BasePageView

urlpatterns =[
    path('registration/' , BasePageView.as_view() , name ="registration"),
    path("about/", AboutPageView.as_view() , name="about"),
    path('', homePageView.as_view() ,name='home'),
]