from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User


class Activity(models.Model):
    """
    The Activity model enables any applicable object to records activity
    during a save() call. Will try to emulate the
    https://www.w3.org/TR/activitystreams-core and
    https://www.w3.org/TR/activitystreams-vocabulary standards.

    Ex.: On August 20, 2015 at 5:13PM, Sarah Johnson changed the Annual Board
    election date from October 12, 2015 to October 17, 2015.
    """

    user = models.ForeignKey(User, unique=False)
    action = models.CharField(30)
    item = models.ForeignKey(models.Model)
    old_value = models.CharField(100)
    new_value = models.CharField(100)


class BaseEMSModel(models.Model):
    """
    The BaseEMSModel handles all common fields and behaviors of the EMS
    management items provided within the system.
    """

    # Audit fields
    date_created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User)
    date_updated = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User)

    class Meta:
        abstract = True


