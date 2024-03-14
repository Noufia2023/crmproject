from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import RegisterViewSet, LoginViewSet,LeadViewSet



router = DefaultRouter()
router.register(r'register', RegisterViewSet, basename='register')
router.register(r'login', LoginViewSet, basename='login')
router.register(r'leads', LeadViewSet, basename='lead')


urlpatterns = [
    path('', include(router.urls)),
]
