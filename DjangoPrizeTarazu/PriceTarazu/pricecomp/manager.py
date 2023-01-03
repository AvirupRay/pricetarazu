from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, uemail, password = None, **extra_fields):
        if not uemail:
            raise ValueError("User Email is required")

        user = self.model(uemail = uemail, **extra_fields)
        user.set_password(password)
        user.save(using = self._db)
        return user


    def create_superuser(self, uemail, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("is_staff must be true for Superuser")

        return self.create_user(uemail, password, **extra_fields)