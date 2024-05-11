"""
URL configuration for recipemanagement project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from  rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views as rviews
from recipe import views
router=DefaultRouter()
router.register('recipedetails',views.recipeviewsets)
router.register('userdetails',views.userviewsets,basename='userdetails')
router.register('createreview',views.createreview,basename='create')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('rev/<int:pk>',views.retrievereview.as_view()),
    path('cssr',views.Cuisinefilter.as_view()),
    path('mlsr', views.mealfilter.as_view()),
    path('ingsr',views.ingredientfilter.as_view()),
    path('login/',rviews.obtain_auth_token),
    path('logout', views.userlogout.as_view())

]
