from django.db import models

# Create your models here.
class Register(models.Model):
	email = models.CharField(max_length = 20, blank = False)
	password = models.CharField(max_length = 20, blank = False)

	def returnEmail(self):
		return self.email
