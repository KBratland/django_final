from django.db import models

from signups import SignUp
# Create your models here.


class Person(models.Model):

    fields = (first_name, last_name, email, user_role)
    first_name = models.ForeignKey(SignUp.first_name)
    last_name = models.ForeignKey(SignUp.last_name)
    email = models.ForeignKey(SignUp.email)
    user_role = models.ForeignKey(SignUp.user_role)
    phone = models.IntField()

    def __unicode__(self):
        return smart_unicode(self.email)