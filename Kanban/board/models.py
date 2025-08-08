from django.db import models

class Board(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self): return self.name

class Column(models.Model):
    board = models.ForeignKey(Board, related_name="columns", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)
    class Meta: ordering = ['order']
    def __str__(self): return f"{self.name} ({self.board.name})"

# === NOVO: Epic ===
class Epic(models.Model):
    board = models.ForeignKey(Board, related_name="epics", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)
    class Meta: ordering = ['order']
    def __str__(self): return self.title

# === NOVO: Task ===
class Task(models.Model):
    column = models.ForeignKey(Column, related_name="tasks", on_delete=models.CASCADE)
    epic = models.ForeignKey(Epic, related_name="tasks", on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)
    color = models.CharField(max_length=7, blank=True, default="#fafafa")  # cor hex, ex: #FF0000

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


# === NOVO: SubTask ===
class SubTask(models.Model):
    task = models.ForeignKey(Task, related_name="subtasks", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    is_done = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)
    class Meta: ordering = ['order']
    def __str__(self): return self.title

# === LEGADO: Card (transitório) ===
class Card(models.Model):
    column = models.ForeignKey(Column, related_name="cards", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)
    class Meta: ordering = ['order']
    def __str__(self): return self.title
