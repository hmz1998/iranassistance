from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser

from django.core.validators import (
    MinLengthValidator,
    EmailValidator
)

from painless.models import UUIDBaseModel

from users.managers import UserManager

class User(AbstractBaseUser, UUIDBaseModel, PermissionsMixin):
    USER_TYPE_CHOICES = (
        ('n', ("Normal user")),
        ('s', ("Silver user")),
        ('g', ("Gold user")),
    )

    username = models.CharField(
        ('Username'),
        max_length=15,
        unique=True,
        validators=[MinLengthValidator(5, "Username cannot be less than 5 characters")],
        error_messages={
            'unique': ("A user with that username already exists."),
        },
    )

    email = models.EmailField(
        ('email address'),
        validators=[EmailValidator],
        null=True,
        blank=True,
        error_messages={
            'unique': ("A user with that email already exists."),
        },
        unique=True
    )
    
    type = models.CharField(
        ("Type"),
        choices=USER_TYPE_CHOICES,
        max_length=1,
        default = 'n'
    )

    first_name = models.CharField(('first name'), max_length=30, blank=True)
    last_name = models.CharField(('last name'), max_length=30, blank=True)

    date_joined = models.DateTimeField(('date joined'), auto_now_add=True)
    is_active = models.BooleanField(('active'), default=False)
    is_staff = models.BooleanField(default=False)
    last_login = models.DateTimeField(null=True)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = ('user')
        verbose_name_plural = ('users')

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def __str__(self):
        return f'{self.username}'

    def __repr__(self):
        return f'{self.username}'
