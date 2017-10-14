from django.db import models

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField()
    rating = models.IntegerField()
    author = models.CharField(max_length=500)
    likes = models.IntegerField()
    def QuestionManager(self):
        return self
    def new(self):
        return self.0 #return last added quest
    def popular(self):
        m = self.0
        for s in self:
            if(m.rating<s.rating):
                m = s
        return self #return sorting by rating quest
    class Meta:
        ordering = ['-added_at']




class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField()
    author = models.CharField(max_length=500)
    question = models.TextField()

