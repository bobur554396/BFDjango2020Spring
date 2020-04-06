from django.contrib.auth.models import User, AbstractUser, \
    AbstractBaseUser, PermissionsMixin, UserManager
from django.db import models


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
    # USER_ROLES = (
    #     (1, 'admin'),
    #     (2, 'moderator'),
    #     (3, 'editor'),
    # )
    # role = models.IntegerField(choices=USER_ROLES)
    # role = models.ManyToManyField(Role)

    def _try_create_profile_for_user(self, created):
        if created:
            Profile.objects.get_or_create(user=self)

    def save(self, *args, **kwargs):
        print('before saving')

        created = self.id is None

        self.username = f'demo_{self.username}'

        super(MyUser, self).save(*args, **kwargs)

        self._try_create_profile_for_user(created)

        print('after saving')


class Profile(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    bio = models.TextField(default='')
    address = models.TextField(default='')

# class Role(models.Model):
#     name = models.CharField(max_length=200)
#     # permissions
#
#
# class UserRole(models.Model):
#     user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
#     role = models.ForeignKey(Role, on_delete=models.CASCADE)


# a = MyUser.objects.create_editor(username='asd', email='asd@asd.asd', password='asd')


# 4. Substitute by subclassing from AbstractBaseUser
# class MyAbstractUser(AbstractBaseUser, PermissionsMixin):
#     username = models.CharField(max_length=150, unique=True)
#     first_name = models.CharField(max_length=30, blank=True)
#     last_name = models.CharField(max_length=150, blank=True)
#     email = models.EmailField(blank=True)
#     is_staff = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     date_joined = models.DateTimeField()
#
#     objects = UserManager()
#
#     EMAIL_FIELD = 'email'
#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = ['email']
#
#     class Meta:
#         abstract = True
