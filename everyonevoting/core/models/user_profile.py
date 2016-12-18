from django.db import models
from django.conf import settings

from ..models import BaseModel


class UserProfile(BaseModel):
    # TODO: Test case
    # TODO: Decide whether to do this or use AbstractUser
    """
    User profile for user accounts.
    """

    user = models.OneToOneField(settings.AUTH_USER_MODEL)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return "User profile for {0}".format(self.user.username)


#TODO: Create account objects
