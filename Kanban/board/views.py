from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Board, Column, Card
from .serializers import BoardSerializer, ColumnSerializer, CardSerializer

from django.shortcuts import render

def index(request):
    return render(request, 'board/index.html')


class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

class ColumnViewSet(viewsets.ModelViewSet):
    queryset = Column.objects.all()
    serializer_class = ColumnSerializer

class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    @action(detail=True, methods=['patch'])
    def move(self, request, pk=None):
        """
        PATCH /api/cards/<id>/move/
        { "column": <column_id>, "order": <int> }
        """
        card = self.get_object()
        column_id = request.data.get("column")
        order = request.data.get("order", 0)
        if column_id is None:
            return Response({"detail": "column é obrigatório"}, status=400)
        try:
            new_col = Column.objects.get(id=column_id)
        except Column.DoesNotExist:
            return Response({"detail": "column não encontrado"}, status=404)
        card.column = new_col
        card.order = order
        card.save()
        return Response(CardSerializer(card).data, status=status.HTTP_200_OK)
