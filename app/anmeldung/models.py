from django.db import models

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _

class AnmeldungManager(BaseUserManager):
    """ Manager for user profiles """
    def create_user(self, email, first_name, last_name, phone_no, password=None):
        """ Create a new user profile """
        if not email:
            raise ValueError('User must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name, phone_no=phone_no)

        user.set_password(password)
        user.save(using=self._db)

        return user


    def create_superuser(self, email, password):
        """ Create a new superuser profile """
        user = self.create_user(email, password=password, first_name='Admin', last_name='Admin', phone_no='1234')
        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user

class User(AbstractBaseUser, PermissionsMixin):
    """ Database model for users in the system """
    email = models.EmailField(_("email address"), blank=True, unique=True)

    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)

    phone_no = models.CharField(max_length=255)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )

    objects = AnmeldungManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    ordering = ('email',)

    def __str__(self):
        """ Return string representation of our user """
        return self.email

