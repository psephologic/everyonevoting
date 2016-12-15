from django.db import models
from django.contrib.auth.models import User

from . import BaseEMSModel


class Organization(BaseEMSModel):
    # TODO: Test case
    """
    Compliant with EML Core v.7-0., ManagingAuthorityStructure
    This serves as the 'organization' to hold the election. We will probably
    commonly refer to it as the organization, but technically adhere to the
    EML terminology as much as possible.
    """

    # EML Core Elements
    name = models.CharField(max_length=100)  #TODO: EML mapping
    url = models.URLField(blank=True)
    description = models.TextField(blank=True)
    # Initially assign the user that established the organization
    # TODO: Remove unique from column (why?)
    responsible_officer = models.ForeignKey(User, unique=False)
    administrators = models.ManyToManyField(User, related_name="org_admins+")
    #voters = models.ManyToManyField('Voter', related_name="org_voters+",
    #    blank=True)


    # Subdomain is site "short name." Only 63 chars allowed per standard!
    subdomain = models.SlugField(max_length=63, blank=True)

    date_established = models.DateField(null=True, blank=True)
    general_email = models.EmailField(blank=True)

    headquarters_address_primary = models.CharField(max_length=100,
        blank=True)
    headquarters_address_secondary = models.CharField(max_length=100,
        blank=True)
    headquarters_city = models.CharField(max_length=50, blank=True)
    headquarters_state = models.CharField(max_length=30, blank=True)
    headquarters_zip = models.CharField(max_length=10, blank=True)

    billing_email = models.EmailField(blank=True)
    billing_address_primary = models.CharField(max_length=100, blank=True)
    billing_address_secondary = models.CharField(max_length=100, blank=True)
    billing_city = models.CharField(max_length=50, blank=True)
    billing_state = models.CharField(max_length=30, blank=True)
    billing_zip = models.CharField(max_length=10, blank=True)
    # Election rules (text)
    # Org. bylaws (file)
    # Logo
    # Social media links

    def headquarters_location(self):
        return self.headquarters_city+', '+self.headquarters_state

    def headquarters_address(self):
        return "{} {}, {} {}".format(
            self.headquarters_address_primary,
            self.headquarters_city,
            self.headquarters_state,
            self.headquarters_zip
            )

    organization_address = headquarters_address
    # EML compliance;
    # #TODO turn to property?

    def __str__(self):
        return self.organization_name

    class Meta:
        pass
