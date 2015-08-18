# from django.conf.urls import patterns, include, url
# from django.contrib import admin

# urlpatterns = patterns('',
#     url(r'^admin/', include(admin.site.urls)),
#     url(r'', include('blog.urls', namespace="coolerapp")),   
# )
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('blog.urls')),
     url(r'^polls/', include('polls.urls')),    
     
]