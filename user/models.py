from django.contrib.auth.models import User
from django.db import models

USER_CHOICES = (
    ("buyer", "Buyer"),
    ("seller", "Seller"),
)


# class UserProfile(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, )
#     user_type = models.CharField(max_length=20, choices=USER_CHOICES, default='Buyer')
#     phone_number = models.CharField(max_length=12)
#     country = models.CharField("Country", max_length=20, null=True, blank=True)
#     state = models.CharField("State", max_length=1024, null=True, blank=True)
#     zip_code = models.CharField("ZIP / Postal code", max_length=12, null=True, blank=True)
#     address = models.TextField("Address", null=True, blank=True)
    #
    # def __str__(self):
    #     return self.first_name + self.last_name



from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.

class UserProfileManager(BaseUserManager):
    """Helps Django work with our custom user model."""

    def create_user(self, email, name, password=None):
        """Creates a new user profile object."""

        if not email:
            raise ValueError('Users must have an email address.')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Creates and saves a new superuser with given details."""

        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Respents a "user profile" inside our system."""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    user_type = models.CharField(max_length=20, choices=USER_CHOICES, null=True, blank=True)
    phone_number = models.CharField(max_length=12)
    country = models.CharField("Country", max_length=20, null=True, blank=True)
    state = models.CharField("State", max_length=1024, null=True, blank=True)
    zip_code = models.CharField("ZIP / Postal code", max_length=12, null=True, blank=True)
    address = models.TextField("Address", null=True, blank=True)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Used to get a users full name."""
        return self.name

    def get_short_name(self):
        """Used to get a users short name."""

        return self.name

    def __str__(self):
        """Django uses this when it needs to convert the object to a string"""

        return self.email