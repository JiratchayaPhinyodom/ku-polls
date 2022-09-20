"""Question models."""
import datetime
from django.contrib import admin
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Question(models.Model):
    """Question model class represent question_text pub_date and end_date."""

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    end_date = models.DateTimeField('the ending date for voting.',
                                    default=timezone.now,
                                    blank=True, null=True)

    def __str__(self):
        """:return The question text."""
        return self.question_text

    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )
    def was_published_recently(self):
        """
        Check the question that was published recently.

        :return boolean True if question was published recently.
        """
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def is_published(self):
        """
        Check the question that is published.

        :return boolean True if question is published.
        """
        now = timezone.now()
        return now >= self.pub_date

    def can_vote(self):
        """
        Check the question at the time that can vote.

        :return boolean True if the question is at the time of voting.
        """
        now = timezone.now()
        return self.pub_date <= now <= self.end_date


class Choice(models.Model):
    """Choice model class represent question choice_text and votes."""

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)

    @property
    def votes(self):
        """:return the number of votes on the choice of polls question."""
        return Vote.objects.filter(choice=self).count()

    def __str__(self):
        """:return the content of choice text."""
        return self.choice_text

class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)