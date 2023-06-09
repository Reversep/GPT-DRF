from django.db import models


class Question(models.Model):
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class Answer(models.Model):
    post = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.answer