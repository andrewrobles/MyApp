from django.db import models
from .utils import strike

class ToDoItem(models.Model):
    _text = models.CharField(max_length=200)
    done = models.BooleanField(default=False)

    @property 
    def text(self):
        return strike(self._text) if self.done else self._text
    
    def __str__(self):
        return self.text