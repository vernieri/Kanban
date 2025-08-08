from django.db import models

class Board(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Column(models.Model):
    board = models.ForeignKey(Board, related_name="columns", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.name} ({self.board.name})"


class Card(models.Model):
    column = models.ForeignKey(Column, related_name="cards", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title
