from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views

from api.urls import router
from element.views.element_wiews import ElementListView

# 网站标签页名称
admin.site.site_title = '北斗后台管理'

# 网站名称：显示在登录页和首页
admin.site.site_header = '北斗后台管理'

urlpatterns = [
    path('admin/', admin.site.urls, ),
    path('api-token-auth/', views.obtain_auth_token, name='auth-token'),
    path('api-auth/', include('rest_framework.urls')),
    path('', include('oauth.urls')),
    path('api/', include(router.urls)),
    path('project/', include('project.urls')),
    path('tool/', include('tool.urls')),
    path('eln/', ElementListView.as_view(), name='eln'),
]

handler400 = 'oauth.views.error_views.bad_request'
handler403 = 'oauth.views.error_views.permission_denied'
handler404 = 'oauth.views.error_views.page_not_found'
handler500 = 'oauth.views.error_views.server_error'
