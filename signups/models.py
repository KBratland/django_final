from django.db import models

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
        return self.email
