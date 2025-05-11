from django.db import models

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _
import datetime

class Verbindung(models.Model):
    """relevante Verbindungsdetails"""
    kuerzel = models.CharField('kuerzel', max_length=150, blank=False, unique=True)
    name = models.CharField('name', max_length=255, blank=False)
    REQUIRED_FIELDS = ['kuerzel', 'name']
    def __str__(self):
        """ Return string representation of Verbindung """
        return self.kuerzel

class AnmeldungManager(BaseUserManager):
    """ Manager for user profiles """
    def create_user(self, email, first_name, last_name, phone_no, password=None, **kwargs):
        """ Create a new user profile """
        if not email:
            raise ValueError('User must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name, phone_no=phone_no, **kwargs)

        user.set_password(password)
        user.save(using=self._db)

        return user


    def create_superuser(self, email, password, **kwargs):
        """ Create a new superuser profile """
        user = self.create_user(email, password=password, first_name='Admin', last_name='Admin', phone_no='1234', **kwargs)
        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user

class User(AbstractBaseUser, PermissionsMixin):
    """ Database model for users in the system """
    # Constants
    SCHULUNGEN = (('gk','Grundkurs'), ('fk','Führungskurs'))
    # Primary identifier
    email = models.EmailField(_("email address"), unique=True)
    first_name = models.CharField(_("first name"), max_length=150)
    last_name = models.CharField(_("last name"), max_length=150)
    birthdate = models.DateField(_('birthdate'), default=datetime.date.today)
    couleurname = models.CharField('Couleurname', max_length=150)
    reception = models.DateField('reception', blank=False, default=datetime.date.today)
    burschung = models.DateField('burschung', blank=True, null=True)
    schulung = models.CharField('schulung', max_length=150, choices=SCHULUNGEN)
    chargen = models.CharField('chargen', max_length=150, blank=True)
    verbindung = models.ForeignKey(Verbindung, blank=False, null=True, on_delete=models.SET_NULL)




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

