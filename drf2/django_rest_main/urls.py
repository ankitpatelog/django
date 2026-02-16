from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # students app
    path('', include('students.urls')),   # ← comma added here

    # api endpoints
    path('api/v1/', include('api.urls')),
]
