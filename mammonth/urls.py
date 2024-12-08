"""
URL configuration for mammonth project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from user.views import t1,t2,t3,t4,t5  # 测试使用，生产不建议写在这里

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('users/', include('user.urls')),  # /users/ 去往二级路由了
    path('index.html', t2), # 测试
    path('test.jsp', t3), # /test.jsp -> t3
    path('t4.cc', t4),
    path('t5', t5),
]

print(urlpatterns)