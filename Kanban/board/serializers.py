# board/serializers.py
import re
from rest_framework import serializers
from .models import Board, Column, Epic, Task, SubTask

# ---------- SubTasks ----------
class SubTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTask
        fields = '__all__'


# ---------- Tasks ----------
class TaskSerializer(serializers.ModelSerializer):
    # nested read-only
    subtasks = SubTaskSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = '__all__'  # id, column, epic, title, description, order, color, subtasks

    # validação opcional para a cor (hex #rgb ou #rrggbb)
    def validate_color(self, value: str):
        if value in (None, "",):
            return value
        if not re.fullmatch(r"#([0-9a-fA-F]{3}|[0-9a-fA-F]{6})", value.strip()):
            raise serializers.ValidationError("Use uma cor HEX válida (ex.: #ffcc00).")
        return value.strip()


# ---------- Columns ----------
class ColumnSerializer(serializers.ModelSerializer):
    # nested read-only
    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = Column
        fields = '__all__'  # id, board, name, order, tasks


# ---------- Epics ----------
class EpicSerializer(serializers.ModelSerializer):
    # listar tasks do épico (read-only)
    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = Epic
        fields = '__all__'  # id, board, title, description, order, tasks


# ---------- Boards ----------
class BoardSerializer(serializers.ModelSerializer):
    columns = ColumnSerializer(many=True, read_only=True)
    epics = EpicSerializer(many=True, read_only=True)

    class Meta:
        model = Board
        fields = '__all__'  # id, name, columns, epics
