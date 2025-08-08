from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import render

from .models import Board, Column, Card, Epic, Task, SubTask
from .serializers import (
    BoardSerializer, ColumnSerializer, EpicSerializer,
    TaskSerializer, SubTaskSerializer
)

def index(request):
    return render(request, 'board/index.html')

class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

class ColumnViewSet(viewsets.ModelViewSet):
    queryset = Column.objects.all()
    serializer_class = ColumnSerializer

# ===== NOVO: Epics =====
class EpicViewSet(viewsets.ModelViewSet):
    queryset = Epic.objects.all()
    serializer_class = EpicSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    @action(detail=True, methods=['patch'])
    def move(self, request, pk=None):
        task = self.get_object()
        column_id = request.data.get("column")
        order = request.data.get("order", 0)
        if column_id is None:
            return Response({"detail": "column é obrigatório"}, status=400)
        try:
            new_col = Column.objects.get(id=column_id)
        except Column.DoesNotExist:
            return Response({"detail": "column não encontrado"}, status=404)
        task.column = new_col
        task.order = order
        task.save()
        return Response(TaskSerializer(task).data, status=status.HTTP_200_OK)


# ===== NOVO: SubTasks =====
class SubTaskViewSet(viewsets.ModelViewSet):
    queryset = SubTask.objects.all()
    serializer_class = SubTaskSerializer
