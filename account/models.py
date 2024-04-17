import uuid
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

CITY_CHOICES=[
    ("Kathmandu","Kathmandu"),
    ("Pokhara","Pokhara")
]

District_CHOICES=[
    ("Kathmandu","Kathmandu"),
    ("Kaski","Kaski")
]


class UserManager(BaseUserManager):
    def create_user(self, email,name,mobile,city,district,address, password=None,password2=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            mobile=mobile,
            city=city,
            district=district,
            address=address
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,name,mobile,city,district,address, password=None,password2=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            name=name,
            mobile=mobile,
            city=city,
            district=district,
            address=address
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    name=models.CharField(max_length=200)
    mobile=PhoneNumberField()
    city=models.CharField(max_length=200,choices=CITY_CHOICES)
    district=models.CharField(max_length=200,choices=District_CHOICES)
    address=models.TextField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name","mobile","city","district","address"]

    def __str__(self):
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