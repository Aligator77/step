from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-added_at')
    def popular(self):
        return self.order_by('-rating')


class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, related_name='+', default=1)
    likes = models.ManyToManyField(User, default=1)
#    def new(self):
#        return self.0 #return last added quest
#    def popular(self):
#        m = self.0
#        for s in self:
#            if(m.rating<s.rating):
#                m = s
#        return self #return sorting by rating quest
#    class Meta:
#        ordering = ['-added_at']




class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question, null=False, on_delete=models.DO_NOTHING)
    author = models.ForeignKey(User, related_name='+', default=1)


