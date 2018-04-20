from django.db import models

# Create your models here.
class Blog(models.Model):
	title = models.CharField(max_length = 20, blank = False)
	body = models.CharField(max_length = 20, blank = False)
	created_at = models.DateTimeField(auto_now = True, blank = True, null = True)

	def returnTitle(self):
		return self.title

