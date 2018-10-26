from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import snippet_detail,snippet_list

urlpatterns = [
    path(r'snippets/',snippet_list),
    path(r'snippets/<int:pk>/',snippet_detail)
]

# urlpatterns = format_suffix_patterns(urlpatterns)