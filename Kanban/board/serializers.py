from rest_framework import serializers
from .models import Board, Column, Card, Epic, Task, SubTask

class SubTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTask
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    subtasks = SubTaskSerializer(many=True, read_only=True)
    class Meta:
        model = Task
        fields = '__all__'

class EpicSerializer(serializers.ModelSerializer):
    # Listar tasks do épico (read-only)
    tasks = TaskSerializer(many=True, read_only=True)
    class Meta:
        model = Epic
        fields = '__all__'

# ATUALIZE Column/Board para expor tasks além de cards (enquanto coexistirem)
class ColumnSerializer(serializers.ModelSerializer):
    cards = serializers.SerializerMethodField(read_only=True)   # legado
    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = Column
        fields = '__all__'

    def get_cards(self, obj):
        # manter compat temporária para o frontend antigo
        return [{'id': c.id, 'column': c.column_id, 'title': c.title,
                 'description': c.description, 'order': c.order} for c in obj.cards.all()]

class BoardSerializer(serializers.ModelSerializer):
    columns = ColumnSerializer(many=True, read_only=True)
    epics = EpicSerializer(many=True, read_only=True)

    class Meta:
        model = Board
        fields = '__all__'
