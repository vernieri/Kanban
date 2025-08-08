from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from board.views import (
    BoardViewSet, ColumnViewSet,
    EpicViewSet, TaskViewSet, SubTaskViewSet,
    index
)

router = DefaultRouter()
router.register(r'boards', BoardViewSet)
router.register(r'columns', ColumnViewSet)
router.register(r'epics', EpicViewSet)        # novo
router.register(r'tasks', TaskViewSet)        # novo
router.register(r'subtasks', SubTaskViewSet)  # novo
# Se ainda quiser manter cards:
# from board.views import CardViewSet
# router.register(r'cards', CardViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', index, name='index'),
]
