from django.urls import path
from .views import ai_law_assist
from .views import qr_view
from .views import whatsapp_redirect



urlpatterns = [
    path("ai/", ai_law_assist),
    path('qr/', qr_view, name='qr'),
        path("book/", whatsapp_redirect),


]


