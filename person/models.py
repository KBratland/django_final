from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


# Create your models here.


class Person(models.Model):

    user = models.OneToOneField(User, primary_key=True)
    # email = models.ForeignKey(User.email)

    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)

    finder_type = (('Finder', 'Finder'),
                  ('Owner', 'Owner'),
                  ('Both', 'Both'),
                   )

    user_role = models.CharField(choices=finder_type, max_length=10)

    def __unicode__(self):
        return "%s's profile" % self.user.username

User.profile = property(lambda u: Person.objects.get_or_create(user=u)[0])