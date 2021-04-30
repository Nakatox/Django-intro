from django.urls import path
from markdown.views import markdownview, index
urlpatterns = [
    path('', index),
    path('<slug:url>', markdownview),
]