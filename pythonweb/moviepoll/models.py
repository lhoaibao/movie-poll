from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def cal_total_vote(self):
        total = 0
        for choice in self.choice_set.all():
            total += choice.votes
        return total

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    Question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def percen(self):
        return round(self.votes / self.Question.cal_total_vote() * 100,2)

    def __str__(self):
        return self.choice_text
