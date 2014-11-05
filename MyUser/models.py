from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
#from simple_email_confirmation import SimpleEmailConfirmationUserMixin


class MyUserManager(BaseUserManager):
    def create_user(self, email,firstname,lastname,username,mobile,password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            firstname=firstname,
            lastname=lastname,
            username = username,
            email=self.normalize_email(email),
            mobile=mobile,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,firstname,lastname,username,mobile,password):
        user = self.create_user(email,
            firstname=firstname,
            lastname=lastname,
            username = username,
            mobile=mobile,
            password=password,
        )
        user.post='presdient'
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    firstname=models.CharField(max_length=32)
    username=models.CharField(max_length=32,unique=True)
    lastname=models.CharField(max_length=32)
    mobile=models.IntegerField(max_length=10)
    #image=models.ImageField(upload_to = 'media',null=True,blank=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['firstname','lastname','email','mobile']

    def get_full_name(self):
        # The user is identified by their email address
        return self.firstname+" "+self.lastname

    def get_short_name(self):
        # The user is identified by their email address
        return self.firstname

    def __unicode__(self):              # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class Message(models.Model):
	user=models.ForeignKey(MyUser)
	message=models.CharField(max_length=140)
	time=models.DateTimeField(auto_now_add=True)
	def __unicode__(self):
		return self.message[0,10]

class Channel(models.Model):
	name = models.CharField(max_length=32)
	messages=models.ForeignKey(Message)
