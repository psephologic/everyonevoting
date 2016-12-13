import pytz

from django.db import models

from core.models import BaseEMSModel
from ..models import Election


class Contest(BaseEMSModel):
    election = models.ForeignKey(Election)
    name = models.CharField(max_length=100, default='New Contest')

    class Meta:
        abstract = True


class CandidateContest(Contest):
    seats = models.IntegerField(default=1)
    # Uses method_id (TODO: should we rename to keep consistent?)
    # TODO: Options should depend on the # of seats
    VOTING_METHOD = (
        (u'IRV', u'irv'),
        ('Plurality', 'plurality'),
    )
    voting_method = models.CharField(max_length=25, default=u'IRV',
        choices=VOTING_METHOD, blank=True)
    # defaults; TODO: should we make use of properties for config. attributes?
    allow_write_ins = models.BooleanField(default=False)
    allow_none_of_the_above = models.BooleanField(default=False)
    ballot_order = models.PositiveIntegerField()
    SORTING_METHOD = (
        ('Alphabetical', 'alphabetical'), # Last name?
        ('Incumbents First', 'incumbents first'),
        ('Random', 'random'),
        ('Robson Rotation', 'robson rotation'),
    )
    # Each "ballot" generated activates a sorting method for choices
    sorting_method = models.CharField(max_length=20)


class QuestionContest(Contest):
    question = models.TextField()
    SORTING_METHOD = (
        ('Yes/No', 'yes/no'), # Last name?
        ('No/Yes', 'no/yes'),
        ('Robson Rotation', 'robson rotation'),
    )
    # Each "ballot" generated activates a sorting method for choices
    sorting_method = models.CharField(max_length=20)
    allow_custom_choices = models.BooleanField(default=False)


class Nomination(BaseEMSModel):

    class Meta:
        abstract = True


class Petition(BaseEMSModel):

    class Meta:
        abstract = True


class Choice(BaseEMSModel):

    class Meta:
        abstract = True


class CandidateChoice(Choice):
    pass


class QuestionChoice(Choice):
    pass