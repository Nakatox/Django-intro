from django.urls import path
from paste.views import markdownview, index
urlpatterns = [
    path('', index),
    path('<slug:url>', markdownview),
]