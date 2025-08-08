from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from board.views import BoardViewSet, ColumnViewSet, CardViewSet, index

router = DefaultRouter()
router.register(r'boards', BoardViewSet)
router.register(r'columns', ColumnViewSet)
router.register(r'cards', CardViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', index, name='index'),   # frontend
]
