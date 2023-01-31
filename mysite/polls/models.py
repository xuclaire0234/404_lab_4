# from django.db import models

# Create your models here.
import datetime
from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self) -> str:
        return self.question_text
    def was_publish_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
class Choice(models.Model):
    # choice is related with question 
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)