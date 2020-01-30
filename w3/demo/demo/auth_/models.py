from django.db import models

from django.contrib.auth.models import User, AbstractUser, \
    AbstractBaseUser, PermissionsMixin, UserManager


# 1 Proxy model
# class MyUser(User):
#     class Meta:
#         proxy = True
#
#     def asd(self):
#         pass
#
# a = MyUser.objects.all()


# 2. Extend with a one-to-one field to User (Profile)
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
# extra fields

# extra methods


# 3. Substitute by subclassing from AbstractUser

class MyUserManager(UserManager):
    def create_editor(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_editor', True)
        return self._create_user(username, email, password, **extra_fields)


class MyUser(AbstractUser):
    pass
    # is_editor = models.BooleanField(default=False)
    #
    # objects = MyUserManager()


# a = MyUser.objects.create_editor(username='asd', email='asd@asd.asd', password='asd')




# 4. Substitute by subclassing from AbstractBaseUser
class MyAbstractUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField(blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField()

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        abstract = True
