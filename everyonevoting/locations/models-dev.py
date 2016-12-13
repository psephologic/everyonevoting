from django.db import models

from core.models import BaseEMSModel, Organization


class GeoDistrict(BaseEMSModel):
    """EML 150."""

    # TODO: At some point, consider using django-mptt
    # TODO: Should we have a separate model for the district type, where
    # things defining the type of district can be made (ex. pollings places are at this level)?
    organization = models.ForeignKey(Organization)
    name = models.CharField(max_length=100, default='Global')
    LEVEL = (
        ('Global', 'Global'),
        ('Continent', 'Continent'),
        ('Nation', 'Nation'),
    )
    level = models.CharField(max_length=12, blank=True, null=True, choices=LEVEL, default='Global')
    short_name = models.CharField(max_length=20, blank=True)
    description = models.CharField(max_length=250, blank=True,
        default='The global district all voters and elections are assigned to '
                'by default. Elections can take place anywhere in the world.')
    parent = models.ForeignKey('GeoDistrict', null=True, blank=True, default=None)

    def __str__(self):
        return self.name


class PollingLocation(BaseEMSModel):
    name = models.CharField(max_length=100, default='Polling Place')
    address = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    geo_district = models.ForeignKey(GeoDistrict, null=True, blank=True, default=None)

    def __str__(self):
        return self.name