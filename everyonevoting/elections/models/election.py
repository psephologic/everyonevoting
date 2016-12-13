import pytz

from django.db import models

from core.models import BaseEMSModel, Organization


class Election(BaseEMSModel):
    """Election specification."""

    organization = models.ForeignKey(Organization)
    name = models.CharField(max_length=100, default='New Election')
    # TODO: This should be conditional based on the type of organization
    # (private vs public)
    TYPE = (
        (u'Annual', u'annual'),
        (u'Primary', u'primary'),
        (u'General', u'general'),
        (u'Mid-term', u'mid-term'),
        (u'Special', u'special'),
        (u'Runoff', u'runoff'),
    )
    type = models.CharField(max_length=50, choices=TYPE, default='General')
    # TODO: What starts: Balloting? Polls? Election?
    TIME_ZONE = [(tz, tz) for tz in pytz.common_timezones]
    # TODO: Timezone support
    time_zone = models.CharField(max_length=100, blank=True,
        choices=TIME_ZONE, default='UTC')
    # TODO: Convert to CalendarEvent
    event_begin = models.DateTimeField()
    event_end = models.DateTimeField()
    ALLOWED_CHANNELS = (
        (u'In-Person', u'in-person'),
    )
    allowed_channels = models.CharField(max_length=30,
        choices=ALLOWED_CHANNELS, default="In Person")
    languages = models.CharField(max_length=30, default="English")
    CONTEST_ORDERING = (
        ('Manual', 'manual'),
    )
    contest_ordering = models.CharField(max_length=20,
        choices=CONTEST_ORDERING, default='manual')
    is_partisan = models.BooleanField(default=False)
    results_report_begin = models.DateTimeField(null=True, blank=True)
    # TODO: split this up
    VOTER_PARTICIPATION = (
        (u'Optional', u'optional'),
        (u'Required', u'required'),
        (u'Membership', u'membership'),
        (u'Open', u'open'),
        (u'Party', u'party'),
        (u'Exemptions', u'exemptions'),
    )

    def __unicode__(self):
        return '{0}: {1} - {2}'.format(
            self.name,
            self.event_begin.isoformat(),
            self.event_end.isoformat()
        )
