from django.db import models
from django.utils.encoding import smart_unicode
# Create your models here.


class SignUp(models.Model):
    finder_type = (('Finder', 'Finder'),
                  ('Owner', 'Owner'),
                  ('Both', 'Both'),
                   )
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField()
    user_role = models.CharField(choices=finder_type, max_length=6)
    
    def __unicode__(self):
        return smart_unicode(self.email)
