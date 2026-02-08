from django.urls import path
from .views import ai_law_assist
from .views import qr_view


urlpatterns = [
    path("ai/", ai_law_assist),
    path('qr/', qr_view, name='qr'),

]

