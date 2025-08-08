from django.contrib import admin
from .models import Board, Column, Epic, Task, SubTask, Card

admin.site.register(Board)
admin.site.register(Column)
admin.site.register(Epic)
admin.site.register(Task)
admin.site.register(SubTask)
# admin.site.register(Card)  # deixe enquanto migrar; remova depois
