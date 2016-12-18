from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User


class BaseModel(models.Model):
    """
    Low-level base class for anything needed beyond the Django Model class.
    """

    # Basic
    created_on = models.DateTimeField(auto_now_add=True)
    #created_by = models.ForeignKey(User, unique=False, null=False)
    updated_on = models.DateTimeField(auto_now=True)
    #updated_by = models.ForeignKey(User, unique=False, null=False)

    class Meta:
        abstract = True

    def create(self):
        pass

    # def save(self, request, *args, **kwargs):
    #     self.updated_by = request.user
    #     self.updated_on = request.date
    #     super(BaseEMSModel, self).save(*args, **kwargs)
    #     # do_something_else()


class ManagementItem(BaseModel):
    """
    The ManagementItem handles all common fields and behaviors of the EMS
    management items provided within the system.
    """

    class Meta:
        abstract = True
