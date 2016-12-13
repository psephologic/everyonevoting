from django.db import models
from django.contrib.auth.models import User


class BaseEMSModel(models.Model):
    # TODO: Test case
    # TODO: Should this be a private class?
    # TODO: Should we also have a ManagementItem superclass?

    """
    The BaseEMSModel handles all common fields and behaviors of the EMS
    management items provided within the system.
    """

    # logging/auditing
    # signals

    #Audit fields
    date_created = models.DateTimeField(auto_now_add=True)
    #created_by = models.ForeignKey(User)
    date_updated = models.DateTimeField(auto_now=True)
    #updated_by = models.ForeignKey(User)

    class Meta:
        abstract = True

#TODO: Do we need an EML Core model that tracks standard compliance?

