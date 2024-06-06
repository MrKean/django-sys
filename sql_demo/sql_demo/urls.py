

from django.contrib import admin
from django.urls import path, include
urlpatterns = [

    path('', include('curd_sql_demo.urls')),
    # path('curd_sql_demo/', include('curd_sql_demo.urls')),
    path('admin/', admin.site.urls),
    # 更多URL模式...
]