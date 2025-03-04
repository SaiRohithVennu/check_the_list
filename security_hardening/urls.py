from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('login',views.user_login,name='login'),
    path('signup',views.user_signup,name='signup'),
    path('logout',views.user_logout,name='logout'),
    path('external/demo.html',views.demo_view,name='demo'),
    path('external/pricing.html',views.pricing_view,name='pricing'),
    path('external/contact.html',views.contact_view,name='contact'),
    path('internal/home.html',views.home_view,name='home'),
    path('internal/tools.html',views.tools_view,name='tools'),
    path('internal/faq.html',views.faq_view,name='faq'),
    path('internal/feedback.html',views.feedback_view,name='feedback'),
]