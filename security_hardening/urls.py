from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import SecurityCheckViewSet
from django.views.generic import TemplateView
from django.http import HttpResponseNotFound

# Create a router and register our viewset with it.
router = DefaultRouter()
router.register(r'securitychecks', SecurityCheckViewSet)

# Custom 404 error handler
def block_internal(request):
    return HttpResponseNotFound()  # Returns 404

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.user_login, name='login'),
    path('signup', views.user_signup, name='signup'),
    path('logout', views.user_logout, name='logout'),
    path('external/demo.html', block_internal,views.demo_view, name='demo'),
    path('external/pricing.html',block_internal, views.pricing_view, name='pricing'),
    path('external/contact.html',block_internal, views.contact_view, name='contact'),
    path('internal/home.html',block_internal, views.home_view, name='home'),
    path('internal/tools.html',block_internal, views.tools_view, name='tools'),
    path('internal/faq.html',block_internal, views.faq_view, name='faq'),
    path('internal/feedback.html',block_internal, views.feedback_view, name='feedback'),
    path('api/', include(router.urls)),  # Added the API endpoint
]

