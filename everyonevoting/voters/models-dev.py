__author__ = 'eronlloyd'

from datetime import datetime
from json import JSONEncoder, JSONDecoder
from django.db import models
from django.contrib.auth.models import User

from core.models import BaseEMSModel, Organization
from locations.models import GeoDistrict

# EML-310: Voter Registration
# ----------------------------------------------------------------------------


class Affiliation(BaseEMSModel):
    """Specifies the affiliations available for voter registrations, such as
    political parties, teams, etc."""
    registered_name = models.CharField(max_length=30)
    abbreviation = models.CharField(max_length=5, blank=True)
    # type = models.CharField(max_length=30)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.registered_name

# NOTE: GeoDistricts and Affiliations are two ways of classifying voters


class VoterRegistration(BaseEMSModel):

    slug = 'voter-registration'

    organization = models.ForeignKey(Organization)
    districts = models.ManyToManyField(GeoDistrict, null=True, blank=True)
    proxy_voter = models.ForeignKey('VoterRegistration', null=True, blank=True)
    proxy_enabled = models.BooleanField(default=False)
    PROXY_PERIOD = (
        (u'None', u'None'),
        (u'Scheduled', u'Scheduled'),
        (u'Permanent', u'Permanent'),
    )
    proxy_period = models.CharField(max_length=10, blank=True, null=True,
        choices=PROXY_PERIOD, default='None')
    proxy_date_begin = models.DateField(null=True, blank=True)
    proxy_date_end = models.DateField(null=True, blank=True)
    proxy_reason = models.CharField(max_length=100, blank=True)
    identifier = models.CharField(max_length=100, blank=True)
    affiliation = models.ForeignKey(Affiliation, null=True, blank=True)
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, blank=True)
    # last_name_prefix = models.CharField(max_length=30, default="",
        # blank=True)
    last_name = models.CharField(max_length=30)
    former_name = models.CharField(max_length=30, blank=True)
    alias = models.CharField(max_length=30, blank=True)
    GENERATION_IDENTIFIER = (
        (u'Jr.', u'Jr.'),
        (u'Sr.', u'Sr.'),
        (u'I', u'I'),
        (u'II', u'II'),
        (u'III', u'III'),
    )
    generation_identifier = models.CharField(max_length=10,
        choices=GENERATION_IDENTIFIER, blank=True)
    # suffix = models.CharField(max_length=30, blank=True)
    # general_suffix = models.CharField(max_length=30, blank=True)
    # TODO: Now that we have the 50+ Facebook options...
    GENDER = (
        (u'Unknown', u'Unknown'),
        (u'Female', u'Female'),
        (u'Male', u'Male'),
    )
    # EML 7.0: 6.1.6 GenderType (compliant)
    gender = models.CharField(max_length=8, choices=GENDER,
        default="Unknown", blank=True)
    ETHNICITY = (
        ('White', 'White'),
        ('Black', 'Black'),
        ('Latino', 'Latino'),
        ('Asian/Pacific Islander', 'Asian/Pacific Islander'),
        ('Native American', 'Native American'),
        ('Mixed/Other', 'Mixed/Other'),
    )
    ethnicity = models.CharField(max_length=30, blank=True, choices=ETHNICITY)
    # nationality = models.CharField(max_length=30, blank=True)
    # birth_place = models.CharField(max_length=30, blank=True)
    # This can be required later, depending on the person's roles and rules.
    birth_date = models.DateField(null=True, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=14, blank=True)
    street_address = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    zip_code = models.CharField(max_length=9, blank=True)
    country = models.CharField(max_length=100, blank=True)
    latitude = models.CharField(max_length=15, blank=True)
    longitude = models.CharField(max_length=15, blank=True)
    registration_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_flagged = models.BooleanField(default=False)

    class Meta:
        pass

    def age(self):
        """Returns person's age in years."""
        # TODO: check for a better algorithm
        today = datetime.date.today()
        # raised when birth date is February 29 and the current year is not a
        # leap year
        try:
            birthday = self.birth_date.replace(year=today.year)
        except ValueError:
            birthday = self.birth_date.replace(year=today.year,
                day=self.birth_date.day-1)
        if birthday > today:
            return today.year - self.birth_date.year - 1
        else:
            return today.year - self.birth_date.year

    def full_name(self):
        if self.middle_name:
            return "%s %s. %s" % (self.first_name, self.middle_name[0],
                self.last_name)
        else:
            return "%s %s" % (self.first_name, self.last_name)

    def __str__(self):
        return self.full_name()


class RegistryImport(BaseEMSModel):
    """Each organization will have an import configuration to """
    # TODO: Eventually we want this based on PostgreSQL's JSON or HStore fields,
    # but for now we just encode as JSON text

    organization = models.ForeignKey(Organization)
    last_import_user = models.OneToOneField(User)
    last_import_date = models.DateTimeField(null=True, blank=True)  # TODO: Default to now
    last_import_added = models.IntegerField(default=0)  # Only track the records added (based on keys)
    # TODO: How do we manage updates? Regardless, we never want to remove records this way.
    current_file = models.FileField(null=True, upload_to='imports/registries/')
    previous_file = models.FileField(null=True)
    field_mappings = models.TextField(blank=True)  # Link field names
    field_keys = models.TextField(blank=True)  # Save all fields as booleans
    # TODO: Some fields could/should be protected; we can specify them too

    def save_mappings(self, mappings):
        encoder = JSONEncoder()
        mappings = encoder.encode(mappings)
        setattr(self.field_mappings, mappings)

    def load_mappings(self):
        decoder = JSONDecoder()
        mappings = decoder.decode(getattr(self.field_mappings))
        return mappings

    def save_keys(self, keys):
        encoder = JSONEncoder()
        keys = encoder.encode(keys)
        setattr(self.field_mappings, keys)

    def load_keys(self):
        decoder = JSONDecoder()
        keys = decoder.decode(getattr(self.field_keys))
        return keys

    def __str__(self):
        return '{0} Registry Import Configuration'.format(self.organization)



class VotingRecord(BaseEMSModel):
    election = models.ForeignKey(Election)
    voter = models.ForeignKey(Voter)
    has_voted = models.BooleanField(default=False)

    def __unicode__(self):
        return self.voter.full_name()+' ('+self.election.name+')'